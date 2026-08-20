def show_user(name, age, city):
    print(name, age, city)

user = {
    "name": "Alex",
    "age": 30,
    "city": "Bydgoszcz"
}

show_user(**user)