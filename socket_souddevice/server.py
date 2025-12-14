
import socket 
import soundfile as sf 
import sounddevice as sd 

matrix,samplerate = sf.read(r"C:\Users\alper\curseforge\minecraft\Instances\Cursed Walking - A Modern Zombie Apocalypse\config\fancymenu\assets\click.wav")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.1.6',45404))
server.listen()

print(*server.getsockname())

client,client_addr = server.accept()

client.send(bytes(matrix))


