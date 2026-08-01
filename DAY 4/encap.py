class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

    def getbalance(self):
        print("Current Balance:", self.__balance)

acc = BankAccount(1000)

acc.deposit(500)
acc.getbalance()