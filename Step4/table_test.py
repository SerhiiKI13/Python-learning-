from openpyxl import Workbook
from openpyxl.worksheet.table import Table,TableStyleInfo
wb = Workbook()
ws = wb.active


style = TableStyleInfo(
    name="TableStyleMedium2",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False,
)
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
    ["Mike", 27, "Gdansk"],
]

ws.append(['Name','Age','City'])

for user in users:
    ws.append([user[0], user[1], user[2]])

table = Table(
    displayName="UsersTable",
    ref= ws.calculate_dimension()
)
ws.add_table(table)
table.tableStyleInfo = style


wb.save("users_table_styled.xlsx")