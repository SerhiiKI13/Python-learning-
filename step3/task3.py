try:
    num = int(input("Enter the number: "))
    print(num)
except ValueError:
    print("Invalid number")
else: 
    print("Number accepted")
finally:
    print("Input process finished")