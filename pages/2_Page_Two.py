import streamlit as st
from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
import tempfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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

def load_documents(uploaded_files):

    text = []

    file_extension = os.path.splitext(uploaded_files.name)[1]
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_files.read())
        temp_file_path = temp_file.name

    loader = None
    if file_extension == ".pdf":
        loader = PyPDFLoader(temp_file_path)
    elif file_extension == ".docx" or file_extension == ".doc":
        loader = Docx2txtLoader(temp_file_path)
    elif file_extension == ".txt":
        loader = TextLoader(temp_file_path)

    if loader:
        text.extend(loader.load())
        os.remove(temp_file_path)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=100)
    split_documents = text_splitter.split_documents(text)
    
    return split_documents

if uploaded_file and question:
    st.chat_message("user").markdown(question)

    documents = load_documents(uploaded_file)

    vector_store = create_vector_store(documents)
    rag_chain = create_rag_pipeline(vector_store)

    response = rag_chain({"question": question})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["answer"])

