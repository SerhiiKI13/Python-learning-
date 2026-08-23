users = [
        {"name": "Serhii", "age": 24},
            {"name": "Alex", "age": 30},
                {"name": "John", "age": 18},
                    {"name": "Mike", "age": 27},
                    ]
def adult_users(users):
    for u in users:
        if u["age"] >= 25:
            yield u
            
for user in adult_users(users):
    print(user)