class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
        elif amount > self.balance:
            print("Withdrawal amount exceeds account balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

# Example usage
account = Account(1000)  # Initialize an account with $1000 balance
account.deposit(500)     # Deposit $500
account.withdraw(300)    # Withdraw $300
account.withdraw(800)    # Attempt to withdraw $800 (exceeds balance)
print(f"Current balance: ${account.get_balance}")
