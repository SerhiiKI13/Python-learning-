class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
          return self.__balance
    def deposit(self, amount):
       if amount > 0:
           self.__balance = self.__balance + amount
       else:
           print("Минимальное пополнение минимум на 1")
    def withdraw(self,amount):
         if amount > 0:
             if self.__balance >= amount:
                 self.__balance = self.__balance - amount
                 print("Вы успешно сняли деньги")   
                 print("Ваш баланс после операции:",self.__balance)
             else:
                 print("Not enough money")
                 print("Ваш баланс:",self.__balance)
         else:
                print("Сумма должна быть больше 0")   
 
account = BankAccount("Serhii", 1000)

account.deposit(500)
account.withdraw(300)

account.withdraw(2000)


