__author__ = '芜疆'
#encoding=utf-8
import xlrd

class OperaExcel:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path="..\\dataconfig\\venue.xls"
        else:
            self.file_path=file_path
        self.excel=self.get_excel()

    def get_excel(self):
        tables=xlrd.open_workbook(self.file_path)
        return tables
    def get_sheet(self,i=None):
        if i == None:
            i=0
        sheet_data=self.excel.sheets()[i]
        return sheet_data
    def get_lines(self):
        lines=self.get_sheet().nrows
        return lines
    def get_cell(self,row,col):
        data=self.get_sheet().cell(row,col).value
        return data

if __name__ == '__main__':
    book=OperaExcel()
    print(book.get_lines())
    print(book.get_cell(2,3))


