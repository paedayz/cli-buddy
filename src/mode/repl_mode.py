from rich.console import Console
from src.rag.domain.services.chat_service import chat

console = Console()

async def run_repl_mode():
    console.print("[bold cyan]👋 Welcome to Buddy CLI! Type 'exit' or 'quit' to leave.[/]\n")
    while True:
        try:
            prompt = input("user> ").strip()
            if prompt.lower() in {"exit", "quit"}:
                console.print("\n[green]Buddy:👋 Bye![/]")
                break
            if not prompt:
                continue

            with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
                response = await chat(prompt)

            console.print(f"[bold green]Buddy:[/][green] {response}[/]\n")

        except KeyboardInterrupt:
            console.print("\n [green]Buddy:👋 Bye![/]")
            break