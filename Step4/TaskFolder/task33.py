from openpyxl import load_workbook
wb = load_workbook('users.xlsx')
ws = wb.active

ws.freeze_panes = "A2"
wb.save('users.xlsx')