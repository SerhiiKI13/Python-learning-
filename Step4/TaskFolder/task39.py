from openpyxl import load_workbook
wb = load_workbook('sheets_test2.xlsx')
ws_users = wb['Users']
copy = wb.copy_worksheet(ws_users)
copy.title = "Users Backup"
wb.save('sheets_copy_test.xlsx')