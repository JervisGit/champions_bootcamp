import streamlit as st
from PIL import Image
from utility import check_password
from dotenv import load_dotenv
import os

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.set_page_config(page_title="Methodology", layout="wide")

st.title("Methodology")
st.caption("🚀 An AI Champions Bootcamp Project")

st.write("""
Our project utilizes a Large Language Model (LLM) with Retrieval-Augmented Generation (RAG) 
to process and retrieve information from the IRAS website and user-uploaded files. This page 
outlines our methodology, including the RAG architecture and the workflow for our two use cases.
""")

# RAG Architecture
st.header("RAG Architecture")
st.write("""
Our RAG architecture forms the backbone of our system, enabling efficient information retrieval 
and generation. Here's an overview of how it works:
""")

# Placeholder for RAG Architecture image
st.image("images/rag_architecture.png", caption="RAG Architecture", width=500)

st.write("""
1. Data Ingestion: We collect data from the IRAS website and user-uploaded files.
2. Text Embedding: The textual data is converted into numerical vectors (embeddings).
3. Vector Store: These embeddings are stored in a vector database for quick and efficient retrieval.
4. Query Processing: When a user asks a question, it's processed and converted into a query vector.
5. Retrieval: The system searches the vector store for relevant information based on the query.
6. Context Integration: Retrieved information is combined with the original query.
7. LLM Generation: The LLM uses the query and retrieved context to generate a comprehensive answer.
""")

# Use Case Flowcharts
st.header("Use Case Flowcharts")

# Use Case 1: Individual Income Tax Filing
st.subheader("Use Case 1: Individual Income Tax Filing")
st.write("""
This flowchart illustrates how our system handles queries related to individual income tax filing:
""")

# Placeholder for Use Case 1 flowchart
st.image("images/usecase_1_flowchart.png", caption="Individual Income Tax Filing Flowchart", width=600)

st.write("""
1. User Input: The user submits a tax-related query.
2. Query Processing: The system processes and embeds the query.
3. IRAS Data Retrieval: Relevant information is retrieved from the IRAS dataset.
4. Context Integration: The query is combined with the retrieved IRAS information.
5. LLM Processing: The LLM generates a response based on the integrated context.
6. User Response: The system provides the user with a detailed answer to their tax query.
""")

# Use Case 2: File Upload Q&A
st.subheader("Use Case 2: File Upload Q&A")
st.write("""
This flowchart demonstrates how our system handles Q&A for user-uploaded documents:
""")

# Placeholder for Use Case 2 flowchart
st.image("images/usecase_2_flowchart.png", caption="File Upload Q&A Flowchart", width=600)

st.write("""
1. Document Upload: The user uploads their document(s).
2. Document Processing: The system processes and embeds the document content.
3. Vector Store Update: Embeddings are stored in the vector database.
4. User Query: The user submits a question about their document(s).
5. Query Processing: The system processes and embeds the query.
6. Custom Data Retrieval: Relevant information is retrieved from the user's document embeddings.
7. Context Integration: The query is combined with the retrieved custom information.
8. LLM Processing: The LLM generates a response based on the integrated context.
9. User Response: The system provides the user with an answer based on their uploaded documents.
""")

st.header("Technology Stack")
st.write("""
Our project leverages several key technologies:

- **LangChain**: For building and managing the LLM application pipeline.
- **Vector Embeddings**: To convert text into numerical representations for efficient retrieval.
- **Vector Database**: For storing and quickly accessing embedded information.
- **Large Language Model**: To generate human-like responses based on retrieved context.
- **Streamlit**: To deploy the application front-end on Community Cloud

This technology stack allows us to create a powerful, flexible system capable of handling 
diverse information retrieval and generation tasks.
""")