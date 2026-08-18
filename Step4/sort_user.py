from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["Name", "Age","City"])
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
]
users.sort(key=lambda x: x[1])
for user in users:
    print(user)
for row,user in enumerate(users,start=2):
    for col,cell in enumerate(user,start=1):
        ws.cell(row=row,column=col).value = cell

wb.save("sorted_users.xlsx")
