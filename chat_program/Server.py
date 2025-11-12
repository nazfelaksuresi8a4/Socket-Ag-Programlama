from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import socket
import sys as _s

class ServerThreadClass(QObject):
    threadSignal = pyqtSignal(str,str)
    connectionSignal = pyqtSignal(str,str)

    def __init__(self,ip,port,msg):
        self.message = msg
        self.ip = ip
        self.port = port
        
        self.server_flag = False

        if self.server_flag == False:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.bind((self.ip,self.port))
        
        self.server.listen(1)
        self.conn,self.conaddr = self.server.accept()

    def SendMsg(self):
        
        ip,port = self.conn.getsockname()

        self.message = str(input('mesaj: '))

        if self.message is not None:
            if type(self.message) != str:
                try:
                    self.conn.send(str(self.message).encode())
                    
                except Exception as SendException:
                    print(SendException,'sendException')
                
            else:
                if isinstance(self.message,str):
                    self.conn.send(self.message.encode())
                    
                else:
                    if type(self.message) != str:
                        try:
                            message = str(self.message)
                            self.conn.send(message.encode())
                            
                        except Exception as sendException_2:
                            print(sendException_2,'sendException_2')

            self.recvMessage()

    def recvMessage(self):
        while True:
            message = self.conn.recv(1024).decode()
            
            if message is not None:
                print(message)

            break
        
        self.SendMsg()

Main = ServerThreadClass('172.16.0.2',45404,'Mesaj')
call = Main.SendMsg()
