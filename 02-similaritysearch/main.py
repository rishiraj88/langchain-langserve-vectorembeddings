from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

template = """Answer the user queries in this context:
{context}

Query: {query}
"""
prompt = ChatPromptTemplate.from_template(template)

# create a vectorstore & embeddings
vectorstore = FAISS.from_texts(
    ["Rishi Raj worked at RiBild"], embedding=OpenAIEmbeddings()
)

# querying the vectorstore

# querying as retriever


