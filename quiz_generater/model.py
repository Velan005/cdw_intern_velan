from langchain_groq import ChatGroq
'''
Function to initialize the ChatGroq 

Returns:
    ChatGroq
'''
def create_groq_llm():
    return ChatGroq(
            model="mixtral-8x7b-32768",
            temperature=1,
            max_tokens=15000,
            timeout=None,
            max_retries=2
    )