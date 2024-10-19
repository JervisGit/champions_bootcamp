import streamlit as st
from utility import check_password
from dotenv import load_dotenv
import os

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.set_page_config(page_title="About Us", layout="wide")

st.title("About Us")
st.caption("🚀 An AI Champions Bootcamp Project")

# Project Scope
st.header("Project Scope")
st.write("""
Our project leverages advanced artificial intelligence to create an intelligent chatbot system. 
This system is designed to assist with individual income tax filing queries and provide a versatile 
Q&A interface for user-uploaded documents.
""")

# Objectives
st.header("Objectives")

# Problem We're Solving
st.subheader("1. Problem We're Solving")
st.write("We aim to address two key challenges:")
st.markdown("""
- The complexity and time-consuming nature of navigating tax-related information for individual income tax filing.
- The difficulty in quickly extracting relevant information from large documents or datasets.
""")

# Our Solution Approach
st.subheader("2. Our Solution Approach")
st.write("Our approach to solving these problems involves:")
approaches = {
    "Simplifying Access to Information": "Creating a user-friendly interface that allows individuals to ask questions in natural language, eliminating the need to navigate complex websites or documents.",
    "Personalized Assistance": "Providing tailored responses based on the specific context of each user's query, whether it's about tax filing or information from their own documents.",
    "Bridging Knowledge Gaps": "Offering explanations and clarifications on complex topics, helping users better understand the information they receive.",
    "Empowering Self-Service": "Enabling users to find answers quickly and independently, reducing the need for direct human support in many cases.",
    "Adaptability": "Creating a system that can handle both standardized information (like tax regulations) and variable content (like user-uploaded documents), making it versatile for different use cases."
}

for approach, description in approaches.items():
    with st.expander(approach):
        st.write(description)

# Why Our AI-Powered Solution is Better
st.subheader("3. Why Our AI-Powered Solution is Better")
advantages = {
    "Enhanced Accessibility": "Users can get answers 24/7 without waiting for human support or searching through lengthy documents.",
    "Consistency": "The system provides uniform, accurate information, reducing the risk of human error or inconsistency.",
    "Scalability": "It can handle a large number of queries simultaneously, making it efficient for wide-scale use.",
    "Continuous Improvement": "The system can be updated with new information quickly, ensuring users always have access to the most current data.",
    "Personalization": "By understanding context and user needs, it provides more relevant and tailored responses than static FAQs or search functions."
}

for advantage, description in advantages.items():
    with st.expander(advantage):
        st.write(description)

# Data Sources
st.header("Data Sources")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Use Case 1")
    st.write("Official IRAS (Inland Revenue Authority of Singapore) website")
with col2:
    st.subheader("Use Case 2")
    st.write("User-uploaded files")

# Features
st.header("Features")
tab1, tab2 = st.tabs(["Use Case 1: Individual Income Tax Filing Chatbot", "Use Case 2: Custom Document Q&A"])

with tab1:
    st.markdown("""
    - Provides instant answers to tax-related queries
    - Offers step-by-step guidance for filing income tax
    - Explains complex tax concepts in simple terms
    """)

with tab2:
    st.markdown("""
    - Allows users to upload their own files
    - Generates a custom knowledge base from uploaded documents
    - Enables users to ask questions and receive answers based on the content of their uploaded files
    """)

# Conclusion
st.header("Our Vision")
st.write("""
By combining advanced AI technology with user-centered design, we're creating a powerful, 
flexible, and user-friendly system to simplify information retrieval and enhance 
decision-making processes across various domains.
""")