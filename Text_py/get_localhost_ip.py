
import socket
#获取本机电脑名
myname = socket.gethostname()
print(myname)
#获取本机ip
myaddr = socket.gethostbyname(myname)
print(myaddr)