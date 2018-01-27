#!/usr/bin/python2
import MySQLdb

db = MySQLdb.connect('192.168.0.107','test','test','test')
cursor = db.cursor()
sql = """
    create table test(
        id int
    )"""
cursor.execute(sql)

db.close()



