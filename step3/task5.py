class AgeError(Exception):
        pass

def check_age(age):
    if age < 18:
        raise AgeError("You must be 18 or older")
    return "Access granted" 

try:
    n1 = int(input("Enter your age: ")) 
    print(check_age(n1))
except AgeError as error:
    print(error)
except ValueError:
    print("Invalid number")
