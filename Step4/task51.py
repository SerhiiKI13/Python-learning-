import csv


with open("users.csv", 'r',encoding="utf-8") as file:
    with open("filtered_users.csv", 'w', newline="", encoding="utf-8") as fileW:
        reader = csv.DictReader(file)
        fieldnames = ["Name", "Age", "City"]
        writer = csv.DictWriter(fileW, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            age = int(row["Age"])
            if age >= 25:
                writer.writerow(row)


