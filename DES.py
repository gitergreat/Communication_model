# -*- coding:UTF-8 -*-
from Crypto.Cipher import DES
import base64
import random
import string

def generateKey():
    key = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    with open('./sender_file/des_key.txt', 'w') as f:
        f.write(key)

def encryptDes(mFilename, wFilename):
    with open(mFilename, 'r') as f:
    #with open('./sender_file/send_message.txt', 'r') as f:
        message = f.read()
    if message is None:
        return ""
    try:
        with open('./sender_file/des_key.txt', 'r') as f1:
            key = f1.read()
        #ECB
        generator = DES.new(key.encode('utf8'), DES.MODE_ECB)

        pad = 8 - len(message) % 8
        pad_str = ""
        for i in range(pad):
            pad_str = pad_str + chr(pad)

        #encrypted = generator.encrypt(bytes(message.ljust(16, '').encode('utf8')))
        #加密
        encrypted = generator.encrypt((message + pad_str).encode('utf8'))
        #编码得密文
        result = base64.b64encode(encrypted)
        with open(wFilename, 'w') as f2:
        #with open('./sender_file/encrypt_message.txt', 'w') as f2:
            f2.write(result.decode('utf8'))
        return result
    except Exception as e:
        print(Exception,":",e)
        return ""

def decryptDes(mFilename, kFilename, wFilename):
    with open(mFilename, 'r') as f:
    #with open('./receiver_file/receive_message.txt', 'r') as f:
        encrypted = f.read()
    if encrypted is None:
        return ""
    try:
        with open(kFilename, 'r') as f1:
            key = f1.read()
        generator = DES.new(key.encode('utf8'), DES.MODE_ECB)
        #解码
        crypted_str = base64.b64decode(encrypted)
        #解密
        result = generator.decrypt(crypted_str)
        #替换非空格字符
        plain = result.decode('utf8')
        deMessage = plain[0:ord(plain[len(plain)-1])*-1]
        with open(wFilename, 'w') as f2:
        #with open('./receiver_file/decrypt_message.txt', 'w') as f2:
            f2.write(deMessage)
        return deMessage
    except Exception as e:
        print(Exception, ":", e)
        return ""

        #result = result.replace("\x06".encode(), "".encode())
        #result = result.replace("\x08".encode(), "".encode())
        #result = result.rstrip('\0')
        #result = result.strip("�����".encode('utf8'))
        #result = result.strip("������".encode('utf8'))
        #deMessage = result.decode('utf8').rstrip("�����")
        #deMessage = deMessage.rstrip("������")
        #deMessage = result.decode('utf8').rstrip('')
        #result.decode('utf8').rstrip('')