from pymysql import connect
import datetime

# 连接数据库
conn = connect(host='123.56.98.186', port=3306, db='common-base6', user='admin', password='$TopE#6%@2o1**7ll', charset='utf8')
# print(conn)

# 使用cursor()方法获取操作游标
cur = conn.cursor()

# SQL 插入语句
sql = "INSERT INTO rd_day_total_read(studentID, readDay, readWordNum, readSentenceNum, readSecond, skipWordNum,skipSentenceNum, readBook, isValid, createTime, updateTime, remarks) VALUES(10999,%s, '389', '105', '1800', '0', '0', '13', '1', '2019-03-12 17:53:22', '2019-03-12 18:24:31', NULL)"
# print(sql)

date_str = input("输入日期(例如2019-03-14):")
day = int(input("输入要批量添加的天数:"))
t1 = datetime.date(*map(int, date_str.split('-')))
T = []
for i in range(day):
    t= t1 + datetime.timedelta(days=i)
    t2 = t.strftime("%Y-%m-%d")
    T.append(t2)

for i in T:
    try:
    # 执行sql语句
        cur.execute(sql,i)
        # 提交到数据库执行
        conn.commit()
        print("插入%s成功" %i)
    except :
        # 如果发生错误则回滚
        conn.rollback()
        print("插入%s失败" % i)
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()