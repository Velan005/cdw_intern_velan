

from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
import models
import prompts
import vectordb

def create_chat_groq():
    """
    Function to initialize ChatGroq
    
    Returns:
    ChatGroq
    """
    return ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=1,                  
        max_tokens=None,
        timeout=None,
        max_retries=2  # Avoiding failures  
    )

def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a Hugging Face embedding model.
    """
    return HuggingFaceEmbeddings(model_name=model_name)

#### QUIZ GENERATION WITHOUT RAG ####
def generate_quiz_chain(topic):
    """
    Generate Quiz using basic LLM chain.

    Args:
        topic - Topic for the quiz.

    Returns:
        str - Generated quiz questions.
    """
    llm = models.create_chat_groq()  # Corrected function call

    prompt_template = prompts.quiz_generator_prompt()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic": topic
    })
    return response.content

#### QUIZ GENERATION WITH RAG ####
def generate_quiz_rag_chain(topic, vector):
    """
    Creates a RAG chain for quiz generation with relevant context retrieval.

    Args:
        topic - Topic for quiz generation.
        vectorstore - Instance of vector store.

    Returns:
        str - Generated quiz questions with RAG.
    """
    prompt = prompts.quiz_generator_rag_prompt()

    llm = models.create_chat_groq()  # Corrected function call

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = vectordb.retrieve_from_chroma(topic, vectorstore=vector)

    rag_chain = prompt | llm | StrOutputParser()

    response = rag_chain.invoke({
        "context": format_docs(retriever),
        "topic": topic
    })
    return response