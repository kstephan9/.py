import xlrd
import pprint
import os

from DefaultItems import DataFolder, OutputFolder, Raw_2Folder

filename = 'SurveyTest_000.xlsx'

pnf = os.path.join(Raw_2Folder, filename)

wb = xlrd.open_workbook(pnf)

sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

### print row 1, all column values
print("sheet1.row_values(0): ", sheet1.row_values(0))
print("sheet2.row_values(1): ", sheet2.row_values(0))

headings = sheet2.row_values(0)
columnCHeading = headings[2]
print(columnCHeading)

i = 0
for row in range(sheet2.nrows):
    i = i + 1
    if str(sheet2.cell(row, 1).value) == "AINST0024815":
        print(i, "was AINST0024815")
    else:
        pass
#    print(i, value_tuple[1].value)



