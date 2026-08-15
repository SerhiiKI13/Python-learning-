def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older")
    return "access "
        
        
try:
    age = int(input("Enter the number: "))
    print(check_age(age))
except ValueError as error:
    print("Error: ", error)
        