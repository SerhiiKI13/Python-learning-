from openpyxl import Workbook
from datetime import datetime
wb = Workbook()
ws = wb.active
ws.append(["Date","Event"])
ws.append([datetime.now(),"Python Course"])
ws["A2"].number_format = "DD.MM.YYYY"
wb.save("date_test.xlsx")