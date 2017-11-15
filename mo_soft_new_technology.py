#-*- coding:utf-8 -*-
import pymysql
import json
import warnings
"""
    本程序的功能：
        1. 实现员工管理系统，包含插、删、改、查的功能
    开发环境：
        1. python3.6
        2. mysql.connector连接MariaDB数据库
        3. Linux，Windows没有测试过
    环境配置：
        1. MySQL数据库 port:13306
        2. 安装lib， pip install pymysql
"""
__author__ = "莫宇剑 1103137684@qq.com"
__date__ = "2017-11-14 20:00"


class InitTable:
    """
    nis:员工信息管理
    +-------------------+
    |        nis        |
    +-------------------+
    | name | age | tel  |
    +-------------------+
    | tom  | 14  | 110  |
    +-------------------+
    """
    def __init__(self):
        # create the table nis
        sql="CREATE TABLE IF NOT EXISTS nis(name VARCHAR(20),age INT,tel VARCHAR(20))"
        exec_Mysql(sql)

def exec_Mysql(sql,search=0):
    mysql_connection = pymysql.connect(host="**********",port=13306,user="***************",passwd="***************",database="test")
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
    name = input("Please input the name:")
    age = input("Please input the age:")
    tel = input("Please input the tel:")
    print("Your input:\nname = "+name+"\tage = "+age+"\ttel = "+tel)
    if input("Please ensure your input(y/Y)") in "yY":
        sql = "INSERT INTO test.nis(name,age,tel) VALUES(\""+name+"\", "+age+", \""+tel +"\");"
        exec_Mysql(sql)

def del_Data():
    name = input("Please input the name:")
    sql = "DELETE FROM nis where name=\"" + name + "\""
    exec_Mysql(sql)

def alter_Data():
    search_Data()
    name = input("Please input the name that need alter:")
    age = input("Please input the age:")
    tel = input("Please input the tel:")
    sql = "UPDATE nis SET "
    if age:
        sql = sql + "age=" + "\"" + age + "\""
        if tel:    sql = sql + ","
    if tel:    sql = sql + "tel=" + "\"" + tel + "\""
    sql = sql + " where name=" + "\"" + name + "\""
    exec_Mysql(sql)
    search_Data(name)

def search_Data(name=0):
    sql = "select * from nis"
    if name:    sql = sql +" where name=" + "\"" + name + "\""
    datas = [x for x in exec_Mysql(sql,1)]
    print(json.dumps(datas,indent=1))

if __name__ == "__main__":
    InitTable()
    operator = {"add":add_Data,"del":del_Data,"alter":alter_Data,"search":search_Data}
    strings = """
    说明：本程序实现了对员工信息的增、删、改、查，如果需要查看数据，输入search即可。
        增      删      改        查
        add     del     alter     search
    """
    while input("Enter q to exit or enter any key to continue:") != "q":
        print(strings)
        try:
            operator[input("What is your exec:").strip()]()
        except KeyError:
            print("Error: Unkown the input command")
