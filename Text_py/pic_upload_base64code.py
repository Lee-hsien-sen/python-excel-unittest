# webImg = image.get("webImg")
# PATH = os.path.join(MEDIA_ROOT, webImg.name)
# with open(PATH, "wb+") as f:
#     for i in webImg.chunks():
#         f.write(i)

#ajax发送base64
import requests
import base64
import os
# import image
import re
import data
import time
# import settings

encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))
print("=============================1===========================================")
print("==============================2==========================================")

print(encodestr)
# encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))
print("===============================3=========================================")
print("===============================4=========================================")
# print(str(encodestr,'utf-8'))
print("=================================5=======================================")
print("================================6========================================")
# print(os.path)


# with open("／home/chaowei/1.png","rb") as f:
with open("C:/Users/acer/Desktop/1/1.jpg","rb") as f:
# b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())
# base64.b64decode(base64data)
print(base64_data)
print("==================================8======================================")
f_t2='data:image/jpeg;base64,'+str(base64_data,'utf-8')
data0='{"base64code":"'+f_t2+'"}'
data0= eval(data0.encode('utf-8'))
print(type(data0))
print(data0)
url ='https://meile.sy.soyoung.com/v1/user/uploadImage'
headers={'User-Agent': 'MicroMessenger', 'Cookie': 'MEILEDEV=8befe75b7cbb59b6e3e400e89a8c120d'}
# print(data)
# 打印结果为 b'YWJjcjM0cjM0NHI='
r = requests.post(url=url,data=data0,headers=headers,verify=False)
print(type(r.text), r.text)
# image = data.get("brief_image")
# # 获取base64编码
# strs = re.match('^data:image/(jpeg|png|gif);base64,', image)
# print(strs)

#
# # 正则匹配出前面的文件类型去掉
# image = image.replace(strs.group(), '')
# imgdata = base64.b64decode(image)
# #转换成图片对象
# a, b = str(time.time()).split(".")
# path = os.path.join(os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, "activities", activity_name, "ticket"), a + ".jpg")
# brief_image = os.path.join("activities", activity_name, "ticket", a + ".jpg")
# file = open(path, 'wb')
# file.write(imgdata)
# # 保存图片
# file.close()
