# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 00:55
# @Author  : Fang Heng
# @File    : encryption_statistics.py
# @Software: PyCharm
# @Comment : 暴力加密统计

from SDES.SDES import SDES
import pandas as pd

def encryption_statistics(plaintext):
    '''统计明文在所有可能的SDES密钥下加密后的密文频率'''
    # 初始化一个空字典来保存密文及其出现的次数
    ciphertexts = {}

    for i in range(1024):  # 2^10 = 1024 个可能的密钥
        key = bin(i)[2:].zfill(10)  # 将数字转化为10位的二进制字符串表示
        sdes = SDES(key)
        encrypted_text = sdes.encrypt(plaintext)

        # 如果这个密文已经在字典中，则增加其计数，否则初始化为1
        if encrypted_text in ciphertexts:
            ciphertexts[encrypted_text] += 1
        else:
            ciphertexts[encrypted_text] = 1

    # 使用pandas构建一个DataFrame来展示统计数据
    df = pd.DataFrame(list(ciphertexts.items()), columns=["Ciphertext", "Count"])

    # 按Count列排序，以显示最常见的密文
    df = df.sort_values(by="Count", ascending=False)

    return df