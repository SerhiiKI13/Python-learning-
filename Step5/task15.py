from operator import itemgetter

numbers = [15, 3, 27, 8, 12, 1]
result = sorted(numbers, reverse=True)
print(result)
print(numbers)
users = [
    {"name": "Serhii", "age": 24},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 18},
    {"name": "Mike", "age": 27}
]

result = sorted(users, key=itemgetter("age"))
print(result)

def get_age(user):
    return user["age"]

result1 = sorted(users, key=get_age)
print(result1)