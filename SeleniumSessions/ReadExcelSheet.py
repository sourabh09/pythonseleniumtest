import xlrd

workbook = xlrd.open_workbook("testdata.xls")

sheet = workbook.sheet_by_name("Sheet1")

row_number = sheet.nrows
col_number = sheet.ncols

for i in range(1, row_number):
    for j in range(0, col_number):
        print(sheet.cell_value(i,j))





