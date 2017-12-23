#-*- coding:utf-8 -*-
import time
import warnings
import random
import pymysql
__author__ = "莫宇剑 1103137684@qq.com"
__date__ = "2017-11-23"

def exec_Mysql(sql,search=0):
    mysql_connection = pymysql.connect(host="localhost",port=3306,user="root",passwd="admin",database="test")
    cursor = mysql_connection.cursor()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        results = cursor.execute(sql)
        mysql_connection.commit()
    if search:
        datas = cursor.fetchmany(results)
        cursor.close()
        return datas
    cursor.close()

def add_Data():
    #sql = "INSERT INTO test.nis(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20) VALUES(" + str( random.randint(1,10000)) +  "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,50000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + "," + str(random.randint(1,10000)) + ");"
    #sql = "INSERT INTO test.nis(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14) VALUES(" + str(5192) + ","+ str(3212) +","+ str(19283) +","+str(12312) +","+str(74638) +","+ str(1293) +","+ str(10023) +"," + str(2387) +","+str(9861)+","+str(1462)+","+ str(11111)+","+str(1231) +","+str(46272) +","+ str(21312)  + ");"
    time1 = time.time()
    sql = "select * from  test.nis where  x1=5192 and x2=3212 and x3=19283 and x4=12312 and x5=74638 and x6=1293 and x7=10023 and x8=2387 and x9=9861 and x10=1462 and x11=11111 and x12=1231 and x13=46272 and x14=21312;"
    exec_Mysql(sql)
    time2 = time.time()
    print(time2-time1)

if __name__ == "__main__":
#   sql="CREATE TABLE IF NOT EXISTS nis(name VARCHAR(20),age INT,tel VARCHAR(20),x1 INT ,x2 INT,x3 INT,x4 INT,x5 INT ,x6 INT ,x7 INT,x8 INT ,x9 INT ,x10 INT ,x11 INT ,x12 INT ,x13 INT ,x14 INT,x15 INT ,x16 INT ,x17 INT ,x18 INT ,x19 INT ,x20 INT)"
    #for x in range(100000):
    add_Data()

