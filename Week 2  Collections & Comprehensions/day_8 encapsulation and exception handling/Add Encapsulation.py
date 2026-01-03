class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")
    
    def get_balance(self):
        return self.__balance

# Usage
acct = BankAccount("Arun", 1000)
acct.deposit(500)
print(acct.get_balance())  # 1500
