from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_community.document_loaders import TextLoader
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv
import warnings
import os

warnings.filterwarnings("ignore")

load_dotenv()

llm = ChatOpenAI()
chat_history = []

"""
historical messages and the latest user question, and 
reformulate the question if it makes reference to any information in history
"""
contextualize_q__system_prompt = """Given a chat history and the latest user question {user_input} \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""
contextualize_q__prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q__system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{user_input}"),
    ]
)

# build full QA chain
qna__system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question {user_input}. \
based on {context}.
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\
"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qna__system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{user_input}"),
    ]
)

# indexing
documents = TextLoader("./docs/faq.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="\n")
splits = text_splitter.split_documents(documents)
db = Chroma.from_documents(documents, OpenAIEmbeddings())
retriever = db.as_retriever()

# Retrieve chat history
history_aware__retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q__prompt
)

# Retrieve and generate
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

def generate_response(query):
    """ Generate a response to user query"""
    rag_chain = create_retrieval_chain(history_aware__retriever, question_answer_chain)
    return rag_chain.invoke({
        "chat_history": chat_history,
        "input": query
    })

def query(query):
    """ Query and generate a response"""
    response = generate_response(query)
    chat_history.extend([HumanMessage(content=query), response["answer"]])
    return response
