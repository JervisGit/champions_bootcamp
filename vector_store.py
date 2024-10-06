from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import openai

import numpy as np

# Load environment variables from .env file
load_dotenv()

def create_vector_store(documents):

    docs = [doc.page_content for doc in documents]

    response = openai.Embedding.create(
    	model= "text-embedding-ada-002",
    	input=docs
	)
	# Extract the AI output embedding as a list of floats
    embeddings = response["data"][0]["embedding"]

    #np.save('embeddings.npy', embeddings)

    # Create a custom embedding function
    class CustomEmbeddings:
        def embed_documents(self, _):
            return embeddings
    
    embedding_func = CustomEmbeddings()

    vector_store = DocArrayInMemorySearch.from_documents(
        documents=documents,
        embedding=embedding_func
    )
    
    # Create the vector store
    #vector_store = FAISS.from_documents(documents, embedding_func)

    #vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

openai.api_key = os.getenv('OPENAI_API_KEY')