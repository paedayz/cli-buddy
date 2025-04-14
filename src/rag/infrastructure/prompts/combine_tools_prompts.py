from langchain.prompts import SystemMessagePromptTemplate

def get_general_combine_tools_prompt_template(tools_call_answer: str, query: str) -> str:
    return f"""
This is tools calling answer for user query, use this for information to respond to the user.

query: {query}
answer: {tools_call_answer}
--------------------------------------------------------------------------
\n
"""

def get_general_combine_tools_prompt(tools_call_answer: str, query: str) -> str:
    return SystemMessagePromptTemplate.from_template(get_general_combine_tools_prompt_template(tools_call_answer=tools_call_answer, query=query))