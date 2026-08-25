from task2 import BankAccount
class SavingsAccount(BankAccount):
    def add_interest(self,percent):
      balance1 = self.get_balance() 
      interest = balance1 * (percent / 100)
      interest = balance1 + interest
      print(interest)

account = SavingsAccount("Serhii", 1000)
account.add_interest(10)