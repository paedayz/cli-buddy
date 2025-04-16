from langchain.chat_models import init_chat_model

from src.rag.domain.services.general_conversation_chain import get_conversation_chain
from src.rag.infrastructure.tools._tool_calling import execute_tool_call
from src.rag.infrastructure.tools.google_work_space_tools import SetCalendar, SendMail
from src.rag.infrastructure.tools.math_tools import Add, Subtract, Multiply, Divide, Prime, Sqrt, Factorial, Fibonacci, Mode, LetterCount

def chat(query: str) -> str:
    
    tools_call_answer = get_answer_from_tools_call(query)
    
    conversation_chain = get_conversation_chain(query=query, tools_call_answer=tools_call_answer)
    
    result = conversation_chain.invoke({
        "query": query,
    })
    
    return result["text"]

def get_answer_from_tools_call(query: str) -> str:
    tools = [
        Add,
        Subtract,
        Multiply,
        Divide,
        Prime,
        Sqrt,
        Factorial,
        Fibonacci,
        Mode,
        LetterCount,
        SetCalendar,
        SendMail
    ]
    
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")
    llm_with_tools = llm.bind_tools(tools)
    tool_calls: list = llm_with_tools.invoke(query).tool_calls
    
    results = [execute_tool_call(call) for call in tool_calls]
    
    if len(results) == 0:
        return ""
    
    return "\n".join(results)