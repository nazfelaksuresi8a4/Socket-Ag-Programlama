import socket 

ip = '127.0.0.1'
port = 4540

server = socket.socket()

server.connect((ip,port))

server.send('merhaba'.encode())

server.close()