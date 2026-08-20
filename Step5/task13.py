names = ["Serhii", "Alex", "John"]
ages = [24, 30, 18]

users = {}

for name,age in zip(names,ages):
   users[name] = age

print(users)