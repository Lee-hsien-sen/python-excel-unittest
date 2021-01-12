import unittest
import test_case_crm
from ddt import ddt


# excelPath='D:\PythonPrp\HTMLTestRunner\crm_report.xlsx'
# sheetName='Sheet1'
#
# #创建ParseExcel类的实例对象
# excel=ParseExcel(excelPath,sheetName)

@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.run=test_case_crm.test_mock()

    # 导入excel的数据(如果@ddt.data()括号中传的是一个方法，方法前需要加星号（*）)
    # @data(*excel.getDatasFromSheet())
    def test_something(self):
        # name, method, url, data, assertion, value=tuple(message)
        # print("测试接口为：%s" % name)
        rep = test_case_crm.test_kdear
        print(rep)
        # self.assertEqual(rep[assertion], value, '测试不通过')



if __name__ == '__main__':
    str="adchhaboooabfh"
    list = dict(Counter(str))
    print({key:value for key,value in list.items() if value > 1})
    # unittest.main()
