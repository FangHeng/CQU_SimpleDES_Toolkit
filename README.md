# CQU_SimpleDES_Toolkit
重庆大学大数据与软件学院信息安全导论作业1：S-DES算法实现

### 1. 算法实现

> 我们的S-DES算法实现在`SDES/SDES.py`文件中，其中可以使用到S-DES算法的加密和解密两个函数。 

为了实现良好的代码封装，我们定义了一个SDES的加密类。

- 初始化函数为：`def __init__(self, key, P10, P8, IP, IP_INV, EP, S0, S1, P4):`
  - 其中`key`为10位二进制字符串，`P10`、`P8`、`IP`、`IP_INV`、`EP`、`S0`、`S1`、`P4`为置换表，如果不传入，则使用默认的置换表。
  - 我们设计中将作业要求中的置换表作为默认置换表，因此在实验使用时，可以不传入置换表。
- 定义了：`def permute(self, block, table):`函数，用于实现置换操作。
- 定义了：`def left_shift(self, block, shifts):`函数，用于实现循环左移操作，可以选择移动位数。
- 定义了：`def key_generation(self):`函数，用于生成子密钥。
- 定义了：`def f(self, right, subkey):`函数，轮函数f，负责进行扩展、置换、S盒转换等操作。
- 以及加密函数：`def encrypt(self, plaintext):`和解密函数：`def decrypt(self, ciphertext):`。 

故在使用中我们可以直接实例化SDES类，生成一个加密对象。

对于这个加密类调用`encrypt`和`decrypt`函数就可以进行加密和解密操作。