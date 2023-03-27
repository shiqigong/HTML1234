from socket import *
s = socket()
s.connect(('127.0.0.1',8888))
msg = input("=>")
s.send(msg.encode())
data = s.recv(1024)
print(data.decode())
s.close()