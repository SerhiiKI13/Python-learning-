names = ["Serhii", "Alex", "John", "Mike"]
cities = ["Torun", "Bydgoszcz", "Warszawa", "Gdansk"]

for names,cities in zip(names,cities):
    print(f"{names} lives in {cities}")