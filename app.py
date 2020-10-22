import pandas as pd

import openpyxl

from openpyxl import Workbook

wbk = openpyxl.Workbook()

wbk.save('hello_world.xlsx')
sht = wbk['Sheet']
sht.title='Hobbit'



# sheet = wbk.active
#
# print(workbook.sheetnames)
#
# sheet["A1"] = "hello"
# sheet["B1"] = "world!"
#
# workbook.save(filename="hello_world.xlsx")

# worksheet = wb['Sheet1']
#
#
#
# for col in ['A', 'B', 'C']:
#     worksheet.column_dimensions[col].hidden= True
