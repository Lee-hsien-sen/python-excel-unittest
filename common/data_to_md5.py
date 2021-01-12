import hashlib
from urllib import parse
from furl import furl
import re
import requests
# from common.get_fanliwang_token import get_fanliwang_token


def get_data_sign_md5(data):
    if "token" in str(data):
        uid =data["token"]    #data中token这个key的值value就是uid，#uid不能为空，谁调函数，谁控制
        print(uid,type(uid))
        sec_key,token =get_token_sign_md5(uid)
        #sec_key,token有可能获取失败为空值，需要考虑
        data["token"] = token
        aaa =sorted(data.items(),key=lambda item:item[0])
        aaa=dict(aaa)
        print(aaa,type(aaa))
        aaa0=furl().add(aaa)
        print(aaa0,type(aaa0))
        aaa1= str(aaa0)[1:]
        aaa2=aaa1+sec_key
        print(aaa2,type(aaa2))
        str01 = parse.quote(aaa2)
        print(type(str01),str01)
        AA = hashlib.new('md5')
        AA.update(str01.encode(encoding='UTF-8'))
        # AA.update(page)
        print(AA.hexdigest())
        data["sign"]=AA.hexdigest()
        print(data,type(data))
        return data
    else:
        data00 = data
        PUB_SECKEY = 'a4dccc1aab481a42fd086ad9e6433769'
        aaa = sorted(data00.items(), key=lambda item: item[0])
        aaa = dict(aaa)
        print(aaa, type(aaa))
        aaa0 = furl().add(aaa)
        print(aaa0, type(aaa0))
        aaa1 = str(aaa0)[1:]
        aaa2 = aaa1 + PUB_SECKEY
        print(aaa2, type(aaa2))
        str1 = 'page=1' + '&' + 'pid=144943' + PUB_SECKEY
        str01 = parse.quote(aaa2)
        print(type(str01), str01)
        AA = hashlib.new('md5')
        AA.update(str01.encode(encoding='UTF-8'))
        print(AA.hexdigest())
        data00["sign"] = AA.hexdigest()
        print(data00, type(data00))
        return data00



def get_token_sign_md5(uid):
    url = 'http://kong.sy.soyoung.com/open/api/passport/fake-login'
    data00='{"uid":"'+str(uid)+'"}'
    data00=eval(data00)
    print(data00,type(data00))
    PUB_SECKEY = 'a4dccc1aab481a42fd086ad9e6433769'
    aaa =sorted(data00.items(),key=lambda item:item[0])
    aaa=dict(aaa)
    print(aaa,type(aaa))
    aaa0=furl().add(aaa)
    print(aaa0,type(aaa0))
    aaa1= str(aaa0)[1:]
    aaa2=aaa1+PUB_SECKEY
    print(aaa2,type(aaa2))
    str1='page=1'+'&'+'pid=144943'+PUB_SECKEY
    str01 = parse.quote(aaa2)
    print(type(str01),str01)
    AA = hashlib.new('md5')
    AA.update(str01.encode(encoding='UTF-8'))
    print(AA.hexdigest())
    data00["sign"]=AA.hexdigest()
    print(data00,type(data00))
    sec_key,token=fanliwang_token(url,data00)
    return sec_key, token

def fanliwang_token(url,data):
    try:
        print("每请求一次get_fanliwang_token接口，则打印一次-----------------------------------------")
        r = requests.get(url, params=data)      #get的data用params来传递#get的data用params来传递#get的data用params来传递
        rp = dict(r.json())  # 因r.headers返回的不是dict类型，所以dict转化
        print(rp)
        try:
            sec_key = rp['data']["sec_key"]
            token =rp['data']["token"]
            print(u'获取返利网token和私钥成功')
            print(type(sec_key),sec_key)
            print(type(token), token)
            return sec_key, token
        except:
            print(u'获取返利网token和私钥失败')
            sec_key=''
            token=''
            return sec_key,token
    except:
        print(u'接口请求35345失败或无json返回')
        sec_key = ''
        token = ''
        return sec_key, token


#
# data5 ={"keyword":"s&u+n*","page":1,"select_city_id":1}
# get_data_sign_md5(data5)

#
# data1={"pid":144943,"page":1,"p":2,"token":20529650}
# data0=[('p', 2), ('page', 1), ('pid', 144943)]

# data0=(['p', 2], ['page', 1], ['pid', 144943])
# print(data0, type(data0))
# data1=dict(data0)
# print(data1, type(data1))
# data2=list(data1.items())
# print(data2, type(data2))
# data3=tuple(data2)
# print(data3, type(data3))

# get_data_sign_md5(data1)

print(parse.quote("https://kong.sy.soyoung.com/open/html/fanli/"))




# #最简单的方法，这个是按照key值排序：
# def sortedDictValues1(adict):
#     items = adict.items()
#     items.sort()
#     return [value for key, value in items]
#
# #又一个按照key值排序，貌似比上一个速度要快点
# def sortedDictValues2(adict):
#     keys = adict.keys()
#     keys.sort()
#     return [dict[key] for key in keys]
#
# #还是按key值排序，据说更快。。。而且当key为tuple的时候照样适用
# def sortedDictValues3(adict):
#     keys = adict.keys()
#     keys.sort()
#     return map(adict.get, keys)
#
# #一行语句搞定：
# [(k,di[k]) for k in sorted(di.keys())]
# #用sorted函数的key参数（func）排序：
# #按照key进行排序
# print (sorted(dict1.items(), key=lambda d: d[0]))


# getlongtexturl="http://kong.sy.soyoung.com/open/api/passport/fake-login"
# params={
#             "uid":20529650,
#             "sign":"3056102953c65d666847e0275eb6081c"  }
# newurl=furl(getlongtexturl).add(params).url
# print(newurl)


#这个是js的结果
# encodeURIComponent('中国')
# "%E4%B8%AD%E5%9B%BD"
# jsRet='%E4%B8%AD%E5%9B%BD'
# print(parse.unquote(jsRet))       #输出：中国
# print(jsRet==parse.quote('中国'))  #输出：True
# str0="page=1&pid=144943a4dccc1aab481a42fd086ad9e6433769"
# print(str0)
# str0 = parse.quote(str0)
# print(str0)
# 签名校验接口
# https://kong.sy.soyoung.com/open/api/passport/encrypt?pid=144943

# https://kong.sy.soyoung.com/open/api/shop/calendar/product-calendar?pid=56920&page=1&sign=ecdf549f1924bbb4932a6ec9a5fd0107
# pid=56920&page=1&sign=ecdf549f1924bbb4932a6ec9a5fd0107
# ecdf549f1924bbb4932a6ec9a5fd0107

# https://kong.sy.soyoung.com/open/api/shop/goods/detail?pid=144943&sign=f9674ed4861e350d9bbf28a9b7ab1a15
# pid=144943&sign=f9674ed4861e350d9bbf28a9b7ab1a15

# page=1&pid=144943a4dccc1aab481a42fd086ad9e6433769
# page%3D1%26pid%3D144943a4dccc1aab481a42fd086ad9e6433769
# "data":{"params":{"page":"1","pid":"144943"},"sign":"d300e053684e4665b09c4d87b88db303",
# "str":"page%3D1%26pid%3D144943a4dccc1aab481a42fd086ad9e6433769","sec_key":"a4dccc1aab481a42fd086ad9e6433769"}
# pid=56920
# pid=bytes(pid)
# print(type(pid),pid)
# page=1
# page=bytes(page)
# print(type(page),page)
# sign =hashlib.md5(PUB_SECKEY.encode(encoding='UTF-8')+page+pid).hexdigest()
# print(sign)
# sign =hashlib.md5(page,pid,PUB_SECKEY).hexdigest()
# sign =hashlib.md5(page+pid+PUB_SECKEY).hexdigest()

# print(hashlib.md5(PUB_SECKEY))
# print(hashlib.md5(bytes(PUB_SECKEY.encode(encoding='UTF-8'))).hexdigest())
# print(hashlib.md5(PUB_SECKEY.encode(encoding='UTF-8')).hexdigest())
# # _md5.mD5Type
# sign =_md5.md5("pid=56920,page=1",2)
# print(sign,type(sign))
# data = '你好'
# print(hashlib.md5(data.encode(encoding='UTF-8')).hexdigest())
# print(hashlib.md5('你好'.encode(encoding='GBK')).hexdigest())
# # 或者可以这样
# print(hashlib.md5(b'123').hexdigest())
# print(hashlib.new('md5', b'123').hexdigest())
# m = hashlib.new('md5')
# m.update(b'123456')
# # hashlib.md5('你好'.encode(encoding='GB2312')).hexdigest()
# # hashlib.md5('你好'.encode(encoding='GB18030')).hexdigest()
# print(m.hexdigest())
# # print(hashlib.algorithms_guaranteed)
# # print(hashlib.algorithms_available)
# # m = hashlib.md5()
# # m.update(b'123')
# # m.update(b'456')
# # print(m.hexdigest())
# # print(m.hexdigest())
# # print(hashlib.md5(b'123456').hexdigest())
# # print()



# hash.hexdigest()都知道，在英语中hex有十六进制的意思，因此该方法是将hash中的数据转换成数据，其中只包含十六进制的数字。另外还有hash.digest()方法。