from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

from src.rag.domain.services.general_conversation_chain import get_conversation_chain
from src.rag.infrastructure.llms.openai_client import llm
from src.rag.infrastructure.logs import logger
from src.rag.infrastructure.tools._tool_calling import execute_tool_call
from src.rag.infrastructure.tools.google_work_space_tools import SetCalendar, SendMail
from src.rag.infrastructure.tools.math_tools import Add, Subtract, Multiply, Divide, Prime, Sqrt, Factorial, Fibonacci, Mode, LetterCount

import warnings

async def chat(query: str) -> str:
    tools_call_answer = await get_answer_from_mcp(query=query)
    conversation_chain = get_conversation_chain(query=query, tools_call_answer=tools_call_answer)
    
    result = conversation_chain.invoke({
        "query": query,
    })
    
    return result["text"]

async def get_answer_from_mcp(query: str) -> str:
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["src/rag/infrastructure/mcp/math_server.py"],
                "transport": "stdio",
            },
            "google_work_space": {
                "command": "python",
                "args": ["src/rag/infrastructure/mcp/google_work_space_server.py"],
                "transport": "stdio",
            },
            "ninjas": {
                "command": "python",                
                "args": ["src/rag/infrastructure/mcp/ninjas_server.py"],
                "transport": "stdio",
            },
            "browser": {
                "command": "python",                
                "args": ["src/rag/infrastructure/mcp/browser_server.py"],
                "transport": "stdio",
            }
        }
    ) as client:
        tools = client.get_tools()
        agent = create_react_agent(llm, tools)
        agent_response = await agent.ainvoke({"messages": query})
        logger.log(f'agent_response: {agent_response}')
        agent_response_messages = agent_response["messages"]
        final_result = agent_response_messages[len(agent_response_messages) - 1].content
        
        return final_result
        
# NOTE: Deprecated
def get_answer_from_tools_call(query: str) -> str:
    warnings.warn("using `get_answer_from_mcp` method instead", DeprecationWarning, stacklevel=2)
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