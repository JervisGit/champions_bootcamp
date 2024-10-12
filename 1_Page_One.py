import streamlit as st
from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
#from test_vector import create_vector_store

from dotenv import load_dotenv
import os

with st.sidebar:
    "Preview Page"

st.title("🤖 Chatbot for Individual Income Tax Filing")
st.caption("🚀 An AI Champions Bootcamp Project")

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

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    #response = rag_chain({"question": prompt, "chat_history": [(m["role"], m["content"]) for m in st.session_state.messages]})
    response = rag_chain({"question": prompt, "chat_history": []})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["answer"])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response["answer"]})