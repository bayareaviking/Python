class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def info(self):
        return f"{self.name} {self.number} {self.balance}"

account1 = BankAccount("Luna", "021000012", 20000)
account2 = BankAccount("Asuka", "001302933", 32000)

print(account2.info())
account2.deposit(20000)
account2.withdraw(100000)
print(account2.info())