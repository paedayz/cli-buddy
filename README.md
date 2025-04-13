# 📦 Installation Guide for Buddy CLI

Follow these steps to install and run the **Buddy** CLI on your system.

---

### Directory Structure
```bash
cli-buddy/
│   .env
│   .env_example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   setup.py
│
└───src
    │   __init__.py
    │   __main__.py
    │
    ├───rag
    │   │   __init__.py
    │   │
    │   ├───application
    │   │       
    │   │
    │   ├───domain
    │   │   ├───models
    │   │   │
    │   │   └───services
    │   │       │   
    │   │       │   chat_service.py
    │   │       │   general_conversation_chain.py
    │   │
    │   ├───infrastructure
    │   │   ├───history
    │   │   │   │   upstash.py
    │   │   │
    │   │   ├───llms
    │   │   │   │   openai_client.py
    │   │   │
    │   │   ├───prompts
    │   │   │   │   
    │   │   │   │   chat_history_prompts.py
    │   │   │   │   humen_message_prompts.py
    │   │   │   │   personal_assistant_prompts.py
    │   │   │
    │   │   ├───repositories
    │   │   │       
    │   │   └───vectorstores
    │   │           
    │   ├───interfaces
```
- `buddy/` is the actual Python package. It must contain `__init__.py`.
- `__main__.py` contains the logic that's executed when you run `buddy`.
- `.env` should include:

---

### 1. Install dependencies
```bash
pip install -e .
```
### 2. Add your OpenAI key
Create a .env file in the root directory:
```bash
touch .env
```
Add your API key:
```bash
OPENAI_API_KEY=your-openai-key-here
```
### 3. Run it!
```bash
buddy what can you do?
```