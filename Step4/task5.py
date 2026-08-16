import json

user = {
        "name": "Serhii",
            "age": 23,
                "city": "Torun"
                }

with open("user.json","w",encoding="utf-8") as file:
    json.dump(user,file,ensure_ascii=False, indent=4)