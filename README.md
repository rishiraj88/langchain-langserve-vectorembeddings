## Building LLM-powered apps (using LangChain)
....
- configuring multiple data sources to use with LangChain and LangServe

- This is a Python application to build more applications, fueled up with OpenAI API and LLMs using LangChain.

## **Install Python**

A [Quick Guide for Installing](https://github.com/PackeTsar/Install-Python/blob/master/README.md#install-python-) Python on popular Operating Systems

....

## Create a virtual environment

**on \*NIX**:
```
python3 -m venv env
```
**on Windows**:
```
python -m venv env
```

## Activate the virtual environment
**on \*NIX**:
```
source env/bin/activate
```
**on Windows**:
```
.\env\Scripts\activate
```

## Install the dependencies as follows
**MacOS/Linux**:
`pip3 install -r requirements.txt`
**Windows**:
`pip install -r requirements.txt`

## Obtain your API Key for OpenAI API
[Get an API key](https://platform.openai.com/account/api-keys)

### Set the key as an environment variable
Add your OpenAI 'API key' to `.env` file.

`export OPENAI_API_KEY='sk-brgHe...AjjgKguu7'`

```
OPENAI_API_KEY=sk-brgHe...AjjgKguu7
```

## Run the main Script for project setup

**on \*NIX**:
```
python3 main.py
```
**on Windows**:
```
python main.py