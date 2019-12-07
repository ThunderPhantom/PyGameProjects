#server.py
import socket
host=''
port=12345
backlog = 5
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
print('socket binded to',port)
s.listen(backlog)
conn,address.accept()
print('socket is listening')
print("Got connection from",addr)
while 1:
 name=input('hello Say something to the client')
 print("waiting for client's response")
 conn.send(name.encode())
 data = conn.recv(1024).decode('utf-8')
 print('Received from client address: ', addr)
 print("Message received: ", data)
conn.close()