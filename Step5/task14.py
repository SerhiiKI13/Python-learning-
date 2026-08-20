names = ["Serhii", "Alex", "John"]
cities = ["Torun", "Bydgoszcz", "Warszawa"]

for index,(name,city)in enumerate(zip(names,cities),start=1) :
    print(f"{index}. {name} - {city}")