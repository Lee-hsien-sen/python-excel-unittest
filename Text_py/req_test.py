import requests
method = 'POST'
url = 'https://kong.sy.soyoung.com/sys/api/crm/user/login'
# url = 'https://kapi.soyoung.com/sys/api/crm/user/login'
headers = {}
data ={"email":"kongdefang06@soyoung.com","password":"123456"}
r = requests.post(url=url, data=data, headers=headers, verify=False, timeout=1500)
print(type(r.text), r.text)