#!/usr/bin/python2
import MySQLdb

db = MySQLdb.connect('192.168.0.107','test','test','test')
cursor = db.cursor()
sql= "select * from test"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        print "id=%d" % id
except:
    print "Error 21654"
db.close()



