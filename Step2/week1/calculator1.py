def calculator(num1, operation, num2):
       match operation:
               case "+":
                  return num1 + num2
               case "-":
                  return num1 - num2
               case "*":
                  return num1 * num2
               case "/":
                  if num2 == 0:
                     return "Cannot divide by zero"
                  return num1 / num2
               case _:
                  return "Invalid operator"


while True:
   num1 = int(input("Enter first number: "))
   operation = input("Enter operation: ")
   num2 = int(input("Enter second number: "))

   result = calculator(num1, operation, num2)
   print("Result:", result)

   answer = input("Continue? ")
   if answer == "no":
      break
   