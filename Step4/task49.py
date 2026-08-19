import csv
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
    ["Mike", 27, "Gdansk"]
]
with open("export_users.csv", mode="w", newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])

    for row in users:
        writer.writerow(row)