
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader  # Corrected import

def process_pdf_for_rag(uploaded_file):
    """
    Processes the uploaded PDF file for RAG (Retrieval-Augmented Generation).

    Args:
        uploaded_file: File-like object (e.g., uploaded via a web app).

    Returns:
        List of text chunks.
    """
    temp_file_path = f"temp_{uploaded_file.name}"  # Temporary file for processing
    try:
        # Save the uploaded file temporarily
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Load the PDF using PyPDFLoader
        loader = PyPDFLoader(temp_file_path)
        docs = loader.load()

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)

        return chunks
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)