import unittest
# from API import method_6
from Text_py.unittest_excel_html import HTMLTestRunner_wangsen, html_excel_py

################以一个类的维度控制测试用例的执行#############
# cases1=unittest.TestLoader().loadTestsFromTestCase(method_5.MyTestCase)
cases2=unittest.TestLoader().loadTestsFromTestCase(html_excel_py.MyTestCase)
mysuite=unittest.TestSuite([cases2])
filename = 'test.html'
#一二进制方式打开文件,准备写
file_object=open(filename,'wb')
#使用HTMLTestRunner配置参数,输出报告路径,报告标题,描述,均可以配置
runner= HTMLTestRunner_wangsen.HTMLTestRunner(
    stream=file_object,
    title='报告主题:接口测试报告',
    description='报告详细描述',

)
#运行测试集合
runner.run(mysuite)