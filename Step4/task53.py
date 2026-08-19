import csv

with open("users_dirty.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    with open("clean_users.csv","w",newline="",encoding="utf-8") as file:
        fieldnames = ["Name","Age","City"]
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            try:
                age = int(row["Age"])
                if age >= 25:
                    writer.writerow(row)
            except ValueError:
                continue