name = input("Введите ваше имя ")
age = int(input("Enter your age "))
height = float(input("Enter your height "))
weight = float(input("Enter your weight "))
answer = input("You have karnet to the gym ")
discount = answer == 'yes'
height = height / 100

print("Имя: ", name)
print("Age: ", age)
print("Adult: ", age >= 18)
print("Height: ", height, "m")
print("Weight: ", weight)
print("Абонемент: ", discount)
imt = weight / (height**2)
print("ИМТ: ", imt)
print(age >= 18 and discount)