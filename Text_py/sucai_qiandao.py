import urllib.request
import urllib
import gzip
import http.cookiejar


def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.17sucai.com',
}

url = 'http://www.17sucai.com/auth'
opener = getOpener(header)

id = 'xxxxxxx'
password = 'xxxxxxx'
postDict = {
    'email': id,
    'password': password,
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data)

url = 'http://www.17sucai.com/member/sign'  # 签到的地址
op = opener.open(url)

data = op.read()
data = ungzip(data)

print(data)
