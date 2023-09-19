# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 10:03
# @Author  : Fang Heng
# @File    : example.py
# @Software: PyCharm 
# @Comment :

from SDES.SDES import SDES

if __name__ == '__main__':

    # 1. 初始化SDES类
    sdes = SDES(key='1010101010')

    # 2. 加密
    ciphertext = sdes.encrypt(plaintext='11111111')
    print("加密后的密文为：{}".format(ciphertext))

    # 3. 解密
    plaintext = sdes.decrypt(ciphertext=ciphertext)
    print("解密后的明文为：{}".format(plaintext))