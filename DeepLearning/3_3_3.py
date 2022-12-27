import numpy as np

# Xは入力される決められた値
X = np.array([1,2])
print(X.shape)
# Wは重み
W = np.array([[1,3,5], [2,4,6]])
print(W.shape)
Y = np.dot(X, W)
print(Y)
