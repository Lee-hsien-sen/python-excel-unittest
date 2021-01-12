# coding:utf-8
from common.db_dict_test import  db_dict_test
# 那么如何来控制警告错误的输出呢？很简单
import warnings
warnings.filterwarnings("ignore")


for i in range(1700,1800):
    sql='insert into db_beaushare.tb_notices_info  values ('+str(i)+', 1,2,1,1000,10266,526,"1000-01-01 00:00:00","2018-06-11 14:42:31",0,0,"1000-01-01 00:00:00")'
    db_auto = db_dict_test(sql)
    aaa=db_auto.get_db_item()
    # print(aaa)