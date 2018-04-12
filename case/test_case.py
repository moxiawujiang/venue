__author__ = '芜疆'
#encoding=utf-8
import sys
import os
project_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from util.opera_excel import OperaExcel
from base.base import ActionMethod

class MyTestCase:
    def run_main(self):
        self.action_method=ActionMethod()
        self.handle_excel=OperaExcel()
        case_lines=self.handle_excel.get_lines()
        for i in range(1,case_lines):
            is_run=self.handle_excel.get_cell(i,2)
            if is_run=="yes":
                method=self.handle_excel.get_cell(i,3)
                print(method)
                handle_value=self.handle_excel.get_cell(i,4)
                send_value=self.handle_excel.get_cell(i,5)
                self.run_method(method,handle_value,send_value)

    #python中的反射，通过字符串找class中的方法
    def run_method(self,method,handle_value,send_value):
        action_function=getattr(self.action_method,method)
        action_function(handle_value,send_value)




if __name__ == '__main__':
    test=MyTestCase()
    test.run_main()



