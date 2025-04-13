from langchain.prompts import HumanMessagePromptTemplate

_general_humen_message_prompt_template = """{query}
Assistant:
"""

general_humen_message_prompt = HumanMessagePromptTemplate.from_template(template=_general_humen_message_prompt_template)