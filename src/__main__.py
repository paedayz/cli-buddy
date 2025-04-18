import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

import sys
import asyncio
import speech_recognition as sr
from dotenv import load_dotenv
from src.rag.domain.services.chat_service import chat
from rich.console import Console

console = Console()
recognizer = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:
        console.print("[cyan]🎙 Listening for 'hey buddy'...[/]")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            if "hey buddy" in text:
                return True
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            console.print("[red]Error with the speech recognition service.[/]")
    return False

def listen_for_command():
    with sr.Microphone() as source:
        console.print("[cyan]🎙 Say your command...[/]")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            console.print("[red]Sorry, I didn't catch that.[/]")
        except sr.RequestError:
            console.print("[red]Speech recognition service error.[/]")
    return ""

async def run_voice_repl():
    console.print("[bold cyan]🎧 Voice-activated Buddy CLI. Say 'hey buddy' to start.[/]")
    while True:
        if listen_for_wake_word():
            prompt = listen_for_command()
            console.print(prompt)
            if prompt.lower() in {"exit", "quit"}:
                console.print("\n[green]Buddy:👋 Bye![/]")
                break
            if prompt:
                with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
                    response = await chat(prompt)
                console.print(f"[bold green]Buddy:[/][green] {response}[/]\n")

async def run_repl():
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

def main(user_prompt: str = None):
    load_dotenv()
    user_prompt = user_prompt or " ".join(sys.argv[1:])
    
    if user_prompt == "--voice":
        asyncio.run(run_voice_repl())
    elif not user_prompt:
        asyncio.run(run_repl())
    else:
        with console.status("[bold cyan]Buddy is thinking...[/]", spinner="dots"):
            response = asyncio.run(chat(user_prompt))
        console.print(f"[bold green]Buddy:[/][green] {response}[/]\n")

if __name__ == "__main__":
    main()
