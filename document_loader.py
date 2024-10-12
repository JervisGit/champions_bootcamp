import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(directory):
    documents = []
    #for filename in os.listdir(directory):
    #    if filename.endswith('.pdf'):
    #        file_path = os.path.join(directory, filename)
    #        loader = PyPDFLoader(file_path)
    #        documents.extend(loader.load())
    filename = "iit_faq.pdf"
    file_path = os.path.join(directory, filename)
    loader = PyPDFLoader(file_path)
    documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_documents = text_splitter.split_documents(documents)
    
    return split_documents