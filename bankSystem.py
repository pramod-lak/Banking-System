import random
from datetime import date

class BankAccount:
    def __init__(self, account_number, name, age, nic, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.nic = nic
        self.balance = initial_deposit

    def deposit(self):
        try:
            while True:
                amount = float(input("Enter deposit amount: "))
                if amount >= 100:
                    self.balance += amount
                    print(f"\nDeposited Rs.{amount:.2f} successfully. Current balance is Rs.{self.balance:.2f}.")
                    break
                elif 0 < amount < 100:
                    print("Deposit amount must be at least Rs.100.00. Please try again.")
                elif amount == 0:
                    print("Deposit amount can't be zero. Please try again.")
                elif amount < 0:
                    print("Deposit amount can't be negative. Please try again.")
        except:
            print("Invalid input. Please enter a deposit valid amount.")
        
    def withdraw(self):
        try:
            while True:
                amount = float(input("Enter withdraw amount: "))
                if amount >= 100:
                    if amount <= self.balance - 1000:
                        self.balance -= amount
                        print(f"\nWithdrew Rs.{amount:.2f} successfully. Remaining balance is Rs.{self.balance:.2f}.")
                        break
                    else:
                        print("Can't proceed with the transaction. Insufficient funds.\nMust leave at least Rs.1000.00 in the account.")
                elif 0 < amount < 100:
                    print("Withdrawal amount must be at least Rs.100.00. Please try again.")
                elif amount == 0:
                    print("Withdrawal amount can't be zero. Please try again.")
                elif amount < 0:
                    print("Withdrawal amount can't be negative. Please try again.")
        except:
            print("Invalid input. Please enter a valid withdrawal amount.")

    def check_balance(self):
        print(f"\nYour current account balance is Rs.{self.balance:.2f}.")

def account_number_generate():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    acc_num = ""
    for i in range(6):
        new_char = random.choice(numbers)
        acc_num += new_char
    return acc_num

def find_account(all_accounts, acc_num):
    for account in all_accounts:
        if account.account_number == acc_num:
            return account
    return None

def display_menu():
    print("\n\nE-CORP BANK MANAGEMENT SYSTEM")
    print("-------------------")
    print("[1] Create a New Account")
    print("[2] Deposit Money")
    print("[3] Withdraw Money")
    print("[4] Check Account Balance")
    print("[5] Transfer Money")
    print("[6] Exit")


# main function of the bank management system
def main():
    accounts_list = []
    while True:
        display_menu()
        choice = input("\nEnter a number between 1 to 6: ")
        
        match choice:
            case '1':
                while True:
                    name = input("\nEnter your name: ")
                    if name:
                        break
                    else:
                        print("Name can't be empty. Please try again.")
                while True:
                    age = input("Enter your age: ")
                    if age:
                        break
                    else:
                        print("Age can't be empty. Please try again.")
                while True:
                    nic = input("Enter your NIC number: ")
                    if nic:
                        break
                    else:
                        print("NIC number can't be empty. Please try again.")
                try:
                    while True:
                        initial_deposit = float(input("Enter initial deposit amount: "))
                        if initial_deposit >= 1000:
                            break
                        elif 0 < initial_deposit < 1000:
                            print("Initial deposit amount must be at least Rs.1000.00. Please try again.")
                        elif initial_deposit == 0:
                            print("Initial deposit amount can't be zero. Please try again.")
                        elif initial_deposit < 0:
                            print("Initial deposit amount can't be negative. Please try again.")
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
                except:
                    print("Invalid input. Please enter a valid initial deposit amount.")
                
            case '2':
                account_number = input("\nEnter account number: ")
                account = find_account(accounts_list, account_number)
                if account:
                    account.deposit()
                else:
                    print("\nAccount not found. Please try again.")

            case '3':
                account_number = input("\nEnter account number: ")
                account = find_account(accounts_list, account_number)
                if account:
                    account.withdraw()
                else:
                    print("\nAccount not found. Please try again.")
            
            case '4':
                account_number = input("\nEnter account number: ")
                account = find_account(accounts_list, account_number)
                if account:
                    account.check_balance()
                else:
                    print("\nAccount not found. Please try again.")

            case '6':
                print("\n\t++ Thank you for banking with E-CORP ++")
                print("\n\t\t++ Have a nice day! ++\n")
                break

            case _:
                print("\nInvalid choice. Please enter a number between 1 to 6.")


# run the program by calling the main function
main()
