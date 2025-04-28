
import streamlit as st
import chains
import vectordb

def quiz_generator_app():
    """
    Quiz Generator App with RAG functionality.
    Provides:
    - Quiz generation using RAG (from uploaded documents).
    - RAG file ingestion feature for better context.
    """

    # Sidebar configuration
    st.sidebar.title("Menu")
    section = st.sidebar.radio(
        "Choose a section:",
        ("Quiz Generator RAG", "RAG File Ingestion")
    )

    # Initialize vector database
    vectordatabase = vectordb.initialize_chroma()

    # Quiz generation
    if section == "Quiz Generator RAG":
        st.title("Generate a Quiz with RAG! 🧠")

        with st.form("quiz_generator"):
            topic = st.text_input("Enter a question for the quiz:")
            enable_rag = st.checkbox("Enable RAG")
            submitted = st.form_submit_button("Generate Quiz")

            if submitted:
                if enable_rag:
                    response = chains.generate_quiz_rag_chain(topic, vectordatabase)
                else:
                    response = chains.generate_quiz_chain(topic)

                st.info(response)

    # File ingestion for RAG
    elif section == "RAG File Ingestion":
        st.title("RAG File Ingestion")

        uploaded_file = st.file_uploader("Upload a file for context:", type=["txt", "csv", "docx", "pdf"])

        if uploaded_file is not None:
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)
            st.success(f"File '{uploaded_file.name}' embedded successfully into the vector database!")


quiz_generator_app()