import json

users = [
        {"name": "Serhii", "age": 24,"city": "Torun"},
            {"name": "Alex", "age": 25,"city": "Bgh"},
                {"name": "John", "age": 30,"city": "hdfb"}
                ]

with open("users.json","w",encoding="utf-8") as file:
    json.dump(users,file,ensure_ascii=False,indent=4)

with open("users.json","r",encoding="utf-8") as file:
    user = json.load(file)
for value in user:
    if value["age"] > 24:
        print(value["name"])