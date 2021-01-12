# coding:utf-8
# import openpyxl
import json
# from common.data_driver_openpyxl import readexcel
from common.data_driver import readexcel
from common.api_requests import api_requests
from common.get_ieng_family_pro_headers import get_ieng_family_pro_headers
from common.get_ieng_teacher_pro_headers import get_ieng_teacher_pro_headers
from common.get_ieng_agent_pro_headers import get_ieng_agent_pro_headers
from common.get_re_dict import get_dict_value
from common.get_re_dict import get_list_tuple_value2
from common.get_re_dict import get_re_list
import re
import ast
from common.db_test import db_test
from common.db_dict_test import db_dict_test
from common.list_compare_all import list_compare_all
import os
# from common.getmeiledevheaders import getmeiledevheaders
# from common.getweizhuanchangheaders import getweizhuanchangheaders
# from common.get_xiaochengxu_headers import get_xiaochengxu_headers
# from common.getsaasheaders import getsaasheaders
# from common.get_crm_headers import get_crm_headers
from common.get_ieng_headers_line import get_ieng_headers
# from common.get_app_token_sign import get_app_token
# from common.get_app_token_sign import get_app_sign
# from common.data_to_md5 import get_data_sign_md5
from common.parameter_to_dict import parameter_to_dict
# 那么如何来控制警告错误的输出呢？很简单
import warnings
import urllib3
import logging
warnings.filterwarnings("ignore")
urllib3.disable_warnings()
logging.captureWarnings(True)
# 学习装饰器
# 学习logs
# 学习cookie
######可以学习不错的框架，，https://www.cnblogs.com/xaye/p/7744417.html
class test_kdear():
    """author: kdear"""
    def __init__(self,path_case,session,row):
        self.path_case = path_case
        self.session = session
        self.row = row
    # def config(self):
    #     aaa = configparser.ConfigParser()
    #     cf1 = readConfig(r'D:\PythonPrp\python+excel+unittest\config\config.ini')  # 读取文件
    #     cf1.readConfigr

    def test_all_api(self):
        # self.path_case = os.path.dirname(os.getcwd()) + '\excel_case\caseall01_ALL.xls'
        print(self.path_case)
        excel = readexcel(self.path_case,self.row)  # 调用caseall01文件，全部整合用例
        data = excel.getdata()
        datatype = excel.getdatatype()
        url_openid = excel.getopenid()
        # getbeforedata =excel.getbeforedata()
        getbeforesql = excel.getbeforesql()
        getresql = excel.getresql()
        url_config = excel.config()
        url = excel.geturl()
        method = excel.getmethod()
        # print(method[0])
        # statuscode = excel.getstatuscode()
        getrejson = excel.getrejson()
        if self.row >= 2:
            self.row = self.row  # # # # # #如果self.row大于等于2时，则按传入的self.row的值取数据
            self.m = self.row-1
        elif self.row == 1:
            self.row = excel.getrows()# 如果self.row小于2时，则按excel中实际数据行数请求接口
            self.m = 1
        result = []  #用来存放验证结果
        responsevalue = []  #用来存放返回的数据
        jsonresult = []  #用来存放返回的josn校验判断结果
        false_why = []
        for i in range(self.m, self.row):
            # # 先执行excel中的前置Sql,执行Sql后再继续请求接口# # 获取excel中的前置Sql,执行SQL后再继续请求接口# # 获取excel中的前置Sql,执行Sql后再继续请求接口
            print("共有%d个url，当前第%d个执行开始" % (self.row - 1, i))
            print("============================================")
            print("@@@@@@@@打印先执行前置Sql@@@@@@@@")
            #字段去空格---延后
            getbeforesql_i = getbeforesql[i]
            getresql_i = getresql[i]
            print(getbeforesql_i)
            print(getresql_i)
            url_openid_i = url_openid[i]
            url_i = url[i]
            url_i = url_i.strip()

            #通过配置文件的前置域名拼接URL
            re0 = re.compile(r"http(.*)")
            search1 = re0.search(url_i)
            if search1:
                url_i = url_i
            else:
                url_i= url_config + url_i

            datatype_i = datatype[i]  # DataType为1时，接口请求时，必须转换为json对象，即string类型
            data_backup = data[i]  # 备份此时的data[i]，备后面微专场使用
            data_i = data_backup
            data_tmp = ''  # 暂时存放sql获取的id，封装为data
            if getbeforesql_i != '':
                db_before = db_test(getbeforesql_i)
                # db_before = db_dict_test(getbeforesql_i)
                db_before_list = db_before.get_db_item()
                print("@@@@@@@@db_before_list@@@@@@@@")
                print(db_before_list, type(db_before_list))
                print("查询id的长度：", len(db_before_list))
                if db_before_list == ['Sql连接失败']:
                    print(u'当前Sql连接失败，请检查Sql服务器或网络')
                    print(u'跳过当前case，继续下一个case')
                    result.append("FAIL")
                    jsonresult.append("FAIL")
                    responsevalue.append("Sql连接失败")
                    false_why.append("Sql连接失败")
                    continue
                elif db_before_list == [' ']:
                    print("前置Sql执行成功")
                elif len(db_before_list) != 0:
                    data_tmp = db_before_list[0]  # 因为请求地址中必须包含?id=755，所以根据data中@beforedata}，与Sql查询的id值进行拼接url
                    print("前置Sql执行成功，封装Sql获取的值", data_tmp, type(data_tmp))
                else:
                    print("前置Sql执行失败")
                    print(u'跳过当前case，继续下一个case')
                    result.append("FAIL")
                    jsonresult.append("FAIL")
                    responsevalue.append("前置Sql执行失败")
                    false_why.append("前置Sql执行失败")
                    continue
            else:
                print("无前置Sql，无需执行")  # 无前置SQL
            print(url_i)


            # 判断data中是否有变量，需要从beforesql中获取
            # 2018-11-20新增的url兼容参数，与data中的参数合并，以url中的参数为准-----【暂且关闭url_beforesql】
            # if ('&url_beforesql' in str(getbeforedata[i])) or ('&URL_BEFORESQL'in str(getbeforedata[i])):
            #     url[i] = url[i] + data_tmp  # 因为请求地址中id的值755是随时变化的，与Sql查询的id值进行实时拼接url【目前只支持1个变量拼接】
            #     print("111111111111111")
            # else:
            #     print("222222222222")
            #

            # 判断data中是否有变量，需要从beforesql中获取

            print("data的原始类型和值")
            print(type(data_i), data_i)
            if len(data_i) == 0:  # 将data字段为空时重定向为{}，【】【】【解决思路不错】【】,,可以容错
                data_i = {}  #改为dict
            elif '&data_beforesql' in str(data_i):
                print(type(data_i),data_i)
                data_i = eval(data_i.encode('utf-8'))
                for k, v in data_i.items():
                    if "&data_beforesql" == v:
                        data_i[k] = data_tmp
                print("data中的变量经前置sql赋值33333333333333000000")
            elif '&DATA_BEFORESQL' in str(data_i):
                data_i = eval(data_i.encode('utf-8'))
                for k, v in data_i.items():
                    if "&DATA_BEFORESQL" == v:
                        print(data_tmp,type(data_tmp))
                        data_i[k] = data_tmp
                print("data中的变量经前置sql赋值33333333333333111111")
            else:
                data_i = eval(data_i.encode('utf-8'))
                print(data_i, type(data_i))
                print("data中无变量无需前置sql赋值4444444444444444")


            #2018-11-20新增的url兼容参数，与data中的参数合并，以url中的参数为准
            print(url_i)
            # if "access_token" not in url_i:   #过滤URL中"access_token"的参数，不放到data中
            if "?" in url_i:
                url_parameter = parameter_to_dict(url_i)
                print(type(url_parameter),url_parameter)
                for ii in url_parameter.keys():
                    data_i[ii] = url_parameter[ii]
                url_i = url_i.split("?",1)[0]
            print(url_i)
            print(data_i)
            getrejson_i = getrejson[i]  # 读取excel中数据，str转换成dict字典格式
            if len(getrejson_i) == 0:  # 将正则表达式字段为空的正则表达式重定向为{}，【】【】【解决思路不错】【】,,可以容错
                getrejson_i = dict()
            else:
                getrejson_i = ast.literal_eval(getrejson_i)  # ast.literal_eval  方法比  eval  安全
            test01 = list(getrejson_i.keys())  # 取出需要校验的getReJson[i]中的key数组
            # if self.session =='fanliwang':
            #     print(type(data_i),data_i)
            #     data_i=get_data_sign_md5(data_i)
            #     print(type(data_i), data_i)
            #     print(type(data_i), data_i)
            #     headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            #     print("正常获取MD5加密后的data")
            # el
            if len(url_openid_i) == 0:
                url_openid_i = '{}'

            if self.session =='ieng':
                print(url_openid_i,type(url_openid_i))
                try:
                    url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                except:
                    print("url_openid_i无法转化成dict字典"+type(url_openid_i))
                headers = {}
                headers["Content-Type"] = "application/json; charset=utf-8"
                headers["User-Agent"] = "okhttp/3.10.0"
                data_studentID,cookie = get_ieng_headers(url_openid_i)
                data_i["studentID"] = data_studentID
                headers["Cookie"] = cookie
                if datatype_i == 1 or datatype_i == "1":  # datatype_i为1时，接口请求时，必须转换为json对象，即string类型
                    data_i = json.dumps(data_i)       #自强的客户接口datatype_i必须是json对象（dict），其他人的必须是json字符串 #【通用办法】headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'

            elif self.session == 'ieng_wx':
                print(url_openid_i, type(url_openid_i))
                try:
                    url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                except:
                    print("url_openid_i无法转化成dict字典" + type(url_openid_i))
                headers = {}
                headers["Content-Type"] = "application/json; charset=UTF-8"
                wx_cookie = get_ieng_family_pro_headers(url_openid_i)
                headers["Cookie"] = wx_cookie
                if datatype_i == 1 or datatype_i == "1":  # datatype_i为1时，接口请求时，必须转换为json对象，即string类型
                    data_i = json.dumps(
                        data_i)  # 自强的客户接口datatype_i必须是json对象（dict），其他人的必须是json字符串 #【通用办法】headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'

            elif self.session == 'ieng_wx_tch':
                print(url_openid_i, type(url_openid_i))
                try:
                    url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                except:
                    print("url_openid_i无法转化成dict字典" + type(url_openid_i))
                headers = {}
                headers["Content-Type"] = "application/json; charset=UTF-8"
                wx_cookie = get_ieng_teacher_pro_headers(url_openid_i)
                headers["Cookie"] = wx_cookie
                if datatype_i == 1 or datatype_i == "1":  # datatype_i为1时，接口请求时，必须转换为json对象，即string类型
                    data_i = json.dumps(
                        data_i)  # 自强的客户接口datatype_i必须是json对象（dict），其他人的必须是json字符串 #【通用办法】headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'

            elif self.session == 'ieng_wx_agt':
                print(url_openid_i, type(url_openid_i))
                try:
                    url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                except:
                    print("url_openid_i无法转化成dict字典" + type(url_openid_i))
                headers = {}
                headers["Content-Type"] = "application/json; charset=UTF-8"
                wx_cookie = get_ieng_agent_pro_headers(url_openid_i)
                headers["Cookie"] = wx_cookie
                if datatype_i == 1 or datatype_i == "1":  # datatype_i为1时，接口请求时，必须转换为json对象，即string类型
                    data_i = json.dumps(
                        data_i)  # 自强的客户接口datatype_i必须是json对象（dict），其他人的必须是json字符串 #【通用办法】headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'


            elif self.session =='crm':
                print(url_openid_i,type(url_openid_i))
                try:
                    url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                except:
                    print("url_openid_i无法转化成dict字典"+type(url_openid_i))
                headers = get_crm_headers(url_openid_i)
                if datatype_i == 1 or datatype_i == "1":  # datatype_i为1时，接口请求时，必须转换为json对象，即string类型
                    data_i = json.dumps(data_i)       #自强的客户接口datatype_i必须是json对象（dict），其他人的必须是json字符串 #【通用办法】headers中必须声明'Content-Type': 'application/json', 'Accept': 'application/json'
            elif self.session == 'soyoung_app':
                print(url_openid_i, type(url_openid_i))
                url_openid_i = eval(url_openid_i)  # 先将url_openid_i登录数据处理为dict类型
                print(url_openid_i, type(url_openid_i))
                app_session1, app_session2 = get_app_token(url_openid_i)
                data_i["xy_token"] = app_session1  #再获取token
                data_i["uid"] = app_session2  # 再获取uid
                data_i = get_app_sign(data_i)  # 再获取签名
                headers = {}
            # elif self.session =='meiledev':
            #     print(type(data_i),data_i)
            #     headers = getmeiledevheaders(url_openid_i)
            # elif self.session =='weizhuanchang':
            #     print(u'微专场的data中变量更新后')
            #     print(type(data_i), data_i)
            #     print("微专场的data，data变量更新后，dump后")
            #     data_i=json.dumps(data_i)
            #     print(type(data_i), data_i)
            #     headers = getweizhuanchangheaders(url_openid_i)
            elif self.session =='xiaochengxu':
                print(u'微专场的data中变量更新后')
                print(type(data_i), data_i)
                print("微专场的data，data变量更新后，dump后")
                data_i=json.dumps(data_i)
                print(type(data_i), data_i)
                headers = get_xiaochengxu_headers(url_openid_i)
            elif self.session =='saas':
                print(type(data_i), data_i)
                headers = getsaasheaders(url_openid_i)
            else:
                headers ={}
            api = api_requests(method[i], url_i, data_i, headers)  # 判断接口方法函数
            api_r = api.api_requests()  # 这样可以省得调用两次request#这样可以省得调用两次request#这样可以省得调用两次request
            try:
                apijson = api_r.json()
            except:
                print(u'当前请求，无法直接获取json，或出现无法预料的错误')
                # if len(api_r.text)>0:
                #     print(api_r.text)
                print(u'跳过当前case，继续下一个case')
                result.append("FAIL")
                jsonresult.append("FAIL")
                # print(api_r.text)

                if isinstance(api_r, str):
                    if len(api_r) ==0 :
                        responsevalue.append("接口返回为空")
                    else:
                        responsevalue.append(api_r)
                else:
                    responsevalue.append(str(api_r))
                # responsevalue.append("接口请求无法直接获取json，或出现无法预料的错误")
                false_why.append("接口请求无法直接获取json，或出现无法预料的错误")
                continue
            # print('接口返回的json格式缩进展示：')
            # print(json.dumps(apijson,ensure_ascii=False, indent=4)) # indent是缩进的意思，数字4是缩进的程度，ensure_ascii默认为true，会将非ASCII码字符显示为\uXXXX序列
            apijson2 = json.dumps(apijson)  # 将获取返回的json信息转换字符串，再转换为列表，才能直接使用dict，安全一些，因为保证不了接口返回的是不是dict格式【重要】
            print(apijson2)
            jsondata = json.loads(apijson2)  # 将获取返回的json信息转换字符串，再转换为列表
            print(jsondata)
            # 校验正则#校验正则#校验正则#校验正则#校验正则#校验正则#校验正则#校验正则#校验正则#校验正则
            stra = str(apijson)  # 将json转换为字符串，使用in方法判断是否有该字段，str化，取apijson、apijson2、data都可以
            temp = True
            temp2=''
            if len(getresql_i) !=0:
                print("@@@@@@@@打印获取数据库中的SQL中各个key列表@@@@@@@@")
                print(getresql_i)
                print("@@@@@@@@打印获取数据库中的SQL语句@@@@@@@@"+getresql_i)
                db_order_id = db_dict_test(getresql_i)
                db_order_id_list = db_order_id.get_db_item()
                print("@@@@@@@@SQL中各个key@@@@@@@@")
                print(db_order_id_list, type(db_order_id_list))
                if len(test01) == 0:  #主要为了看【无正则表达式】时的RESQL查询的key与请求结果比对问题
                    print(
                        "@@@@@@@@取ReSql有数据，正则表达式无数据@@@@@@@@")
                    if len(db_order_id_list)==0:
                        print("sql语句查询结果为空")
                    else:
                        for each in db_order_id_list:
                            for each1 in each :
                                tmp_list01 = []  # 暂时用于传参，有时间优化下
                                tmp_list02 = []  # 暂时用于传参，有时间优化下
                                print('我的全参数1的SQL校验key结果：    ' + each1)

                                #获取json中的key对应的所有value
                                tmp_list1 = get_dict_value(each1, jsondata, tmp_list01)
                                #如果返回的json中有key的velue是一个数组，且该数组中的元素不是字典类型，需要做下处理
                                #先判断tmp_list1是【只有一个元素】，再判断tmp_list1[0]为数组类型，如果是数组，则只取tmp_list1[0]赋给tmp_list1
                                if len(tmp_list1)==1 and isinstance(tmp_list1[0], list):
                                    tmp_list1=tmp_list1[0]
                                    print('我的json查询1的key列表：    ' + each1+"，该key的value是个纯数组类型，即非标准的字典键值对，已做处理")
                                print('我的json查询1的key列表：    ' + each1)
                                print(tmp_list1, type(tmp_list1))

                                tmp_list2 = get_list_tuple_value2(each1, db_order_id_list, tmp_list02)
                                print('我的SQL查询1的key列表：    ' + each1)
                                print(tmp_list2, type(tmp_list2))
                                if list_compare_all(tmp_list2, tmp_list1):      #数组序列按有序匹配
                                    print("通过sql查询1的key " + each1 + " 序列与接口返回的key " + each1 + " 序列【一致】")
                                else:
                                    print("通过sql查询1的key " + each1 + " 序列与接口返回的key " + each1 + " 序列【不一致】")  # 接口有可能返回的是第几页的
                                    temp = False
                                    temp2 ="通过sql查询1的key " + each1 + " 序列与接口返回的key " + each1 + " 序列【不一致】"
                                    break
                            if temp == False:
                                break
                else:
                    if len(db_order_id_list)==0:
                        print("sql语句查询结果为空，则无法继续校验，用例执行校验结果为：失败")
                        temp = False
                    elif "Sql连接失败" in str(db_order_id_list):
                        print("Sql连接失败，则无法继续校验，用例执行校验结果为：失败")
                        temp = False
                    else:
                        each000=db_order_id_list[0]        #需要修改按数组取
                        print("sql查询回的数组序列，的每一个元素，打印查验下类型")
                        # print(each000,type(each000))
                        for each in each000.keys():
                            print(each, type(each))
                            tmp_list01 = []  # 暂时用于传参，有时间优化下
                            tmp_list02 = []  # 暂时用于传参，有时间优化下
                            tmp_list00 = []  # 暂时用于传参，有时间优化下
                            tmp_list = get_dict_value(each, jsondata, tmp_list00)  # 调用字典取key的所有值函数
                            print("当前的校验的 " + each + " 在SQL查询到的各个key中")
                            print("正则字符串中有key " + each + " ，打印返回语句中的 " + each + " 的所有value列表： ")
                            print(tmp_list, type(tmp_list))
                            print('我的全参数2的SQL校验key结果：    ' + each)
                            # 获取json中的key对应的所有value
                            tmp_list1 = get_dict_value(each, jsondata, tmp_list01)
                            # 如果返回的json中有key的velue是一个数组，且该数组中的元素不是字典类型，需要做下处理
                            # 先判断tmp_list1是【只有一个元素】，再判断tmp_list1[0]为数组类型，如果是数组，则只取tmp_list1[0]赋给tmp_list1
                            if len(tmp_list1) == 1 and isinstance(tmp_list1[0], list):
                                tmp_list1 = tmp_list1[0]
                                print('我的json查询1的key列表：    ' + each + "，该key的value是个纯数组类型，即非标准的字典键值对，已做处理")
                            print('我的json查询到2的key列表：    ' + each)
                            print(tmp_list1, type(tmp_list1))
                            print(type(db_order_id_list))
                            tmp_list2 = get_list_tuple_value2(each, db_order_id_list, tmp_list02)
                            print('我的SQL查询2的key列表：    ' + each)
                            print(type(tmp_list2))
                            print(tmp_list2, type(tmp_list2))
                            if list_compare_all(tmp_list2, tmp_list1):  # 数组序列按有序匹配
                                print("通过sql查询2的key " + each + " 序列与接口返回的key " + each + " 序列【一致】")
                            else:
                                print(
                                    "通过sql查询2的key " + each + " 序列与接口返回的key " + each + " 序列【不一致】")  # 接口有可能返回的是第几页的
                                temp = False
                                temp2 = "通过sql查询2的key " + each + " 序列与接口返回的key " + each + " 序列【不一致】"
                                break
                    if temp != False:   #SQL精确查询校验后，再校验正则
                        for each in test01:
                            tmp_list00 = []  # 暂时用于传参，有时间优化下
                            tmp_list = get_dict_value(each, jsondata, tmp_list00)  # 调用字典取key的所有值函数
                            if each in stra:  # 将json转换为字符串，使用in方法判断是否有该字段
                                if each in str(db_order_id_list):
                                    print("当前的校验的 " + each + " 在SQL查询到的各个key中,则跳过正则校验")
                                else:
                                    print("当前的校验的 " + each + " 不在SQL查询到的各个key中")
                                    re1 = re.compile(str(getrejson_i[each]))  # 取Excel正则参数来校验
                                    print('我的全参数2的正则校验结果：    ' + each)
                                    temp = get_re_list(re1, tmp_list)  # 调用#正则匹配序列函数
                                    if temp == False:
                                        temp2 = '我的全参数2的正则校验结果：    ' + each + '   校验失败'
                                        break
                            else:
                                temp = False  # 如果结果不对，写False，如果有message就写，没有就全写入
                                print('该返回json中没有找到对应的keys: '+each+' ，无需调用校验函数，直接匹配失败')
                                temp2 ='该返回json中没有找到对应的keys: '+each+' ，无需调用校验函数，直接匹配失败'
                                break
                    else:
                        print('该SQL精确校验失败，无需进行正则校验')
                if temp:
                    temp = "PASS"
                else:
                    temp = "FAIL"
                jsonresult.append(temp)  # 调用#正则匹配序列函数
                false_why.append(temp2)
            else:
                print("ReSql无数据，打印跳过ReSql的校验")
                if len(test01) == 0:  # 多余的判断，主要为了看无正则表达式时的流程问题
                    print(
                        "@@@@@@@@因ReSql无数据,且无正则表达式，则校验通过@@@@@@@@")
                else:
                    for each in test01:
                        if each in stra:  # 将json转换为字符串，使用in方法判断是否有该字段
                            tmp_list = []  # 暂时用于传参，有时间优化下
                            tmp_list1 = get_dict_value(each, jsondata, tmp_list)  # 调用字典取key的所有值函数
                            re1 = re.compile(str(getrejson_i[each]))  # 取Excel正则参数来校验
                            print('我的全参数3的正则校验结果：    ' + each)
                            temp = (get_re_list(re1, tmp_list1))  # 调用#正则匹配序列函数
                            if temp ==False:
                                temp2='我的全参数3的正则校验结果：    ' + each+'   校验失败'
                                break
                        else:
                            temp = False  # 如果结果不对，写False，如果有message就写，没有就全写入
                            print('该返回json中没有找到对应的keys，无需调用校验函数，直接匹配失败')
                            temp2 ='该返回json中没有找到对应的keys: '+each+' ，无需调用校验函数，直接匹配失败'
                            break
                if temp:
                    temp = "PASS"
                else:
                    temp = "FAIL"
                jsonresult.append(temp)  # 调用#正则匹配序列函数
                false_why.append(temp2)
            responsevalue.append(json.dumps(apijson, ensure_ascii=False))
            print('共有%d个url，当前第%d个执行完毕' % (self.row - self.m, i))
            print("============================================")
            print("============================================")
            print("============================================")
            print("============================================")
            print("============================================")
        print("共有多少个数量需要输出到报告里:")
        print(len(jsonresult))
        print(len(responsevalue))
        print(len(false_why))
        newexcel = excel.openpyxl_read_sheet()
        # sheet1 = newexcel["Sheet1"]
        # 默认获取第一个工作sheet
        sheet1 = newexcel.worksheets[0]
        jsonresult_index = excel.getallcol().index('Status') +1
        responsevalue_index = excel.getallcol().index('ActualResult') +1
        false_why_index = excel.getallcol().index('FalseWhy') + 1
        if self.m==1:
            for j in range(2, self.row+1):
                sheet1.cell(j, jsonresult_index).value = jsonresult[j - 2]  # 正则校验
                sheet1.cell(j, responsevalue_index).value = responsevalue[j - 2]  # json
                sheet1.cell(j, false_why_index).value = false_why[j - 2]  # json
        elif self.m != 1:
            for j in range(self.row, self.row+1):
                sheet1.cell(j, jsonresult_index).value = jsonresult[j - self.row]  # 正则校验
                sheet1.cell(j, responsevalue_index).value = responsevalue[j - self.row]  # json
                sheet1.cell(j, false_why_index).value = false_why[j - self.row]  # json
        # if self.session == 'fanliwang':
        #     path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', 'flw_report.xlsx')
        # el
        if self.session == 'ieng':
            excel_report_file = "ieng_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)

        elif self.session == 'ieng_wx' or self.session == 'ieng_wx_tch' or self.session=='ieng_wx_agt':
            excel_report_file = "ieng_wx_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)

        elif self.session == 'crm':
            excel_report_file = "crm_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)
        elif self.session == 'soyoung_app':
            excel_report_file = "soyoung_app_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report',excel_report_file)
        # elif self.session == 'weizhuanchang':
        #     excel_report_file = weizhuanchang_report.xlsx
        #     path_report = excel_report_file
        # elif self.session == 'meiledev':
        #     excel_report_file = "mlx_report.xlsx"
        #     path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)
        elif self.session == 'xiaochengxu':
            excel_report_file = "xiaochengxu_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)
        elif self.session == 'saas':
            excel_report_file = "saas_mlx_report.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)
        else:
            excel_report_file = "result.xlsx"
            path_report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'excel_report', excel_report_file)
        print(path_report)
        try:
            newexcel.save(path_report)
        except:
            print("对不起，由于您目前打开了正要保存的report文件，请关闭该报告后，再次执行相应自动化用例")