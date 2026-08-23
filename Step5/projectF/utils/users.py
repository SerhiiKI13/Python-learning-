users = [
        {"name": "Serhii", "age": 24, "city": "Torun"},
        {"name": "Alex", "age": 30, "city": "Bydgoszcz"},
        {"name": "John", "age": 18, "city": "Warszawa"},
        {"name": "Mike", "age": 27, "city": "Gdansk"},
        {"name": "Anna", "age": 32, "city": "Torun"},
]

def adult_users(users):
    for u in users:
        if u["age"] >= 25:
                    yield u