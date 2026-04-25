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
    question: {question}. 
    You assist users with general inquiries based on {context} /
    and  technical issues. /
    """

# define prompt

# init model

# indexing
def load_split_documents():
    """Load a file from path, split it into chunks, embed each chunk and load it into the vector store."""
    raw_text = TextLoader("./docs/faq.txt").load()
    text_splitter = CharacterTextSplitter(chunk_size=30, chunk_overlap=0, separator=".")
    chunks = text_splitter.split_documents(raw_text)
    # print(f"number of chunks {len(chunks)}")
    # print(chunks[0])
    return chunks

# convert to embeddings
def load_embeddings(documents, user_query):
    """Create a vector store from a collection of documents."""
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embeddings)
    docs = db.similarity_search(user_query)
    print(docs)


def generate_response(retriever, query):
    """Generate a response to user query."""
    pass


def query(query):
    """Query the model with user query."""
    """Query the model with a user query."""
    documents = load_split_documents()
    load_embeddings(documents, query)
    query("what is return policy?")
