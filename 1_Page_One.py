import streamlit as st
from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
#from test_vector import create_vector_store

from dotenv import load_dotenv
import os

st.title("Page One - Individual Income Tax Filing")

# Load environment variables from .env file
load_dotenv()

@st.cache_resource
def initialize_rag():
    documents = load_documents("data/page1_docs")
    vector_store = create_vector_store(documents)
    rag_chain = create_rag_pipeline(vector_store)
    return rag_chain

rag_chain = initialize_rag()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])