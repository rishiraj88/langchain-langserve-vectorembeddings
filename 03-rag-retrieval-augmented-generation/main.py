from colorama import Fore
from query import query 


def start():
    instructions = (
        """Enter  your query [ENTER]. Type 'x' to go to main menu.\n"""
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("Main Menu")
    print("====")
    print("[1]- Put a query...")
    print("[2]- Exit.")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Enjoy efficient work!")
        exit()
    else:
        print("Please try again.")
        start()


def ask():
    while True:
        user_input = input("Query: ")
        # Exit
        if user_input == "x":
            start()
        else:

            response = query(user_input)

            print(Fore.BLUE + "Response: " + response + Fore.RESET)
            print(Fore.WHITE + 
                  "\n-------------------------------------------------")


if __name__ == "__main__":
    start()
