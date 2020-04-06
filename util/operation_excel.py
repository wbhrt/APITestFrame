import xlrd,os

class Excel:
    def __init__(self,path=None,sheet_name=None):
        if path:
            self.path = path
            self.sheet_name = sheet_name
        else:
            self.path = ('../dataconfig/case.xls')
            self.sheet_name = 'sheet1'
        self.data = self.get_excel_data()
    #获取Sheet1的全部内容
    def get_excel_data(self):
        data = xlrd.open_workbook(self.path)
        tables = data.sheet_by_name(self.sheet_name)
        return tables

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.row_values(row,col)

    #获取总共的行号
    def get_rows(self):
        return self.data.nrows

if __name__ == '__main__':
    el = Excel()
    print(el.get_rows())