## Using OpenAI and LangChain to Build an LLM-powered ChatBot
....

This is an application that uses the OpenAI to generate text, based on user input.

## **Install Python**

A [quick guide to install Python](https://github.com/PackeTsar/Install-Python/blob/master/README.md#install-python-) on popular operating systems

....

## Create a virtual environment

**on /*NIX**:
```
python3 -m venv env
```
**on Windows**:
```
python -m venv env
```

## Activate the virtual environment
**on /*NIX**:
```
source env/bin/activate
```
**on Windows**:
```
.\env\Scripts\activate
```

## Project Setup: Initialization

To initialize this project off repository, follow these steps:

1. Clone this repository on to a target machine. It may well be your local machine.
2. Install the required dependencies, using the following commands:

   ```
   pip install -r requirements.txt
   pip install -U langchain-community
   ip install -U langchain-openai
   ```

3. Additionally, you need to obtain an API key for OpenAI usage and add it to `.env` file.

## Installation: Install dependencies
**on /*NIX**:
```
pip3 install -r requirements.txt
pip3 install -U langchain-community
pip3 install -U langchain-openai
```
**on Windows**:
```
pip install -r requirements.txt
pip install -U langchain-community
pip install -U langchain-openai
```

## [Get your API key for OpenAI](https://platform.openai.com/account/api-keys)

### Set the key as an environment variable
Add your API key to `.env` file.

`export OPENAI_API_KEY='sk-brgHe...AjjgKguu7'`

```
OPENAI_API_KEY=sk-brgHe...AjjgKguu7
```

## Run the script:

**on /*NIX**:
```
python3 main.py
```
**on Windows**:
```
python main.py
```
