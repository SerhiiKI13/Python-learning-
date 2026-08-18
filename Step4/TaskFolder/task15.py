from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(["Name", "Age", "City"])
ws.append(["Serhii", 24, "Torun"])
ws.append(["Alex", 25, "Bydgoszcz"])
ws.append(["John", 30, "Warszawa"])
wb.save('users2.xlsx')