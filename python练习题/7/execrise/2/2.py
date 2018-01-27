#!/usr/bin/python2
import MySQLdb
import os 
def insert_result():
    db = MySQLdb.connect('192.168.0.107','test','test','test')
    cursor = db.cursor()
    cursor.execute("drop table if exists test")
 
    sql_create_table = """create table test(result char(20))"""
    cursor.execute(sql_create_table)

    file_result = open("result")
    cache =file_result.readlines()
    try:
        for i in cache:
            sql_insert_data = "insert into test(result) values('%s')" % i 
            cursor.execute(sql_insert_data)
        db.commit()
    except:
        db.rollback()
    db.close()

insert_result()

