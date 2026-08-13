age = int(input("Enter your age: "))
bilet = input("Do you have a bilet or not?")
vip = input("Do you have a vip or not?")
status_bilet = bilet == 'yes'
status_vip = vip == 'yes'
status = "Adult" if age >= 18 else "Minor"
if status == "Adult":
    if status_bilet:
        if status_vip:
            print("Vip")
        else:
            print("Normal")
    else:
        print("Доступ запрещён: нет билета")
else:
    print(status)