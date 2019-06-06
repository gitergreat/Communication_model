#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
#print(host)
port = 12345

s.connect((host, port))
print (s.recv(1024))
s.close()