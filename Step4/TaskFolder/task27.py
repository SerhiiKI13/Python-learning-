from openpyxl import load_workbook

wb = load_workbook('users.xlsx')
ws = wb.active

ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 10
ws.column_dimensions['C'].width = 20

wb.save('users.xlsx')