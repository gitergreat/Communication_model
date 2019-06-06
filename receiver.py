# -*- coding:UTF-8 -*-
import RecivingEnd as R
import RSA
import DES

receiver = R.Receiver(9999)
print("接收方套接字初始化完成")
print()
receiver.connect('./receiver_file/receive_message.txt', './receiver_file/receive_des_key.txt',
                 './receiver_file/receive_sign.txt')
receiver.shutdown()
print()
print("数据接收完成")
print("断开连接")
print()

decryptDESKey = RSA.decryptRSA('./receiver_file/rsa_des_private.txt', './receiver_file/receive_des_key.txt')
with open('./receiver_file/decrypt_des_key.txt', 'w') as f:
    f.write(decryptDESKey.decode('utf8'))
print("des密钥解密完成")

DES.decryptDes('./receiver_file/receive_message.txt', './receiver_file/decrypt_des_key.txt',
               './receiver_file/decrypt_message.txt')
print("接收消息des解密完成")

with open('./receiver_file/decrypt_message.txt', 'r') as f:
    message = f.read()
    print("解密后的消息: "+message)
    print()

flag = RSA.verSign('./publickey_file/rsa_sign_public.txt',
                   './receiver_file/decrypt_des_key.txt','./receiver_file/decrypt_message.txt',
                   './receiver_file/sha1_s.txt', './receiver_file/receive_sign.txt')

if(flag is True):
    print("数字签名验证成功")
else:
    print("数字签名验证失败")