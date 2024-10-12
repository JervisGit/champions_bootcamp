from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
import openai

import numpy as np

# Load environment variables from .env file
load_dotenv()

def create_vector_store(documents):

    #embeddings = OpenAIEmbeddings()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

#openai.api_key = os.getenv('OPENAI_API_KEY')