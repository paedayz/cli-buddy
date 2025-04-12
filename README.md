# 📦 Installation Guide for Buddy CLI

Follow these steps to install and run the **Buddy** CLI on your system.

---

### Directory Structure
```bash
cli-buddy/
├── buddy/               ← This is a real Python package (must have __init__.py)
│   ├── __init__.py      ← Can be empty
│   └── __main__.py      ← Has your CLI logic and `main()`
├── setup.py
├── .env
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