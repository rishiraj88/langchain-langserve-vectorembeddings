from dotenv import load_dotenv
from langchain_openai import OpenAI
from colorama import Fore
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
# to build a chain using LangChain Expression Language (LCEL), `ChatPromptTemplate` helps
chain_prompt_template = ChatPromptTemplate.from_template("Tell me a fact about {topic}?")
llm = OpenAI()
string_output_parser = StrOutputParser()


def generate(text):
    """ generate text based on user input """
    chain = chain_prompt_template | llm | string_output_parser
    return chain.invoke({"Theme is": text})

def start():
    instructions = (
        "Search or query. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Put a query...")
    print("[2]- Exit.")
    choice = input("What is your choice (1 or 2)? ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Enjoy efficient work!")
        exit()
    else:
        print("Please retry.")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = generate(user_input)
            print(Fore.BLUE + f"A: " + response + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()
