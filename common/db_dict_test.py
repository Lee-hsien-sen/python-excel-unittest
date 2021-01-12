import pymysql
# import MYSQLdb
class db_dict_test(object):

    def __init__(self,data):
        self.data = data#.encode('utf-8')
        print(self.data)
        # 目前通用新SQL，不需要代理，只需连上360Connect即可
        self.host = '10.10.10.110'
        self.port = 6033
        self.user = 'lvweb1'
        self.password = 'lavion#2013'
        # self.db = 'db_beaushare'
    def get_db_item(self):
        # 打开数据库连接
            ##要在 Mysql 中保存 4 字节长度的 UTF-8 字符，需要使用 utf8mb4 字符集，但只有 5.5.3 版本以后的才支持(查看版本： select version();)。
            # 我觉得，为了获取更好的兼容性，应该总是使用 utf8mb4 而非utf8.  对于 CHAR 类型数据，utf8mb4 会多消耗一些空间，根据 Mysql 官方建议，使用 VARCHAR  替代 CHAR。
        sql_dict = []
        try:
            db = pymysql.connect(host=self.host, port=self.port,user=self.user, password=self.password,autocommit=True,charset='utf8mb4')         #db=db，不指定表名db_passport_qa，则sql中需加上表名
            cursor=db.cursor(pymysql.cursors.DictCursor)
            # if not cursor:
            #     raise (NameError, "连接数据库失败")
            # else:
            #     return cursor
            print("执行完毕打印一次")
        except Exception:
            print(u'Sql连接失败',Exception)
            sql_dict.append("Sql连接失败")
            return sql_dict
        r=cursor.execute(self.data)
        xxx=cursor.fetchall()
        # print(type(xxx), xxx)
        sql_tem={}
        for i in xxx:
            print(i)
            sql_dict.append(i)
        # print(sql_dict)
        db.close()

        # 调试异常
        # sql_dict = []
        # sql_dict.append("Sql连接失败")
        return sql_dict