from openpyxl import load_workbook
wb = load_workbook('users3.xlsx')
ws = wb.active

ws.delete_rows(3)
wb.save('users3.xlsx')
