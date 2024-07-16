class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance


account1 = BankAccount("Luna", "021000012", 20000)
account2 = BankAccount("Asuka", "001302933", 32000)
print(account1.name)