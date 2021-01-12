# coding:utf-8
import unittest
import os
import sys
from common.test_kdear import test_kdear


# 学习装饰器
# 学习logs
# 学习cookie
######可以学习不错的框架，，https://www.cnblogs.com/xaye/p/7744417.html
class test_mock(unittest.TestCase):
    # print(os.path.dirname(os.getcwd()))
    # print(sys.path)
    # 更改path为当前工作目录
    # os.chdir(os.path.dirname(__file__))
    # 更改path为当前工作目录的上一级目录
    # os.chdir(os.path.dirname(os.path.dirname(__file__)))
    def test_all_api(self):
        print(os.path.dirname(os.getcwd()))   #上级目录
        print(os.getcwd())  #当前目录
        # path_case = os.path.dirname(os.getcwd()) + '/excel_case/meilexiang_case.xls'
        # path_case = os.path.join(os.getcwd(), 'meilexiang_case.xls')
        # path_case = os.path.join(os.path.dirname(os.getcwd()),'excel_case', 'meilexiang_case.xls')
        path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'crm_case_crm_importe.xlsx')
        # path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'fanliwang_case02.xls')
        # path_case = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_case', 'meilexiang_case.xls')
        print(path_case)
        session = 'crm_crm_importe'
        row = 3 # 如果self.row小于2时，则按excel中实际数据行数请求接口，，如果self.row大于等于2时，则按传入的self.row的值取数据
        test_kdear0 = test_kdear(path_case,session,row)
        test_kdear0.test_all_api()


if __name__ == '__main__':
    unittest.main(verbosity=2)


# def test_all_api():
#     print(os.path.dirname(os.getcwd()))   #上级目录
#     print(os.getcwd())  #当前目录
#     # path_case = os.path.dirname(os.getcwd()) + '/excel_case/meilexiang_case.xls'
#     # path_case = os.path.join(os.getcwd(), 'meilexiang_case.xls')
#     # path_case = os.path.join(os.path.dirname(os.getcwd()),'excel_case', 'meilexiang_case.xls')
#     path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'crm_case.xlsx')
#     # path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'fanliwang_case02.xls')
#     # path_case = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_case', 'meilexiang_case.xls')
#     print(path_case)
#     session = 'crm'
#     row = 2  # 如果self.row小于2时，则按excel中实际数据行数请求接口，，如果self.row大于等于2时，则按传入的self.row的值取数据
#     test_kdear0 = test_kdear(path_case,session,row)
#     test_kdear0.test_all_api()
#
# test_all_api()
#
