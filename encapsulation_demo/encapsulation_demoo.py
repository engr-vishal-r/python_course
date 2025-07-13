class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # private variable

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    # Setter method to update balance (with a check)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

# Usage
acc = BankAccount("Ramesh", 1000)

# Direct access to balance is not allowed
# print(acc.__balance)  ❌ This will raise an AttributeError

# Proper access via methods
print("Initial Balance:", acc.get_balance())  # ✅

acc.deposit(500)
print("After Deposit:", acc.get_balance())    # ✅

acc.withdraw(300)
print("After Withdrawal:", acc.get_balance()) # ✅

acc.withdraw(5000)  # ❌ Invalid
