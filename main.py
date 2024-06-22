class BankAccount:
    def __init__(self, account_number, name, age, nic, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.nic = nic
        self.balance = initial_deposit


# displaying main bank controls menu
def display_menu():
    print("\n\nE-CORP BANK MANAGEMENT SYSTEM")
    print("-------------------")
    print("[1] Create a New Account")
    print("[2] Deposit Money")
    print("[3] Withdraw Money")
    print("[4] Check Account Balance")
    print("[5] Transfer Money")
    print("[6] Exit")


# main function
def main():
    display_menu()


# running the program
main()
