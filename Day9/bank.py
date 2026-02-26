class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance   # Getter method to access the private balance attribute 

acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)

print("Current Balance:", acc.get_balance()) # Safe acess using getter method