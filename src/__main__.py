import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import os
import sys
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def run_repl(llm):
    print("👋 Welcome to Buddy CLI! Type 'exit' or 'quit' to leave.\n")
    while True:
        try:
            prompt = input("buddy> ").strip()
            if prompt.lower() in {"exit", "quit"}:
                print("👋 Bye!")
                break
            if not prompt:
                continue
            response = llm([HumanMessage(content=prompt)])
            print(f"🤖 Buddy: {response.content}\n")
        except KeyboardInterrupt:
            print("\n👋 Bye!")
            break

def main():
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    user_prompt = " ".join(sys.argv[1:])

    if not user_prompt:
        # No arguments → enter REPL mode
        run_repl(llm)
    else:
        # Run single-shot command
        response = llm([HumanMessage(content=user_prompt)])
        print(f"\n🤖 Buddy: {response.content}")

