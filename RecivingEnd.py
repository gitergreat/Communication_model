# -*- coding:UTF-8 -*-
import socket
#import sys

class Receiver:
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, port, host=socket.gethostname()):
        self.port = port
        self.host = host


    '''
        def connect(self, *filename):
        # 连接服务，指定主机和端口
        self.s.connect((self.host, self.port))
        # 接收小于 1024 字节的数据
        for file in filename:
            message = self.s.recv(1024)
            print (message.decode('utf8'))
            with open(file, 'w') as f:
                f.write(message.decode('utf8'))
        self.s.close()
    '''

    def connect(self, *filename):
        # 连接服务，指定主机和端口
        self.s.connect((self.host, self.port))
        print("与发送方建立连接成功")
        # 接收小于 1024 字节的数据
        print("正在接收数据")
        for file in filename:
            message = self.s.recv(1024)
            print("接收到"+str(len(message))+"字节数据")
            with open(file, 'w') as f:
                f.write(message.decode('utf8'))
                print("将数据写入文件"+file)
            self.s.send('ok'.encode('utf8'))

    def shutdown(self):
        self.s.close()