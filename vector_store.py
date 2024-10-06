from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import openai

import numpy as np

# Load environment variables from .env file
load_dotenv()

def create_vector_store(documents):

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

openai.api_key = os.getenv('OPENAI_API_KEY')