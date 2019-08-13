import xlrd
import xlwt
import numpy as np


def transpose(path, sheet_index=0):
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(sheet_index)
    rows = sheet.nrows
    cols = sheet.ncols

    narray = np.ndarray((rows, cols))
    for i in range(rows):
        narray[i] = sheet.row_values(i)

    tran_sheet = narray.T
    # with open ('tran_sheet.xslx','x') as tran:
    # tran.writelines(x for x in tran_sheet)
    x_workbook = xlwt.Workbook()
    sheet1 = x_workbook.add_sheet('transpose')
    for i in range(len(tran_sheet)):
        for j in range(len(tran_sheet[i])):
            sheet1.write(i, j, tran_sheet[i][j])
    x_workbook.save(r"C:\Users\schen\Desktop\tran_sheet.xls")


path = r"D:\我的坚果云\研究性学习\光催化测试结果\光催化测试结果.xlsx"
transpose(path, 1)
