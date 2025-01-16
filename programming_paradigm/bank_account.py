class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
         if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
         return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
        return self.balance