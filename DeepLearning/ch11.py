import numpy as np

# 入力値x1,x2
X = np.array([1.0, 2.0])
print(X.shape)

# 各重みの配列
W = np.array([[1.0, 3.0, 5.0], [2.0, 4.0, 6.0]])
print(W.shape)
# XとWの行列の次元数を合わせておくこと。

# y1, y2, y3の3つの出力を一度の内積で計算できる！
Y = np.dot(X, W)
print(Y)