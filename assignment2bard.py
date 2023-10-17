class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print("Debit amount exceeds account balance.")
            return

        self.balance -= amount

    def withdraw(self, amount):
        self.debit(amount)

    def get_balance(self):
        return self.balance

# Example usage:
account = Account("Alice", 100)

# Debit $50
account.debit(50)

# Print the account balance
print(account.get_balance())

# Output:
# 50
