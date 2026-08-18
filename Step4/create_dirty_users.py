from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(['Name', 'Age','City'])
users = [
    {"name": "Serhii", "age": 24, "city": "Torun"},
    {"name": "", "age": "", "city": ""},
    {"name": "Alex", "age": 25, "city": "Bydgoszcz"},
    {"name": "John", "age": 30, "city": "Warszawa"},
    {"name": "", "age": "", "city": ""},
    {"name": "", "age": 22, "city": "Warszawa"},
    {"name": "Mike", "age": 17, "city": "Torun"},
]

for user in users:
    ws.append([user["name"], user["age"], user["city"]])

wb.save('dirty_users.xlsx')