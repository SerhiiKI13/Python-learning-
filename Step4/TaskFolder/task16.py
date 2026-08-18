from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["Name", "Age", "City"])

users = [
    {"name": "Serhii", "age": 24, "city": "Torun"},
    {"name": "Alex", "age": 25, "city": "Bydgoszcz"},
    {"name": "John", "age": 30, "city": "Warszawa"}
]

for user in users:
    ws.append([user["name"], user["age"], user["city"]])


wb.save('users3.xlsx')