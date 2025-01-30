import os
from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
load_dotenv()
def create_chat_groq():
    """
    Function to intialize chat groq
    
    Returns:
    ChatGroq
    
    """
    api_key = os.getenv("GROQ_API_KEY")  # Retrieve API key from environment
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set. Please set it in the environment variables.")

    
    return  ChatGroq(
    model="mixtral-8x7b-32768",
    api_key=api_key,
    temperature=1,                  
    max_tokens=None,
    timeout=None,
    max_retries=2 
)
def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a Hugging Face embedding model.
    """
    return HuggingFaceEmbeddings(model_name=model_name)