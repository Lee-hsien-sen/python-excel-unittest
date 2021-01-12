import requests
import json
import time
from common.get_crm_headers import get_crm_headers
time1 =0
time2 =0
# time3 =0
times1=0
times2=0
fail_times1 =0
fail_times2 =0
url_openid ={"email":"kongdefangzhenxuan13@soyoung.com","password":"123456"}
url_openid=json.dumps(url_openid)
print(type(url_openid))
headers =get_crm_headers(url_openid)
print(type(headers))
for i in range(100):
    try:
        r1 = requests.get(url="https://kong.sy.soyoung.com/sys/api/crm/revisit/list?keyword=&page=1&page_size=10&plan_date_end=&plan_date_start=&status=1&target_id=&user_id=",headers=headers)
        time1 += r1.elapsed.microseconds
        times1 += 1
        print(i+1)
    except:
        fail_times1+=1
        print("异常"+str(i+1))
    try:
        r2 = requests.get(url="https://kong.sy.soyoung.com/apidocs/sys-api/index.html#api-crm_dictionary-customerSources")
        time2 += r2.elapsed.microseconds
        times2 += 1
        print(i+1)
    except:
        fail_times2+=1
        print("异常"+str(i+1))
    # r2 = requests.get(url="https://kong.sy.soyoung.com/apidocs/sys-api/index.html#api-crm_dictionary-customerSources")
    # time.sleep(5)
    # r3 = requests.get(url="https://kong.sy.soyoung.com/apidocs/sys-api/index.html#api-crm_dictionary-customerStatus")
    # time.sleep(5)
    # print(r.elapsed.microseconds) #微秒
    # print(r.elapsed.microseconds/1000) #毫秒
    # print(r.elapsed) #秒
    # time2 += r2.elapsed.microseconds
    # time3 += r3.elapsed.microseconds
    # time.sleep(1)
# print(r1.json())
# print(r2.json())
# print(r3.json())
# print(time2)
# print(time3)
if times1 ==0:
    avg_time1 =0
else:
    avg_time1=time1/times1
if times2 ==0:
    avg_time2 =0
else:
    avg_time2=time2/times2
# avg_time3=time3/times
print("1请求失败次数"+str(fail_times1))
print(time1)
print("请求该回访列表接口共"+str(times1)+"次,平均用时（微秒）："+str(avg_time1))
print("请求接口共"+str(times1)+"次,平均用时（微秒）："+str(avg_time1/1000))
print("请求接口共"+str(times1)+"次,平均用时（秒）："+str(avg_time1/1000000))
print("=================================")
print("2请求失败次数"+str(fail_times2))
print(time2)
print("请求该接口https://kong.sy.soyoung.com/apidocs/sys-api/index.html#api-crm_dictionary-customerSources共"+str(times2)+"次,平均用时（微秒）："+str(avg_time2))
print("请求接口共"+str(times2)+"次,平均用时（微秒）："+str(avg_time2/1000))
print("请求接口共"+str(times2)+"次,平均用时（秒）："+str(avg_time2/1000000))
# print("=================================")
# print("请求该接口https://kong.sy.soyoung.com/apidocs/sys-api/index.html#api-crm_dictionary-customerSources共"+str(times)+"次,平均用时（微秒）："+str(avg_time3))
# print("请求接口共"+str(times)+"次,平均用时（微秒）："+str(avg_time3/1000))
# print("请求接口共"+str(times)+"次,平均用时（秒）："+str(avg_time3/1000000))
