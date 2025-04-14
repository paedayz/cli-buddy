import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import sys
from dotenv import load_dotenv
from src.rag.domain.services.chat_service import chat
from rich.console import Console

console = Console()

def run_repl():
    print("👋 Welcome to Buddy CLI! Type 'exit' or 'quit' to leave.\n")
    while True:
        try:
            prompt = input("user> ").strip()
            if prompt.lower() in {"exit", "quit"}:
                print("\n[green]Buddy:👋 Bye![/]")
                break
            if not prompt:
                continue

            with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
                response = chat(prompt)

            console.print(f"[green]Buddy: {response}[/]\n")

        except KeyboardInterrupt:
            print("\n[green]Buddy:👋 Bye![/]")
            break

def main(user_prompt: str = None):
    load_dotenv()
    
    if not user_prompt:
        user_prompt = " ".join(sys.argv[1:])

    if not user_prompt:
        # No arguments → enter REPL mode
        run_repl()
    else:
        # Run single-shot command
        with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
            response = chat(user_prompt)

        console.print(f"\n[green]Buddy:[/] {response}")

