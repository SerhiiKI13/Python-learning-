from task2 import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        
account = SavingsAccount("Serhii", 1000, 5)
print(account.owner)
print(account.get_balance())
print(account.interest_rate)