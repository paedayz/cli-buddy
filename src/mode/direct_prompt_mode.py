from rich.console import Console
from src.rag.domain.services.chat_service import chat

console = Console()

async def run_direct_prompt_mode(user_prompt: str):
    with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
        response = await chat(user_prompt)
    console.print(f"[bold green]Buddy:[/][green] {response}[/]\n")