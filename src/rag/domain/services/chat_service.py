from src.rag.domain.services.general_conversation_chain import get_conversation_chain

def chat(query: str) -> str:
    conversation_chain = get_conversation_chain()
    result = conversation_chain.invoke({
        "query": query,
        "chat_history": []
    })
    
    return result["text"]