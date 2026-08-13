age = int(input("Enter your age: "))
answer = input("Do you have license: ")
has_license = answer == "yes"
if age >= 18 and has_license:
    print("Можно водить")
    else:
        print("Нельзя водить")
