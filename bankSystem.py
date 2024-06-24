import random
from datetime import date

#BankAccount class to create bank account objects
class BankAccount:
    def __init__(self, account_number, name, age, nic, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.nic = nic
        self.balance = initial_deposit

    #Deposit method to deposit money to the account
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
        
    #Withdraw method to withdraw money from the account
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

    #Check balance method to check the account balance
    def check_balance(self):
        print(f"\nYour current account balance is Rs.{self.balance:.2f}.")

    #Transfer method to transfer money to another account
    def transfer(self, to_account):
        try:
            while True:
                amount = float(input("Enter transfer amount: "))
                if amount >= 100:
                    if amount <= self.balance - 1000:
                        self.balance -= amount
                        to_account.balance += amount
                        print(f"\nTransfer Rs.{amount:.2f} successfully. Remaining balance is Rs.{self.balance:.2f}.")
                        break
                    else:
                        print("\nCan't proceed with the transaction. Insufficient funds.\nMust leave at least Rs.1000.00 in the account.")
                elif 0 < amount < 100:
                    print("Transfer amount must be at least Rs.100.00. Please try again.")
                elif amount == 0:
                    print("Transfer amount can't be zero. Please try again.")
                elif amount < 0:
                    print("Transfer amount can't be negative. Please try again.")
        except:
            print("Invalid input. Please enter a valid transfer amount.")

#Function to create a new account
def new_account_create():
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

#Function to generate a random account number
def account_number_generate():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    acc_num = ""
    for i in range(6):
        new_char = random.choice(numbers)
        acc_num += new_char
    return acc_num

#Function to find an account by account number
def find_account(all_accounts, acc_num):
    for account in all_accounts:
        if account.account_number == acc_num:
            return account
    return None

#Function to display the main menu
def display_menu():
    print("\n\nE-CORP BANK MANAGEMENT SYSTEM")
    print("-------------------")
    print("[1] Create a New Account")
    print("[2] Deposit Money")
    print("[3] Withdraw Money")
    print("[4] Check Account Balance")
    print("[5] Transfer Money")
    print("[6] Exit")

#Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("\nEnter a number between 1 to 6: ")
        
        match choice:
            case '1':
                new_account_create()
                
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

            case '5':
                from_account_number = input("\nEnter your account number: ")
                from_account = find_account(accounts_list, from_account_number)
                if not from_account:
                    print("\nAccount not found. Please try again.")
                else:
                    to_account_number = input("Enter recipient's account number: ")
                    to_account = find_account(accounts_list, to_account_number)
                    if not to_account:
                        print("\nRecipient's account not found. Please try again.")
                    else:
                        from_account.transfer(to_account)

            case '6':
                print("\n\t++ Thank you for banking with E-CORP ++")
                print("\n\t\t++ Have a nice day! ++\n")
                break

            case _:
                print("\nInvalid choice. Please enter a number between 1 to 6.")

#List to store all the bank accounts
accounts_list = []

#Run the main function
main()
