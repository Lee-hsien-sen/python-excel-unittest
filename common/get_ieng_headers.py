import re
import requests
import json
#
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
#
#获取crm的MEILEDEV，session
def get_ieng_headers(data):
    # 以下数据获取《美乐享公众号》的MELEDEV
    method = 'POST'
    url = 'http://ppe.tope365.com/common-interface/login'
    headers={}
    # headers = {"cookie":"JSESSIONID_COOKIE=1efcbfe8-fe83-4d96-81d8-e5d2e0e14037; readappc=df2b80dc43705d28db9be6f29fe58da3"}
    # headers 必须有以下声明
    headers["Content-Type"] = "application/json; charset=utf-8"
    headers["User-Agent"] = "okhttp/3.10.0"
    # headers[""] =
    # headers[""] =
    # headers[""] =

    # openid = "{'openid':'" +openid + "'}"
    # data_all = {}
    # data = {
    #     "loginName": "sunweimin",
    #     "deviceNumber": "0123456789ABCDEF86938302013923400:92:fa:08:dc:6d",
    #     "appVersion": "3.9.4.181204",
    #     "password": "E10ADC3949BA59ABBE56E057F20F883E",
    #     "deviceName": "alps/full_l805b_f_tpad/l805b_f_tpad:5.1/LMY47D/1476325388:user/test-keys",
    #     "isForce": "0"
    # }
    if data !='':
        # print("取到管家或咨询师登录数据了")
        #IENG必须转成json对象
        data = json.dumps(data)
        print(type(data), data)

    else:
        # print("没有取到管家或咨询师登录数据了")
        # IENG必须转成json对象
        data = json.dumps(data)
        print(type(data), data)
    if data == {} or data =='':
        # headers = {'Content-Type': 'application/json', 'Accept': 'application/json','Authorization':''}
        session = ''
        print(
            "获取ieng的studentID的data为空数据------------------------------------------------------------=========================================================================================")
    else:
        # data = eval(data)  # 字符类型的openid转为dist
        # print(type(data),data)
        student_id, cookie = ieng_session(method, url, data, headers)  # 判断接口方法函数
        # headers = {'Content-Type': 'application/json', 'Accept': 'application/json','Authorization': session}
        # studentID = {"studentID":session}
        # print(studentID)
        JSESSIONID_COOKIE = 'JSESSIONID_COOKIE=' + cookie
        # headers = {'Cookie': session_all}
    return student_id, JSESSIONID_COOKIE


def ieng_session(method, url, data, headers):
    try:
        print("每请求一次testApi接口，则打印一次，不分请求方法-----------------------------------------")
        if method =='POST':
            r = requests.post(url=url,data=data,headers=headers,verify=False,timeout = 1500)
            print(type(r.text), r.text)
        elif method == 'GET':                  #get的data用params来传递#get的data用params来传递#get的data用params来传递#get的data用params来传递
            r = requests.get(url, params=data, headers=headers,timeout = 1500)      #get的data用params来传递#get的data用params来传递#get的data用params来传递
        elif method == 'PUT':
            r = requests.put(url,data=data,headers=headers,timeout = 1500)
        elif method == 'DELETE':
            r = requests.delete(url,timeout = 1500)
        else:
            print("--------------------请求方法"+method+"不支持-----------------")
            r = ''
        headers4 = r.json()
        headers5 = dict(r.headers)
        print(headers5)
        if 'data' in str(headers4):
            a = headers4['data']
            # print(type(a),a)
            if 'studentID' in str(a):
                b = a["studentID"]
                print("获取studentID成功")
                print(b)
            else:
                b = ''
                print('获取studentID失败，返回json中data中未找到ieng的studentID')
        else:
            b = ''
            print('获取失败，返回json中未找到存放data')

        if 'Set-Cookie' in str(headers5):
            a = headers5['Set-Cookie']
            print(type(a),a)
            if 'JSESSIONID_COOKIE=' in a:
                # print("走到这一步")
                b_headers = (re.findall('JSESSIONID_COOKIE=([\w,\-]+);', a))[0]
                # print("走到这二步")
                print("获取JSESSIONID_COOKIE成功")
            else:
                b_headers = ''
                print('获取JSESSIONID_COOKIE失败，返回headers中Set-Cookie中未找到ieng的JSESSIONID_COOKIE')
        else:
            b_headers = ''
            print('获取失败，返回headers中未找到存放saas的PHPSESSID的Set-Cookie')
        print("获取到接口返回的ieng的studentID的值为：   ", b)
        print("获取到接口返回的ieng的headers的值为：   ", b_headers)
        return b,b_headers
    except:
        print(u'接口请求35345失败')
        b=''
        b_headers = ''
        return b,b_headers


if __name__ == "__main__":
    data = {
        "loginName": "sunweimin",
        "deviceNumber": "0123456789ABCDEF86938302013923400:92:fa:08:dc:6d",
        "appVersion": "3.9.4.181204",
        "password": "E10ADC3949BA59ABBE56E057F20F883E",
        "deviceName": "alps/full_l805b_f_tpad/l805b_f_tpad:5.1/LMY47D/1476325388:user/test-keys",
        "isForce": "1"
    }
    ieng_token = get_ieng_headers(data)
    print(ieng_token)