import json

with open("user.json","r") as file:
     user = json.load(file)
user["age"] = 24
user["city"] = "Bydgoszcz"

with open("user.json","w",encoding="utf-8") as file:
    json.dump(user,file,ensure_ascii = False,indent = 4)
     