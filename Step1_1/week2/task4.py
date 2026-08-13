age = int(input("enter your age: "))
license = input("Do you have license? ")
has_license = license == "yes"
if age >= 18:

    if has_license:
        print("Drive")
    else:
        print("Not Drive")
else:
    print("You very young")