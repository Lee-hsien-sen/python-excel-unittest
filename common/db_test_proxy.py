#encoding=utf-8
# import pymysql
import time
import threading
import pymysql
from sshtunnel import SSHTunnelForwarder,create_logger

sshIp='10.10.10.100'
sshPort=22
sshUser='kongdefang'
sshPassword='kdf@sy321'


class DbVo(object):

    def __init__(self,
                 host=None,
                 port=None,
                 user=None,
                 password=None,
                 dbName=None,
                 charset='utf-8',
                 localPort=10000
                 ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbName = dbName
        self.charset = charset
        self.localPort = localPort


def connect(proxyInfo):
    server = SSHTunnelForwarder(
        ssh_address_or_host=(sshIp,sshPort),
        ssh_username=sshUser,
        ssh_password=sshPassword,
        local_bind_address=('127.0.0.1',proxyInfo.localPort),#绑定的端口
        remote_bind_address=(proxyInfo.host,proxyInfo.port),#代理远程的端口
        logger=create_logger(loglevel=1)  #sshtunnel打开日志输出
        )
    server.start()

#代理锁死主线程，所有使用一个线程去运行代理
def proxyConnect(proxyInfo):
    thread = threading.Thread(target=connect,args=(proxyInfo,))
    thread.start()


def connectDataBase(dbinfo):
    proxyConnect(dbinfo)
    time.sleep(2)
    client = pymysql.connect(
        host='127.0.0.1',  # 此处必须是是127.0.0.1
        # host=dbinfo.host,  # 此处必须是是127.0.0.1
        port=dbinfo.localPort,
        user=dbinfo.user,
        passwd=dbinfo.password,
        db=dbinfo.dbName,
        charset='utf8')
    return client



def getCount(dbClient):
    sql = "SELECT sms_content FROM db_main.tb_sms_log WHERE  mobile ='13910843622' order BY create_date DESC LIMIT 1"
    print (sql)
    cursor = dbClient.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    print (values[0][0])

dataCenter = DbVo(
    host="10.10.10.110",
    port=13306,
    user="lvweb1",
    password="lavion#2013",
    dbName="db_main",
    localPort=8203
    )

dataCenterDbClient = connectDataBase(dataCenter)
getCount(dataCenterDbClient)

#
# class db_test(object):
#
#     def __init__(self,data):
#         self.data = data#.encode('utf-8')
#         print(self.data)
#         # print(self.data,type(self.data))
#         # mysql的链接配置
#         self.host='10.10.10.110'
#         self.port=13306
#         self.user='lvweb1'
#         self.password= 'lavion#2013'
#         self.db='db_passport'
#
#     def get_db_item(self):
#         # 打开数据库连接
#             ##要在 Mysql 中保存 4 字节长度的 UTF-8 字符，需要使用 utf8mb4 字符集，但只有 5.5.3 版本以后的才支持(查看版本： select version();)。
#             # 我觉得，为了获取更好的兼容性，应该总是使用 utf8mb4 而非utf8.  对于 CHAR 类型数据，utf8mb4 会多消耗一些空间，根据 Mysql 官方建议，使用 VARCHAR  替代 CHAR。
#         sql_order_id = []
#
#         try:
#             db = pymysql.connect(host=self.host, port=self.port,user=self.user, password=self.password,autocommit=True,charset='utf8mb4')         #db=db，不指定表名db_passport_qa，则sql中需加上表名
#             db2=pymysql.Connect(host=self.host, port=self.port,user=self.user, password=self.password,autocommit=True,charset='utf8mb4')
#         except Exception:
#             print(u'Sql连接失败',Exception)
#             sql_order_id.append("Sql连接失败")
#             return sql_order_id
#
#
#         # db = pymysql.connect(host=host, port=port,user=user, password=password,db=db)
#         # 使用 cursor() 方法创建一个游标对象 cursor
#         cursor = db.cursor()
#
#         # 使用 execute()  方法执行 SQL 查询
#         # cursor.execute("SELECT VERSION()")
#         # self.data="SELECT a.order_id FROM  db_beaushare_qa.tb_spread_order_info a,db_beaushare_qa.tb_user_info b WHERE a.spread_uid = b.id AND b.open_id = 'oESYd1TKkOkBNk89ATki3ioPu1fQ'"
#         r=cursor.execute(self.data)
#         # db.commit()
#
#         sql_order_id2 =[]
#         if "order_id" in str(self.data) and ("SELECT" in str(self.data) or "select" in str(self.data)):
#             for i in range(r):
#                 order_id_tem = list(cursor.fetchone())[0]
#                 # print("查询到的order_id是: %s " %order_id_tem,type(order_id_tem))# 使用 fetchone() 方法获取单条数据.，取出一条就没了一条
#                 print(order_id_tem,type(order_id_tem))
#                 sql_order_id.append(str(order_id_tem))
#         elif "token" in str(self.data) and ("SELECT" in str(self.data) or "select" in str(self.data)):
#             token_tem = list(cursor.fetchone())[0]
#             # print("查询到的order_id是: %s " %order_id_tem,type(order_id_tem))# 使用 fetchone() 方法获取单条数据.，取出一条就没了一条
#             print(token_tem, type(token_tem))
#             sql_order_id.append(str(token_tem))
#         elif "SELECT" in str(self.data) or "select" in str(self.data):              #打印其它查询到的信息
#             # print("sql查询语句中没有order_id，将返回的列表设置为【【单空格】】字符列表打印其它查询到的信息")
#             # sql_order_id.append(' ')   #【【单空格】】字符列表，标记单纯的select
#             for i in range(r):
#                 order_id_tem = list(cursor.fetchone())[0]
#                 print("Sql查询到的【非order_id】是: %s " %order_id_tem,type(order_id_tem))# 使用 fetchone() 方法获取单条数据.，取出一条就没了一条
#                 print(order_id_tem,type(order_id_tem))
#                 sql_order_id.append(str(order_id_tem))
#             print(sql_order_id)
#         else:
#             # print("sql查询语句中没有select语句，将返回的列表设置为【【单空格】】字符列表")
#             sql_order_id.append(' ')
#         # print(sql_order_id)
#
#         db.close()
#         return sql_order_id
#
#
#
#
# try:
#     # 通过游标对象执行 sql
#     cursor.execute(sql)
#     db.commit()          # 提交事务到数据执行
# except:
#     db.rollback()        # 发生异常，回滚事务
# ​
# ​
# # 关闭数据库连接对象
# db.close()
# ​
#
# 数据库查询操作
#
# pymysql 的 cursor 对象提供以下方法用于获取 sql 执行结果：
# cursor.fetchone()：获取一行结果，该结果为一个 list 对象；
# cursor.fetchall()：获取所有结果集，该结果是包含所有行对象的 list；
# curosr.rowcount()：获取结果集的行数；



#
# sql = "SELECT user_id, user_name, user_password, user_email FROM t_user "
# ​
# try:
#     # 通过游标对象执行 sql
#     cursor.execute(sql)
# ​
#     # 获取结果集
#     results = cursor.fetchall()
#     for row in results:
#         user_id = row[0]
#         user_name = row[1]
#         user_password = row[2]
#         user_email = row[3]
#         print("info -\t%s\t%s\t%s\t%s " % (user_id, user_name, user_password, user_email))
# ​
#     db.commit()
# except:
#     db.rollback()




#
# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表# # 创建数据库表
# # 打开数据库连接
# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()


# import db
#
# def get_sms_captcha(mobile):
#     # 获取短信验证码
#     sms_captcha = db.execute('select code from send_sms_code where mobile=%s order by id desc',params=(mobile))
#     return sms_captcha['code']
#
# def delete_user(mobile):
#     # 删除用户
#     db.execute('delete from user where mobile=%s',params=(mobile))



# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表# 查询数据库表
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (1000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")
#
# # 关闭数据库连接
# db.close()



# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入# 数据库插入
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 插入语句1# # SQL 插入语句1# # SQL 插入语句1
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#       ('Mac', 'Mohan', 20, 'M', 2000)
# # SQL 插入语句2# # SQL 插入语句2
# ## sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
# ##         LAST_NAME, AGE, SEX, INCOME)
# ##         VALUES ('Mac', 'Mohan', 20, 'M', 2000)""
# # SQL 更新语句# # SQL 更新语句# # SQL 更新语句# # SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# # SQL 删除语句# SQL 删除语句# SQL 删除语句# SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 执行sql语句
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()





# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。


#-=================================================================================
#
# Python shell下操作mysql一直使用MySqldb。
# 其默认的Cursor Class是使用tuple（元组）作为数据存储对象的，操作非常不便
# 1 p = cursor.fetchone()
# 2 print(p[0], p[1])
# 如果有十几个字段，光是数数位数，就把我数晕了。
#
# 当然，MySqldb Cursor Class本身就提供了扩展，我们可以切换成DictCurosor作为默认数据存储对象，如
# MySQLdb.connect(host=127.0.0.1, user=sample, passwd=123456, db=sample, cursorclass=DictCursor, charset=utf8)
# #
# p = cursor.fetchone()
# print(p[id], p[name])字典的方式优于元祖。
#
# 但是，"[]"这个符号写写比较麻烦，并且我编码风格带有强烈的Java习惯，一直喜欢类似"p.id","p.name"的写法。
# 于是，扩展之
# 1. 扩展Dict类，使其支持"."方式：
# 1 class Dict(dict):
#  2
#  3     def __getattr__(self, key):
#  4         return self[key]
#  5
#  6     def __setattr__(self, key, value):
#  7         self[key] = value
#  8
#  9     def __delattr__(self, key):
# 10         del self[key]2. 扩展Curosor，使其取得的数据使用Dict类：
#  1 class Cursor(CursorStoreResultMixIn, BaseCursor):
#  2
#  3     _fetch_type = 1
#  4
#  5     def fetchone(self):
#  6         return Dict(CursorStoreResultMixIn.fetchone(self))
#  7
#  8     def fetchmany(self, size=None):
#  9         return (Dict(r) for r in CursorStoreResultMixIn.fetchmany(self, size))
# 10
# 11     def fetchall(self):
# 12         return (Dict(r) for r in CursorStoreResultMixIn.fetchall(self))
# 这下，就符合我的习惯了：
# 1 MySQLdb.connect(host=127.0.0.1, user=sample, passwd=123456, db=sample, cursorclass=Cursor, charset=utf8)
# 2 #
# 3 p = cursor.fetchone()
# 4 print(p.id, p.name)