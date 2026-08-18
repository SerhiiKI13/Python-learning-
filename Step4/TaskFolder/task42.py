from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["Name", "Age", "City"])
ws.freeze_panes = 'A2'


users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
    ["Mike", 27, "Gdansk"],
]

users.sort(key=lambda x: x[0])
print(users)


for row,user in enumerate(users,start=2):
    for col,cell in enumerate(user,start=1):
        ws.cell(row=row,column=col).value = cell

ws.auto_filter.ref = "A1:C5"

wb.save("sorted_by_name.xlsx")
