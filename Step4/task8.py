users = [
        {"name": "Serhii", "age": 24},
            {"name": "Alex"},
                {"name": "John", "age": 30},
                    {"name": "Mike", "age": 17}
                    ]

for user in users:
    u = user.get("age")
    if u and u > 18:
        print(user["name"])