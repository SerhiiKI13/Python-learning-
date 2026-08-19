import csv
users = [
    {"Name": "Serhii", "Age": 24, "City": "Torun"},
    {"Name": "Alex", "Age": 30, "City": "Bydgoszcz"},
    {"Name": "John", "Age": 18, "City": "Warszawa"},
    {"Name": "Mike", "Age": 27, "City": "Gdansk"},
]

with open("export_users_dict.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user)
