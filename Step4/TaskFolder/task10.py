import csv

with open("users.csv","r",encoding="utf-8") as file:
      users= csv.DictReader(file)
      adult = []
      for u in users:
          unum = int(u["age"])
          if unum >= 18:
              adult.append(u)
with open("adult.csv","w",encoding="utf-8",newline="") as file:
                  fieldnames =["name","age","city"]
                  writer =csv.DictWriter(file,fieldnames=fieldnames)
                  writer.writeheader()
                  writer.writerows(adult)
              
              
              