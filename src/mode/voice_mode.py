import speech_recognition as sr
from rich.console import Console
from src.rag.domain.services.chat_service import chat

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

async def run_voice_mode():
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