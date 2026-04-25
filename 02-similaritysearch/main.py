from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

template = """Answer the user queries in this context:
{context}

Query: {query}
"""
prompt = ChatPromptTemplate.from_template(template)

model = OpenAI()

# create a vectorstore & embeddings
vectorstore = FAISS.from_texts(
    ["Rishi Raj worked at RiBild"], embedding=OpenAIEmbeddings()
)

# querying the vectorstore
query = "Where did Rishi Raj work?"
""" Number of results kept very small (=1) 
so as to keep number of API calls (and token being used) 
low during 'development' """
docs = vectorstore.similarity_search(query, top_k=1)

# querying as retriever
retriever = vectorstore.as_retriever()
docs = retriever.invoke(query, top_k=1)
print(docs[0].page_content)
# preparing a chain for the retriever
retrieval_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)

response = retrieval_chain.invoke(query)
print(response)