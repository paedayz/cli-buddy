from langchain.prompts import SystemMessagePromptTemplate

_general_chat_history_prompt_template = """
This is chat history between AI and Humen, please focus on context first and chat history before
```
{chat_history}
```
--------------------------------------------------------------------------
\n
"""

general_chat_history_prompt = SystemMessagePromptTemplate.from_template(template=_general_chat_history_prompt_template)