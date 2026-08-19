import csv

with open("users.csv", "r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        age = int(row["Age"])
        if age >= 25:
            print(row["Name"])
            print(row["Age"])
            print(row["City"])