#server-side#

import socket 

ip = '127.0.0.1'
port = 4540

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port)) #ip ve portu servera tanımladık 
server.listen(1)     #suncu istekleri dinlemeye hazır

print('Sunucu istemciyi dinliyor..')

conn,adr = server.accept() #bağlanan client ve ip adresini tuple olarak döner
while True:
    try:
        a = str(conn.recv(1024).decode())
    except:
        a = None

    if a is not None:
        if type(a) == str:
            print(a)
        else:
            pass
    else:
        pass

#print(conn,adr)    

