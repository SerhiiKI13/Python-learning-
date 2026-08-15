
def mainx():
    expenses =[]

    while True:
       num = int(input("""
              1.Add expense
              2.Show expenses
              3.Show total
              4.Exit
                                          
              Choose:
              """))
       if num == 1:
           name = input("Enter the name: ")
           amount = int(input("Enter the amount: "))
           add_expense(expenses,name,amount)
       elif num == 2:
           print(show_expenses(expenses))
       elif num == 3:
           print(show_total(expenses))
       else:
           print("Работа закончена")
           break
       
        
def add_expense(expensess,name,amount):
      exp = {"name": name,"amount": amount}
      expensess.append(exp)
      return expensess
  
def show_expenses(expenses):
    if len(expenses) >= 1:
        return expenses
    else:
        return "Нету расходов"
    
def show_total(expenses):
    total = 0
    for e in expenses:
        total = total + e['amount'] 
             
    return total           
     
     
#add_expense(expenses,"food",25)  

print(mainx())
    
