users = [
    {"name": "Serhii", "age": 24},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 18},
    {"name": "Mike", "age": 27},
]

result = { user['name']: user['age'] for user in users if user['age'] >= 20}
print(result)