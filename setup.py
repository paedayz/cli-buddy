from setuptools import setup, find_packages

setup(
    name="buddy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-community",
        "openai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "buddy=buddy.__main__:main"
        ]
    },
)
