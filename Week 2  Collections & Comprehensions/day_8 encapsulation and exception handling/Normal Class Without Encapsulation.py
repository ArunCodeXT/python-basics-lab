class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance  # public attribute

account = Bank("Arun", 1000)
print(account.balance)   # ✅ accessible
account.balance = -5000  # 😱 we can set negative balance
print(account.balance)
