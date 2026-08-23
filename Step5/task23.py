users = [
    {"name": "Serhii", "age": 24},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 18},
    {"name": "Mike", "age": 27},
    {"name": "Anna", "age": 32},
]

def get_names(users):
    for u in users:
        if u["age"] >= 25:
            yield u["name"]
for user in get_names(users):
    print(user)