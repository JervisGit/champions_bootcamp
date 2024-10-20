from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_rag_pipeline(vector_store):
    llm = ChatGroq(temperature=0.5, model_name="mixtral-8x7b-32768")
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    system_prompt = """You are an AI assistant specializing in answering questions based on provided context. 
Always cite your sources when giving information. If you're unsure or the information isn't in the context, say so."""

    
    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        system_prompt=system_prompt
        #return_source_documents=True
    )
    
    return rag_chain