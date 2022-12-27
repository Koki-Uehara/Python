import numpy as np

# シグモイド関数（リストを貰ってリストで結果を返す）
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

# 第一層部分の実装
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5] ,[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
print(X.shape)
print(W1.shape)
print(B1.shape)
A1 = np.dot(X, W1) + B1 
print(A1)
Z1 = sigmoid(A1)
print(Z1)

# 第二層部分の実装
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print(W2.shape)
print(B2.shape)
print(Z1.shape)
A2 = np.dot(Z1, W2) + B2
print(A2)
Z2 = sigmoid(A2)

# 第三層部分の実装
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3  =np.dot(Z2, W3) + B3
Y = A3
print(Y)