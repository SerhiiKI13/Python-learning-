from openpyxl import load_workbook
wb = load_workbook('users.xlsx')
ws = wb.active

ws.auto_filter.ref = "A1:C4"

wb.save('users.xlsx')