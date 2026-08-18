from openpyxl import load_workbook
wb = load_workbook('sheets_test.xlsx')
ws_users = wb["Users"]
ws_stats = wb["Statistics"]
ws_report = wb["Report"]
ws_users['A1'] = 'Name'
ws_stats['A1'] = 'Total users'
ws_report['A1'] = 'Users Report'
wb.save('sheets_test2.xlsx')