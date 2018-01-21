## server
# -*- coding:utf-8 -*-
#Author: yujmo
import socket
sk=socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)
while 1:
    conn,addr=sk.accept()
    while 1:
        conn.send("hello client".encode("utf8"))
        data=conn.recv(1024)
        print(data.decode("utf8"))
