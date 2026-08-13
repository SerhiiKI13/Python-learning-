def show_info():
        print("Python is awesome!")

        show_info()
        show_info()
        show_info()


def greet(name):
        print("Hello", name)

        greet("Serhii")
        greet("Alex")
        greet("John")

def show_product(name,price, quantity):
        print("Product:", name)
        print("Price:", price)
        print("Quantity:", quantity)
show_product("btc",32,24)
show_product("eth",45,23)

def add(a,b):
        return a + b
        print(add(10,5))

def multiply(a,b):
        return a * b
        result = multiply(5,4)
        result = result * 10
        print(result)

def check_number(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

result = check_number(5)
print(result)

def greet(name="Guest"):
               return "Hello," + name + "!"

print(greet())
print(greet("Serhii"))