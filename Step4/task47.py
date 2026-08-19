import csv

with open("users.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        age = int(row[1])
        if age >= 25:
            print(row)