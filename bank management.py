class BankAccount:
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount ${amount} deposited successfully.")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount should be positive.")
        else:
            self.balance -= amount
            print(f"Amount ${amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")


class Bank:
    def _init_(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print(f"Account created for {account_holder} with Account Number: {account_number}")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None


# Main Program
bank = Bank()

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_num = input("Enter Account Number: ")
        acc_holder = input("Enter Account Holder Name: ")
        bank.create_account(acc_num, acc_holder)

    elif choice == 2:
        acc_num = input("Enter Account Number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

    elif choice == 3:
        acc_num = input("Enter Account Number: ")
        account = bank.get_account(acc_num)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

    elif choice == 4:
        acc_num = input("Enter Account Number: ")
        account = bank.get_account(acc_num)
        if account:
            account.check_balance()

    elif choice == 5:
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
