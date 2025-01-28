from langchain_groq import ChatGroq
def create_chat_groq():
    """ 
    this used to return ChatGroq model
      """
    return ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)