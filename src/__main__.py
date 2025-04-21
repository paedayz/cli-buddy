from dotenv import load_dotenv
from langchain._api import LangChainDeprecationWarning
from src.mode.direct_prompt_mode import run_direct_prompt_mode
from src.mode.repl_mode import run_repl_mode
from src.mode.voice_mode import run_voice_mode

import asyncio
import sys
import warnings

warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

def main(user_prompt: str = None):
    load_dotenv()
    user_prompt = user_prompt or " ".join(sys.argv[1:])
    
    if user_prompt == "--voice":
        asyncio.run(run_voice_mode())
    elif not user_prompt:
        asyncio.run(run_repl_mode())
    else:
        asyncio.run(run_direct_prompt_mode(user_prompt))

if __name__ == "__main__":
    main()
