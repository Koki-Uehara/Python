# ORゲートの実装
import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2]) #numpyは各要素同士が計算される。
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# print(Or(0, 1))
# print(Or(1, 0))
# print(Or(1, 1))
# print(Or(0, 0)) #ANDとは出力が逆になる。