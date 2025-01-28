from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def poem_generator_prompt_from_hub():
    """
    Generates Prompt template from the LangSmith prompt hub
    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    prompt_template = hub.pull("velan")
    return prompt_template