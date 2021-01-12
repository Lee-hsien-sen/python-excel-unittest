# coding:utf-8
import unittest
import os
import sys
from common.test_kdear import test_kdear
from common.excel_html_ok import write_html
import json
from common.api_requests import api_requests
import socket


# 学习装饰器
# 学习logs
# 学习cookie
######可以学习不错的框架，，https://www.cnblogs.com/xaye/p/7744417.html
class test_mock(unittest.TestCase):
    # print(os.path.dirname(os.getcwd()))
    # print(sys.path)
    # 更改path为当前工作目录
    # os.chdir(os
    #
    #
    # .path.dirname(__file__))
    # 更改path为当前工作目录的上一级目录
    # os.chdir(os.path.dirname(os.path.dirname(__file__)))
    def test_all_api(self):
        print(os.path.dirname(os.getcwd()))   #上级目录
        print(os.getcwd())  #当前目录
        # path_case = os.path.dirname(os.getcwd()) + '/excel_case/meilexiang_case.xls'
        # path_case = os.path.join(os.getcwd(), 'meilexiang_case.xls')
        # path_case = os.path.join(os.path.dirname(os.getcwd()),'excel_case', 'meilexiang_case.xls')
        path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'iEng_agent_test.xlsx')
        # path_case = os.path.join(os.path.dirname(__file__), 'excel_case', 'fanliwang_case02.xls')
        # path_case = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_case', 'meilexiang_case.xls')
        print(path_case)
        session = 'ieng_wx_agt'
        row = 2 # 如果self.row小于2时，则按excel中实际数据行数请求接口，，如果self.row大于等于2时，则按传入的self.row的值取数据
        test_kdear0 = test_kdear(path_case,session,row)
        test_kdear0.test_all_api()

    # def test_html_dingding(self):    #test_html_dingding前面加个no就不会跑这段代码了
    def no_test_html_dingding(self):  # test_html_dingding前面加个no就不会跑这段代码了
        #加上生成html的代码
        excel_report_file = "ieng_wx_report.xlsx"
        excel_case_time = "0:00:22.744000"
        html_path, pass_count, fail_count = write_html(excel_report_file, "Sheet1", "Name", "IENG接口测试报告", excel_case_time)
        print(pass_count, fail_count)
        print(html_path)
        # 加上 发钉钉消息的代码

        # 获取本机电脑名
        myname = socket.gethostname()
        # print(myname)
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        print(myaddr)
        dingding_headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        #实际的群
        # dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=fd7bfd3d40008e0fed2c5c875ba8710cd53fbd38edcf7a77e94db0f82172f59f"
        #自己的测试群
        dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=305a3658de4c8d9b5c4450564e71a2d4ed7948a9285360651fe1f18aef5e26be"
        dingding_method = "POST"
        dingding_data = {"msgtype": "link", "link": {"text": "", "title": "IENG测试环境接口监听报告", "picUrl": "", "messageUrl": ""}}
        dingding_data["link"]["text"] = "IENG测试环境接口监听报告：用例总数" + str(pass_count + fail_count) + "条，成功" + str(
            pass_count) + "条，失败" + str(fail_count) + "条。"
        dingding_data["link"]["messageUrl"] = "http://" + myaddr + ":8081/" + html_path
        dingding_data = json.dumps(dingding_data)
        api_dingding = api_requests(dingding_method, dingding_url, dingding_data, dingding_headers)
        api_dingding_r = api_dingding.api_requests()
        try:
            dingding1 = api_dingding_r.json()
            dingding2 = json.dumps(dingding1)  # 将获取返回的json信息转换字符串，再转换为列表，才能直接使用dict，安全一些，因为保证不了接口返回的是不是dict格式【重要】
            print(dingding2)
            dingding3 = json.loads(dingding2)  # 将获取返回的json信息转换字符串，再转换为列表
            print(dingding3)
        except:
            print(u'当前请求，无法直接获取json，或出现无法预料的错误,发送钉钉消息失败')
            if len(api_dingding_r.text) > 0:
                print(api_dingding_r.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
