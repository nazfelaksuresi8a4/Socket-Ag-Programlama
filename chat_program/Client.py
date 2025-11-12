from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import socket
import sys as _s

class ServerThreadClass(QObject):
    threadSignal = pyqtSignal(str,str)
    connectionSignal = pyqtSignal(str,str)

    def __init__(self,ip,port,msg):
        self.message = 'test'
        self.ip = ip
        self.port = port
        
        self.message_flag = False
        self.server_flag = False

        if self.server_flag == False:
            self.client = socket.socket()
            self.client.connect((self.ip,self.port))


    def SendMsg(self):      
        self.message = str(input('Mesaj yazın: '))
        
        if self.message is not None:
            if type(self.message) != str:
                try:
                    self.client.send(str(self.message).encode())
                
                except Exception as SendException:
                    print(SendException,'sendException')
            
            else:
                if isinstance(self.message,str):
                    self.client.send(self.message.encode())
                
                else:
                    if type(self.message) != str:
                        try:
                            message = str(self.message)
                            self.client.send(message.encode())
                        
                        except Exception as sendException_2:
                            print(sendException_2,'sendException_2')
            
            self.RecvMessage()

    
    def RecvMessage(self):
        while True:
            message = self.client.recv(1024).decode()

            if message is not None:
                print(message)
            
            break
        
        self.SendMsg()
        


Main = ServerThreadClass('172.16.0.2',45404,None)
call = Main.RecvMessage()
