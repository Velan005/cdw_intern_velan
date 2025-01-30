
from langchain.vectorstores import Chroma  # Corrected import
import models
import utils


def initialize_chroma(persist_directory="./chroma_db"):
    """
    Initializes and returns a Chroma vector store.

    Args:
        persist_directory (str): Directory to store ChromaDB.

    Returns:
        Chroma: Initialized Chroma vector store.
    """
    hf_embeddings = models.create_hugging_face_embedding_model()
    vectorstore = Chroma(embedding_function=hf_embeddings, persist_directory=persist_directory)
    return vectorstore


def store_pdf_in_chroma(uploaded_file, vectorstore):
    """
    Processes and stores PDF data in the Chroma vector store.

    Args:
        uploaded_file: File for RAG ingestion pipeline.
        vectorstore: Instance of Chroma vector store.

    Returns:
        None
    """
    splits = utils.process_pdf_for_rag(uploaded_file)
    vectorstore.add_documents(splits)


def retrieve_from_chroma(query, vectorstore):
    """
    Retrieves relevant documents from the Chroma vector store.

    Args:
        query (str): Query for document retrieval.
        vectorstore: Chroma vector store instance.

    Returns:
        List: Relevant documents.
    """
    retriever = vectorstore.as_retriever()
    return retriever.get_relevant_documents(query)