# -*- coding:UTF-8 -*-
import RSA

print("正在重置rsa密钥")
RSA.generatorKey('./publickey_file/rsa_sign_public.txt', './sender_file/rsa_sign_private.txt')
print("发送方rsa密钥对重置完成")
RSA.generatorKey('./publickey_file/rsa_des_public.txt', './receiver_file/rsa_des_private.txt')
print("接收方rsa密钥对重置完成")
