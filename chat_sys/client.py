import socket 

ip = '127.0.0.1'
port = 4540

server = socket.socket()

server.connect((ip,port))

while True:
    message = str(input('Mesaj girin: '))
    server.send(message.encode())

server.close()