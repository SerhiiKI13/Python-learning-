import csv

users = [
        {"name": "Serhii", "age": 24, "city": "Torun"},
                    {"name": "Alex", "age": 25, "city": "Bydgoszcz"}
                                ]
user = {"name": "John", "age": 30, "city": "Warsaw"}

with open("new_users.csv","a",encoding="utf-8",newline="") as file:
    fieldnames = ["name","age","city"]
    writer = csv.DictWriter(file,fieldnames=fieldnames) 
    writer.writerow(user)

