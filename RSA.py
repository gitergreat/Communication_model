# -*- coding:UTF-8 -*-
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA1
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64
import DES

def getMessage(filename):
    with open(filename,'r') as f:
        message = f.read()
    return message

def generatorKey(publicKey, privateKey):
    random_generator = Random.new().read
    #伪随机数生成器
    #random_generator = Random.new().read
    #rsa算法生成实例
    rsa = RSA.generate(2048, random_generator)

    #master的密钥对生成
    #私钥
    private_pem = rsa.exportKey()
    with open(privateKey, 'w') as f:
        f.write(private_pem.decode('utf8'))
    #公钥
    public_pem = rsa.publickey().exportKey()
    with open(publicKey, 'w') as f:
        f.write(public_pem.decode('utf8'))

def encryptRSA(publicKey, filename):
    with open(publicKey, 'r') as f:
        key = f.read()
        key = key.encode('utf8')
        message = getMessage(filename)
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf8')))
        #print(cipher_text)
        return cipher_text

def decryptRSA(privateKey, filename):
    with open(privateKey,'r') as f:
        key = f.read()
        key = key.encode('utf8')
        encrypted = getMessage(filename)
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(encrypted), "ERROR")#random_generator
        #print(text)
        return text

def sign(kFilename, mFilename, sFilename, wFilename):
    with open(kFilename, 'r') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA1.new()
    with open(mFilename, 'r') as f1:
        message = f1.read()
    with open(sFilename, 'r') as f2:
        message = message + f2.read()
        digest.update(message.encode('utf8'))
        sign = base64.b64encode(signer.sign(digest))
    with open(wFilename, 'w') as f3:
        f3.write(sign.decode('utf8'))

    signature = DES.encryptDes(wFilename, wFilename)
    return signature

def verSign(kFilename1, kFilename2, mFilename, sFilename, wFilename):
    with open(kFilename1) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA1.new()
    with open(mFilename, 'r') as f1:
        message = f1.read()
    with open(sFilename, 'r') as f2:
        message = message + f2.read()
        digest.update(message.encode('utf8'))

    signature = DES.decryptDes(wFilename, kFilename2, wFilename)
    signature = base64.b64decode(signature)

    is_verify = verifier.verify(digest,signature)
    return is_verify