from openpyxl import load_workbook
wb = load_workbook("users3.xlsx")
ws = wb.active
ws.freeze_panes = "B2"

wb.save("freeze_b2.xlsx")