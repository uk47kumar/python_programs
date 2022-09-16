import xlrd

loc = ("C:\Users\uk47k\Downloads")  # To open Workbook
wb = xlrd.open_workbook(loc)
worksheet = wb.sheet_by_name('Sheet1')  # worksheet = wb.sheet_by_index(0)
i = 1
while (i <= 15):
    sn = worksheet.cell(i, 0)
rn = worksheet.cell(i, 1)
mrks = worksheet.cell(i, 2)
print(" ", int(sn.value), " ", int(rn.value), " ", int(mrks.value))
i = i+1
