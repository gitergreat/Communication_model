# -*- coding:UTF-8 -*-
import socket
#import sys

class Sender:
    # 创建 socket 对象
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def __init__(self, port, host=socket.gethostname()):
        self.port = port
        self.host = host

    # 绑定端口号
    def setting(self):
        self.serversocket.bind((self.host, self.port))

        # 设置最大连接数，超过后排队
        self.serversocket.listen(10)

    def start(self):
        while True:
            clientsocket, addr = self.serversocket.accept()
            if clientsocket != None and addr != None:
                print("连接地址: %s" % str(addr))
                return clientsocket, addr

    def sendMessage(self, clientsocket, addr, *filename):
        print("向主机"+str(addr)+"发送数据:")
        for file in filename:
            with open(file, 'r') as f:
                while True:
                    message = f.read()
                    print("正在发送长度为"+str(message.encode('utf8').__len__())+"字节的数据")
                    clientsocket.send(message.encode('utf8'))
                    if (clientsocket.recv(10) == 'ok'.encode('utf8')):
                        print("发送成功")
                        break
                    else:
                        print("发送失败")

    def shutdownConncet(self, clientsocket):
        clientsocket.close()

    def shutdown(self):
        self.serversocket.close()


'''
    def start(self,filename):
        while True:
            # 建立客户端连接
            clientsocket, addr = self.serversocket.accept()
            print("连接地址: %s" % str(addr))
            with open('encrypt_message.txt', 'r') as f:
                message = f.read()
            with open('encrypt_des_key.txt', 'r') as f1:
                encryptDESKey = f1.read()
            #message = input("Input the message to send: ")
            clientsocket.send(message.encode('utf8'))
            clientsocket.send(encryptDESKey.encode('utf8'))
            clientsocket.close()
'''