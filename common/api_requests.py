#coding:utf-8
import requests
import urllib3
# import json
# import time

class api_requests(object):
    def __init__(self,method,url,data,headers):
        self.method = method
        self.url = url
        self.data = data
        # self.data = json.dumps(self.data)       ##【该转换已前置】【】【crm】统一将dict参数转化为json，如此，headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'
        self.headers = headers
    def api_requests(self):
        print("每请求一次testApi接口，则打印一次，不分请求方法-----------------------------------------")
        # request的高级操作           https://www.cnblogs.com/lei0213/p/6957508.html #request的高级操作
        urllib3.disable_warnings()
        try:
            # print(type(self.data), self.data)
            if self.method =='POST':
                print(self.headers)
                print(type(self.data),self.data)
                r = requests.post(self.url,data=self.data,headers=self.headers,verify=False,timeout = 1500)
                # r = requests.post(self.url, data=self.data, verify=False)
                # print(type(r.text), r.text)
                return r
            elif self.method == 'GET':                  #get的data用params来传递
                r = requests.get(self.url, params=self.data, headers=self.headers,verify=False,timeout = 1500)
                # print("验证哪里出错了------------------------2-----------------")
                # # print(type(r.text),r.text)
                # # print(type(r.data), r.data)
                # print("验证哪里出错了------------------------1-----------------")
                return r
            elif self.method == 'PUT':
                r = requests.put(self.url,data=self.data,headers=self.headers,verify=False,timeout = 1500)
                # print(type(r.text), r.text)
                return r
            elif self.method == 'DELETE':
                r = requests.delete(self.url,verify=False,timeout = 1500)
                # print(type(r.text), r.text)
                return r
            else:
                print("--------------------请求方法"+self.method+"不支持-----------------")
                r='请求方法不支持，请检查请求方法'
                return r
        except requests:
            print(u'接口请求35345失败',requests)
            r = '接口请求出现异常'
            return r

    # 错误与异常
    # 遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
    # 如果HTTP请求返回了不成功的状态码， Response.raise_for_status()会抛出一个HTTPError异常。
    # 若请求超时，则抛出一个Timeout异常。
    # 若请求超过了设定的最大重定向次数，则会抛出一个TooManyRedirects异常。
    # 所有Requests显式抛出的异常都继承自requests.exceptions.RequestException 。
