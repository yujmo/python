#!/usr/bin/python2
import MySQLdb

db = MySQLdb.connect('192.168.0.107','test','test','test')
cursor = db.cursor()
sql= "insert into test(id) values('%d')" % (20)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()



