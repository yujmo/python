#!/usr/bin/python2
import MySQLdb

db = MySQLdb.connect('192.168.0.107','test','test','test')
cursor = db.cursor()
cursor.execute("SELECT version()")
data = cursor.fetchone()

print data

db.close()



