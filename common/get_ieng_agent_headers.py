import re
import requests
import json
#
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
#

def get_ieng_wx_agent_headers(data):
    # 以下数据获取《IENG公众号》的MELEDEV
    method = 'POST'
    url = 'https://test.tope365.com/agent/login'
    headers = {}
    # headers = {'content-type': 'application/json'}
    headers["Content-Type"] = "application/json; charset=UTF-8"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
    data = json.dumps(data)
    print(data)
    if data == '':
        # headers["Content-Type"] = "application/json; charset=UTF-8"
        wx_cookie = ""
        print(
            "url_openid为空的数据------------------------------------------------------------=========================================================================================")
    else:
        session = ieng_wx_session(method, url, data, headers)  # 判断接口方法函数
        wx_cookie = 'JSESSIONID_COOKIE=' + session
        print(wx_cookie)
    return wx_cookie


def ieng_wx_session(method, url, data, headers):
    try:
        print("每请求一次getmeiledevsessions接口，则打印一次-----------------------------------------")
        if method =='POST':
            r = requests.post(url,data=data,headers=headers,verify=False,timeout = 1500)
            print(type(r.text), r.text)
        elif method == 'GET':                  #get的data用params来传递#get的data用params来传递#get的data用params来传递#get的data用params来传递
            r = requests.get(url, params=data, headers=headers)      #get的data用params来传递#get的data用params来传递#get的data用params来传递
        elif method == 'PUT':
            r = requests.put(url,data=data,headers=headers)
        elif method == 'DELETE':
            r = requests.delete(url)
        else:
            print("--------------------请求方法"+method+"不支持-----------------")
            r = '接口请求出现异常'
    except:
        print(u'接口请求35345失败')
        r = '接口请求出现异常'
    try:
        headers4 = dict(r.headers)  # 因r.headers返回的不是dict类型，所以dict转化
        print(headers4)
        if 'Set-Cookie' in str(headers4):
            a = headers4['Set-Cookie']
            # print(type(a),a)
            if 'JSESSIONID_COOKIE=' in a:
                b = (re.findall('JSESSIONID_COOKIE=([\w,\-]+);', a))[0]
                print("获取JSESSIONID_COOKIE成功")
            else:
                b=''
                print('获取JSESSIONID_COOKIE失败，返回headers中Set-Cookie中未找到JSESSIONID_COOKIE')
        else:
            b = ''
            print('获取失败，返回headers中未找到存放ieng_wx的Set-Cookie')
        print("获取到接口返回的ieng_wx_cookie的值为：   ", b)
    except:
        b = ''
        print(u'当前请求，无法直接获取返回的header信息，或出现无法预料的错误')
    return b

# url = 'http://meiledev.soyoung.com/v1/user/testlogin'
# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN'}
# # data = {'openid': 'oESYd1cJy0UIVlFVQ8HnXvt4AMw0'}
# data = {'openid': 'oeUP30MdsPv2xwxyqXZnNXWqhlYU'}
#
# method ='GET'
# getMELEDEV = getMELEDEVsession(method, url, data,headers)  # 判断接口方法函数
# MELEDEV = getMELEDEV.getMELEDEVsession()

if __name__ == "__main__":

    data = {"loginName": "ss1", "password": "123456"}
    ieng_token = get_ieng_wx_agent_headers(data)
    print(ieng_token)

