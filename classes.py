from datetime import datetime


class Account:
    def __init__(self, account_name, balance=0.0):
        self.account_name = account_name
        self.balance = balance
        self.transactions = []  # Log for transactions

    def log_transaction(self, transaction_type, amount):
        """Helper function to log the transaction with date and time."""
        timestamp = datetime.now()
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "date": timestamp.strftime("%Y-%m-%d"),
            "time": timestamp.strftime("%H:%M:%S"),
            "balance_after": self.balance
        })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction("Deposit", amount)
            print(f"Deposit of {amount} was successful. New balance is {self.balance}")
        else:
            print("Deposit failed. Check amount to complete the transaction.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.log_transaction("Withdrawal", amount)
            print(f"Withdrawal of {amount} was successful. Balance: {self.balance}")
        else:
            print(f"Request declined. Insufficient funds, balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


# SavingsAccount Class (inherits from BankAccount)
class SavingsAccount(Account):
    def __init__(self, account_name, balance=0.0, interest_rate=0.15):
        super().__init__(account_name, balance)
        self.interest_rate = interest_rate  # Set interest rate as a decimal (e.g., 0.12 for 12%)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.log_transaction("Interest", interest)
        print(f"Interest added: {interest}. New balance: {self.balance}")


# CheckingAccount Class (inherits from BankAccount)
class CheckingAccount(Account):
    def __init__(self, account_name, balance=0.0, overdraft_limit=50000):
        super().__init__(account_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            self.log_transaction("Withdrawal", amount)
            print(f"Withdrawal of {amount} was successful. New balance: {self.balance}")
        else:
            print("Withdrawal request denied overdraft limit exceeded or insufficient balance.")


savings = SavingsAccount("Hudson", 30000)
checking = CheckingAccount("Robb", 15000)

savings.deposit(70000)
savings.add_interest()
checking.withdraw(65000)

print("Savings Account Transaction: ")
for transaction in savings.get_transactions():
    print(transaction)

print("\nChecking Account Transaction: ")
for transaction in checking.get_transactions():
    print(transaction)
print("\nchecking balance in the transaction: ")
for transaction in str(checking.get_balance()):
    print(transaction) 