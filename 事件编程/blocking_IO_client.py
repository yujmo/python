import socket
sk=socket.socket()
sk.connect(("127.0.0.1",8080))
while 1:
    data=sk.recv(1024)
    print(data.decode("utf8"))
    sk.send(b"hello server")
