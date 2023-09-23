# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 00:09
# @Author  : Fang Heng
# @File    : brute_force_attack.py
# @Software: PyCharm
# @Comment : 暴力破解函数

from SDES.SDES import SDES

def brute_force_attack(ciphertext, expected_plaintext):
    '''暴力破解SDES密钥并返回所有可能的密钥'''
    possible_keys = []
    for i in range(1024):  # 2^10个可能的密钥
        key = bin(i)[2:].zfill(10)  # 将数字转化为10位的二进制字符串表示
        sdes = SDES(key)
        decrypted_text = sdes.decrypt(ciphertext)
        if decrypted_text == expected_plaintext:
            possible_keys.append(key)

    return possible_keys