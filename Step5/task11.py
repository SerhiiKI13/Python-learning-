names = ["Serhii", "Alex", "John", "Mike"]

for index,name in enumerate(names,start=1):
    print(index,name)

names = ["Serhii", "Alex", "John", "Mike", "Anna"]

for index,name in enumerate(names):
    if index % 2 == 0:
        print(index,name)


names = ["serhii", "alex", "john", "mike"]
for index,name in enumerate(names):
    names[index] = name.capitalize()

print(names)