from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_rag_pipeline(vector_store):
    llm = ChatGroq(model_name="mixtral-8x7b-32768")
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )
    
    # Create a custom prompt template
    prompt_template = """
    You are an AI assistant answering questions based on the given context. 
    Use the following pieces of context to answer the question at the end. 
    If you don't know the answer or can't find it in the context, just say "I don't know".
    Base your answer solely on the provided context, not on any prior knowledge.
    
    Context: {context}

    Chat History: {chat_history}

    Human: {question}
    AI Assistant: Based on the provided context, here's the answer:
    """
    
    PROMPT = PromptTemplate(
        input_variables=["context", "chat_history", "question"],
        template=prompt_template
    )
    
    # Create a custom QA chain
    qa_chain = load_qa_chain(
        llm,
        chain_type="stuff",
        prompt=PROMPT,
        verbose=True
    )
    
    rag_chain = ConversationalRetrievalChain(
        retriever=retriever,
        memory=memory,
        combine_docs_chain=qa_chain,
        return_source_documents=True
    )
    
    """
    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    """
    
    return rag_chain