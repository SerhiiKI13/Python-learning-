from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(['Name', 'Age', 'City'])
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
    ["Mike", 27, "Gdansk"],
]
users.sort(key=lambda x: x[2])
print(users)
for row_num, user in enumerate(users, start=2):
    for col_num, cell in enumerate(user,start=1):
        ws.cell(row=row_num, column=col_num).value = cell

ws.freeze_panes = "A2"

ws.auto_filter.ref = ws.calculate_dimension()
wb.save('sorted_by_city.xlsx')