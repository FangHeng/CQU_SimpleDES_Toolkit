# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 09:09
# @Author  : Fang Heng
# @File    : SDES.py
# @Software: PyCharm 
# @Comment : S-DES加密类的实现

class SDES:
    '''
    S-DES加密类
    '''

    def __init__(self, key, P10=None, P8=None, IP=None, IP_INV=None, EP=None, S0=None, S1=None, P4=None):
        '''初始化加密类以及对应的密钥和各种转换盒'''
        self.key = key
        self.P10 = P10 if P10 is not None else [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = P8 if P8 is not None else [6, 3, 7, 4, 8, 5, 10, 9]
        self.IP = IP if IP is not None else [2, 6, 3, 1, 4, 8, 5, 7]
        self.IP_INV = IP_INV if IP_INV is not None else [4, 1, 3, 5, 7, 2, 8, 6]
        self.EP = EP if EP is not None else [4, 1, 2, 3, 2, 3, 4, 1]
        self.S0 = S0 if S0 is not None else [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 0, 2]
        ]
        self.S1 = S1 if S1 is not None else [
            [0, 1, 2, 3],
            [2, 3, 1, 0],
            [3, 0, 1, 2],
            [2, 1, 0, 3]
        ]
        self.P4 = P4 if P4 is not None else [2, 4, 3, 1]
        self.k1, self.k2 = self.key_generation()

    def permute(self, block, table):
        '''按照给定的表进行排列操作'''
        return ''.join([block[x-1] for x in table])

    def left_shift(self, block, shifts):
        '''将给定的block进行循环左移操作'''
        return block[shifts:] + block[:shifts]

    def key_generation(self):
        '''密钥生成函数'''
        after_p10 = self.permute(self.key, self.P10)
        left, right = after_p10[:5], after_p10[5:]
        ls1_left, ls1_right = self.left_shift(left, 1), self.left_shift(right, 1)
        ls2_left, ls2_right = self.left_shift(ls1_left, 1), self.left_shift(ls1_right, 1)
        k1 = self.permute(ls1_left + ls1_right, self.P8)
        k2 = self.permute(ls2_left + ls2_right, self.P8)
        print(f'k1:{k1}')
        print(f'k2:{k2}')
        return k1, k2

    def f(self, right, subkey):
        '''轮函数f，负责进行扩展、置换、S盒转换等操作'''
        after_ep = self.permute(right, self.EP)
        after_xor = bin(int(after_ep, 2) ^ int(subkey, 2))[2:].zfill(8)
        left_xor, right_xor = after_xor[:4], after_xor[4:]
        left_s0_row = int(left_xor[0] + left_xor[3], 2)
        left_s0_col = int(left_xor[1] + left_xor[2], 2)
        right_s1_row = int(right_xor[0] + right_xor[3], 2)
        right_s1_col = int(right_xor[1] + right_xor[2], 2)
        sbox_left = bin(self.S0[left_s0_row][left_s0_col])[2:].zfill(2)
        sbox_right = bin(self.S1[right_s1_row][right_s1_col])[2:].zfill(2)
        after_p4 = self.permute(sbox_left + sbox_right, self.P4)
        return after_p4

    def encrypt(self, plaintext):
        '''加密函数，输入明文，输出密文'''
        after_ip = self.permute(plaintext, self.IP)
        left, right = after_ip[:4], after_ip[4:]
        left, right = right, bin(int(left, 2) ^ int(self.f(right, self.k1), 2))[2:].zfill(4)
        left = bin(int(left, 2) ^ int(self.f(right, self.k2), 2))[2:].zfill(4)
        ciphertext = self.permute(left + right, self.IP_INV)
        return ciphertext

    def decrypt(self, ciphertext):
        '''解密函数，输入密文，输出明文'''
        after_ip = self.permute(ciphertext, self.IP)
        left, right = after_ip[:4], after_ip[4:]
        left, right = right, bin(int(left, 2) ^ int(self.f(right, self.k2), 2))[2:].zfill(4)
        left = bin(int(left, 2) ^ int(self.f(right, self.k1), 2))[2:].zfill(4)
        plaintext = self.permute(left + right, self.IP_INV)
        return plaintext



if __name__ == '__main__':

    # 设置一些初始的变量
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 0, 2]
    ]
    S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
]
    P4 = [2, 4, 3, 1]

    # 设置密钥和明文
    key = "1010101010"
    plaintext = "11111111"

    # 进行加密/解密操作
    sdes = SDES(key, P10, P8, IP, IP_INV, EP, S0, S1, P4)
    encrypted = sdes.encrypt(plaintext)
    decrypted = sdes.decrypt(encrypted)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

