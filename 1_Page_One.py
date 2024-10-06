from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
#from test_vector import create_vector_store

from dotenv import load_dotenv
import os

import openai

# Load environment variables from .env file
load_dotenv()

def initialize_rag():
    documents = load_documents("data/page1_docs")
    vector_store = create_vector_store(documents)
    rag_chain = create_rag_pipeline(vector_store)
    return rag_chain

openai.api_key = os.getenv('OPENAI_API_KEY')

rag_chain = initialize_rag()

#documents = load_documents("data/page1_docs")
#docs = [doc.page_content for doc in documents]
#print(docs)
#vector_store = create_vector_store(documents)

#import numpy as np
#loaded_embeddings = np.load('embeddings.npy')
#print(len(loaded_embeddings))