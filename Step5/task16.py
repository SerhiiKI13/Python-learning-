numbers = [5, 12, 3, 20, 8]

result = sorted(numbers,key=lambda x: x % 10)
print(result)

users = [
    {"name": "Serhii", "age": 24},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 18},
    {"name": "Mike", "age": 27}
]

users1 = sorted(users,key=lambda x:x["name"])
print(users1)
users2 = sorted(users,key=lambda x:x["age"],reverse=True)

print(users2)
