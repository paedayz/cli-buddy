from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from src.rag.infrastructure.history.upstash import get_redis_history
from src.rag.infrastructure.prompts.personal_assistant_prompts import general_asistant_prompt
from src.rag.infrastructure.prompts.chat_history_prompts import general_chat_history_prompt
from src.rag.infrastructure.prompts.humen_message_prompts import general_humen_message_prompt
from src.rag.infrastructure.llms.openai_client import llm

def get_conversation_chain():
    history = get_redis_history(session_id="test")
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        chat_memory=history
    )
    
    # NOTE: sequences of prompt is important to make model have a nice context understanding
    chat_prompt = ChatPromptTemplate.from_messages([
        general_asistant_prompt,
        general_chat_history_prompt,
        general_humen_message_prompt
    ])
    
    return LLMChain(
                llm=llm,
                prompt=chat_prompt,
                memory=memory,
                verbose=True  # ✅ Enables logging of inputs/outputs
            )