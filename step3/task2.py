def calc(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Cannot divide by zero"

try:
    num1= float(input("Enter first number: "))
    num2= float(input("Enter second number: "))
    print(calc(num1,num2))
except ValueError:
    print("Invalid number")