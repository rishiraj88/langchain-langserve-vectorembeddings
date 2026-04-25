import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
)
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.vectorstores import Chroma
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

template: str = """/
    You are a customer support specialist /
    question: {query}. 
    You assist users with general inquiries based on {context} /
    and  technical issues. /
    """

def get_embedding(text_to_embed):
    """ to view the embeddings so created with OpenAI API"""
    response = client.embeddings.create(
        model= "text-embedding-ada-002",
        input=[text_to_embed]
    )
    print(response.data[0].embedding)


# define prompt
system_message__prompt_template = SystemMessagePromptTemplate.from_template(template)
human_message__prompt_template = HumanMessagePromptTemplate.from_template(
    input_variables=["query", "context"], 
    template="{query}"
)
chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message__prompt_template, 
    human_message__prompt_template
])
# init model
model = ChatOpenAI()

# indexing
def load_split_documents():
    """Load a file from path, split it into chunks, embed each chunk and load it into the vector store."""
    raw_text = TextLoader("./docs/faq.txt").load()
    text_splitter = CharacterTextSplitter(chunk_size=30, chunk_overlap=0, separator=".")
    chunks = text_splitter.split_documents(raw_text)
    return chunks

# convert to embeddings
def load_embeddings(documents, user_query):
    """Create a vector store from a collection of documents."""
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embeddings)
    docs = db.similarity_search(user_query)
    return db.as_retriever()

def generate_response(retriever, query):
    """Generate a response to user query."""
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | chat_prompt_template 
        | model 
        | StrOutputParser()
    )
    return chain.invoke(query)

def query(query):
    """Query the model with user query."""
    documents = load_split_documents()
    load_embeddings(documents, query)
    return generate_response(query)
