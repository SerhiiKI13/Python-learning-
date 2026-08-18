import csv

with open("big_users.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        age = int(row["age"])
        if age > 18:
            count+=1
    print(count)