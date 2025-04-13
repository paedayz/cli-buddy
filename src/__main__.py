import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import sys
from dotenv import load_dotenv
from src.rag.domain.services.chat_service import chat

def run_repl():
    print("👋 Welcome to Buddy CLI! Type 'exit' or 'quit' to leave.\n")
    while True:
        try:
            prompt = input("user> ").strip()
            if prompt.lower() in {"exit", "quit"}:
                print("👋 Bye!")
                break
            if not prompt:
                continue
            
            print(f"buddy: {chat(prompt)}\n")
        except KeyboardInterrupt:
            print("\n👋 Bye!")
            break

def main():
    load_dotenv()
    user_prompt = " ".join(sys.argv[1:])

    if not user_prompt:
        # No arguments → enter REPL mode
        run_repl()
    else:
        # Run single-shot command
        print(f"\nBuddy: {chat(user_prompt)}")

