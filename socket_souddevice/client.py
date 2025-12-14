import socket 
import sounddevice as sd 
import numpy as np 

bytearr = bytearray()
flag = True

client = socket.socket()

client.connect(('192.168.1.6',45404))

while True:
    v = client.recv(1024)
    if not v:
        break
    bytearr.extend(v)

client.close()

buffer = np.frombuffer(bytearr)

sd.play(buffer)
sd.wait()



