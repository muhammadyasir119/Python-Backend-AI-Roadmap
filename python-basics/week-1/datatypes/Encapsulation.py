# Week 2 - Day 4 (Encapsulation)

class BankAccount:
    
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)


# Object
acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)

acc.show_balance()

# print(acc.__balance) error (direct access allowed nahi)
