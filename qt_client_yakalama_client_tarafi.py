import socket 

client = socket.socket()

message = str(input('Mesaj: '))

client.connect(('192.168.x.x',4540))

client.send(message.encode())    #ascii ile encode edilirse daha sağlıklı olur

client.close()
