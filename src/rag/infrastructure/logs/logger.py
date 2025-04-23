import os
from rich.console import Console

# Set environment manually for example purposes
# os.environ['ENV'] = 'dev'  # or 'prod'

ENV = os.getenv('ENV', 'dev')  # default to dev
console = Console()

def log(message):
    if ENV != 'prod':
        console.log(message)