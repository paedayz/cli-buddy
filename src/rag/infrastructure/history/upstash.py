import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories.upstash_redis import UpstashRedisChatMessageHistory

load_dotenv()

UPSTASH_REDIS_URL = os.getenv('UPSTASH_REDIS_URL')
UPSTASH_REDIS_TOKEN = os.getenv('UPSTASH_REDIS_TOKEN')

def get_redis_history(session_id: str):
    history = UpstashRedisChatMessageHistory(
        url=UPSTASH_REDIS_URL,
        token=UPSTASH_REDIS_TOKEN,
        ttl=500,
        session_id=session_id
    )
    return history