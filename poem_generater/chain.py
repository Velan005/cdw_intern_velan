import prompt

from model import create_chat_groq
def poem(topic_str):
    """generate poem
    Args:
        topic str is the poem comment 
    returns:
    response """
    prompt_temp=prompt.poem_generator_prompt_from_hub()

    llm= create_chat_groq()

    chain = prompt_temp| llm
    response = chain.invoke({"question":topic_str})
    return response.content