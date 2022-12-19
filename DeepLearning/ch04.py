# NANDゲートの実装
import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2]) #numpyは各要素同士が計算される。
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# print(NAND(0, 1))
# print(NAND(1, 0))
# print(NAND(1, 1))
# print(NAND(0, 0)) #ANDとは出力が逆になる。