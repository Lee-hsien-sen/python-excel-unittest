#coding:utf-8
from common.data_driver_openpyxl import readexcel
import requests


# 遍历字典查找对应的key的所有值，并以列表的形式返回
# 传入数据的value值是字典，则调用get_target_value  传入数据的value值是列表或者元组，则调用get_list_tuple_value
#遍历函数1：传入数据的value值是字典，则直接调用自身
def get_dict_value(key, dic, tmp_list,tmp_method,tem_description,flag):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        tem_description.append(dic["description"])   # 传入描述数据存在则存入tmp_list
        if int(dic["requestType"]) == 1:
            tmp_method.append("GET")
        elif int(dic["requestType"]) ==2:
            tmp_method.append("POST")
        elif int(dic["requestType"]) ==3:
            tmp_method.append("PUT")
        else:
            tmp_method.append(dic["requestType"])
        print(dic["requestType"],type(dic["requestType"]))
        print(dic[key])
    else:
        for value in dic.values():  # 传入数据不符合KEY,则对其value值进行遍历
            if isinstance(value, dict):
                if "name" in value.keys():
                    print(value["name"])
                else:
                    print("当前字典层级没有name")
                get_dict_value(key, value, tmp_list,tmp_method,tem_description,flag)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                flag =flag+1
                get_list_tuple_value(key, value, tmp_list,tmp_method,tem_description,flag)  # 传入数据的value值是列表或者元组，则调用get_list_tuple_value
    return tmp_list,tmp_method,tem_description

#遍历函数2：传入数据的value值是列表，则直接调用列表
def get_list_tuple_value(key, val, tmp_list,tmp_method,tem_description,flag):
    for val_ in val:
        if isinstance(val_, dict):
            if "name" in val_.keys():
                if flag ==1:
                    print(val_["name"])
                    temp_name = val_["name"]
                    name0.append(temp_name)
                    name1.append("")
                    name2.append("")
                    tmp_list.append("")
                    tmp_method.append("")
                    tem_description.append("")
                elif  flag ==2 :
                    print(val_["name"])
                    temp_name = val_["name"]
                    name0.append(name0[-1])
                    name1.append(temp_name)
                    name2.append("")
                    tmp_list.append("")
                    tmp_method.append("")
                    tem_description.append("")

                elif  flag ==3:
                    print(val_["name"])
                    temp_name = val_["name"]
                    name0.append(name0[-1])
                    name1.append(name1[-1])
                    name2.append(temp_name)

                else:
                    print("序列层级多于三层，需手动添加层级")
            else:
                print("当前字典层级没有name")
            get_dict_value(key, val_, tmp_list,tmp_method,tem_description,flag)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):           #list中还是list，不可能，字典嵌套列表，列表嵌套字典，否则不再是字典
            flag = flag + 1
            get_list_tuple_value(key, val_, tmp_list,tmp_method,tem_description,flag)   # 传入数据的value值是列表或者元组，则调用自身


#
##调试数据##调试数据##调试数据##调试数据##调试数据##调试数据##调试数据##调试数据##调试数据

url='http://192.168.1.250:8080/workspace/loadWorkspace.do'
header = {"Cookie":"JSESSIONID=C745D236D6175E5B633C7EF9C06CEE3C"}           #JSESSIONID 需要更新 #JSESSIONID 需要更新 #JSESSIONID 需要更新 #JSESSIONID 需要更新 #JSESSIONID 需要更新
datas={"projectId":54}
# datas={"projectId":72}


print("每请求一次接口，则打印一次-----------------------------------------")
try:
    r = requests.request('POST',url, data=datas, headers=header)
    print("每请求成功一次接口，则打印一次成功----------------成功------------------------")
except:
    print(u'接口请求35345失败')

print(type(r.text))
r.enconding = 'utf-8'
print(r.text)
print(type(r.text))
# print(r.content)
# print(r.content.decode("utf-8"))
# data0=json.dumps(r.text)
# print(data0)
data1=eval(r.text)
# data = dict(r.text)
# print(data1)
print(type(data1))
print('接口返回的json格式缩进展示：')
# print(json.dumps(data1, ensure_ascii=False,              indent=4))  # indent是缩进的意思，数字4是缩进的程度，ensure_ascii默认为true，会将非ASCII码字符显示为\uXXXX序列

data=data1



flag =0
name0=[]
name1=[]
name2=[]
tmp_list =[]
tmp_method =[]
tem_description=[]
tmp_list1,tmp_method1,tem_description1 = get_dict_value("requestUrl",data,tmp_list,tmp_method,tem_description,flag)
print(tmp_method1,type(tmp_method1))
print(tmp_list1,type(tmp_list1))
print(tem_description1,type(tem_description1))
print(len(name0),name0)
print(len(name1),name1)
print(len(name2),name2)
print(len(tmp_list1),tmp_list1)
print(len(tmp_method1),tmp_method1)
print(len(tem_description1),tem_description1)
excel = readexcel(r'D:\PythonPrp\python+excel+unittest\excel_case\weizhuanchang.xlsx')  # 调用excel文件
newexcel = excel.writeresults()
sheet1 = newexcel.get_sheet(0)  # copy原来的excel

# sheet = data.sheet_by_index(0)
for j in range(1, (len(name0)+1)):
    sheet1.write(j, 1, name0[j - 1])
    sheet1.write(j, 2, name1[j - 1])
    sheet1.write(j, 3, name2[j - 1])
    sheet1.write(j, 4, tmp_list1[j - 1])
    sheet1.write(j, 10, tmp_method1[j - 1])
    sheet1.write(j, 11, tem_description1[j - 1])
newexcel.save(r'D:\PythonPrp\python+excel+unittest\excel_report\saas_meile.xls')
