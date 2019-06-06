# -*- coding:UTF-8 -*-
import SendingEnd as S
import DES
import RSA

sender = S.Sender(9999)
sender.setting()
print("发送方套接字初始化完成")
print()

DES.generateKey()
encryptDESKey = RSA.encryptRSA("./publickey_file/rsa_des_public.txt", "./sender_file/des_key.txt")
with open('./sender_file/encrypt_des_key.txt', 'w') as f:
    f.write(encryptDESKey.decode('utf8'))
print("des密钥生成及其rsa加密完成")

DES.encryptDes('./sender_file/send_message.txt', './sender_file/encrypt_message.txt')
print("发送消息des加密完成")

RSA.sign('./sender_file/rsa_sign_private.txt', './sender_file/send_message.txt',
         './sender_file/sha1_s.txt', './sender_file/sign.txt')
print("数字签名生成完成")
print()

print("发送方等待连接建立")
print()
client,addr = sender.start()

with open('./sender_file/send_message.txt', 'r') as f:
    message = f.read()
    print("待发送的消息: "+message)
    print()

sender.sendMessage(client, addr, './sender_file/encrypt_message.txt', './sender_file/encrypt_des_key.txt',
                   './sender_file/sign.txt')
print()
print("数据发送完成")
print("断开连接")
sender.shutdownConncet(client)
sender.shutdown()