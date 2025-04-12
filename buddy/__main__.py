import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import os
import sys
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def main():
    load_dotenv()

    # Grab everything the user types after "buddy"
    user_prompt = " ".join(sys.argv[1:])

    if not user_prompt:
        print("🤖 Buddy says: Please give me something to respond to!")
        sys.exit(1)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    response = llm([HumanMessage(content=user_prompt)])
    print(f"\n🤖 Buddy: {response.content}")
