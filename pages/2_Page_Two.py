import streamlit as st
from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
#from test_vector import create_vector_store

from dotenv import load_dotenv
import os

with st.sidebar:
    "Preview Page"

st.title("🤖 File Upload Q&A")
st.caption("🚀 An AI Champions Bootcamp Project")

uploaded_file = st.file_uploader("Upload a document", type=("txt", "doc", "pdf"))
question = st.text_input(
    "Ask something about the document",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)