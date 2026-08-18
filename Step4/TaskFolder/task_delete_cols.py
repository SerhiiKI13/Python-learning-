from openpyxl import load_workbook
wb = load_workbook('users3.xlsx')
ws = wb.active

ws.delete_cols(2)
wb.save("delete_cols.xlsx")
