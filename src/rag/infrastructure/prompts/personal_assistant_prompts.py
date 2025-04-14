from langchain.prompts import SystemMessagePromptTemplate

_general_asistant_prompt_template = """
You are AI personal assistant that help user do everything by Windows terminal, Your name is Buddy.
Please use some emoji to make user friendly
--------------------------------------------------------------------------
\n
"""

general_asistant_prompt = SystemMessagePromptTemplate.from_template(template=_general_asistant_prompt_template)