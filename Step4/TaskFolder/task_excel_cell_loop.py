from openpyxl import Workbook
wb = Workbook()
ws = wb.active
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 25, "Bydgoszcz"],
    ["John", 30, "Warszawa"]
]
for row_num,user in enumerate(users,start=2):
    for col_num,u in enumerate(user,start=1):
        ws.cell(row=row_num, column=col_num).value = u

wb.save("cell_loop.xlsx")