import hmac
import streamlit as st
from document_loader import load_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_pipeline
#from test_vector import create_vector_store

from dotenv import load_dotenv
import os

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.title("🤖 Chatbot for Individual Income Tax Filing")
st.caption("🚀 An AI Champions Bootcamp Project")

with st.expander("Disclaimer"):
    st.write('''
        IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
    ''')

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

    response = rag_chain({"question": prompt, "chat_history": [(m["role"], m["content"]) for m in st.session_state.messages]})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["answer"])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response["answer"]})