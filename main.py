import random
from datetime import date

class BankAccount:
    def __init__(self, account_number, name, age, nic, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.nic = nic
        self.balance = initial_deposit


# generates a random account number with 6 characters
def account_number_generate():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    acc_num = ""
    for i in range(6):
        new_char = random.choice(numbers)
        acc_num += new_char
    return acc_num


# find if account exists
def find_account(all_accounts, acc_num):
    for account in all_accounts:
        if account.account_number == acc_num:
            return account
    return None


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
    accounts_list = []
    while True:
        display_menu()
        user_choice = input("\nEnter a number between 1 to 6: ")
        
        match user_choice:
            case '1':
                name = input("\nEnter your name: ")
                age = input("Enter your age: ")
                nic = input("Enter your NIC number: ")
                initial_deposit = int(input("Enter initial deposit amount: "))
                account_number = account_number_generate()
                account1 = BankAccount(account_number, name, age, nic, initial_deposit)
                accounts_list.append(account1)
                print(f"\nAccount created successfully. Your account number is {account1.account_number}.")
                print("\n---- New Account Details ----")
                print(f"Account number\t\t: {account1.account_number}")
                print(f"Created date\t\t: {date.today()}")
                print(f"Account holder's name\t: {account1.name}")
                print(f"Account holder's age\t: {account1.age}")
                print(f"Account holder's NIC\t: {account1.nic}")
                print(f"Available balance\t: Rs.{account1.balance:.2f}")
                
            
            case '6':
                print("\n\t++ Thank you for banking with E-CORP ++")
                print("\n\t\t++ Have a nice day! ++\n")
                break

            case _:
                print("\nInvalid choice. Please enter a number between 1 to 6.")


# run the program
main()
