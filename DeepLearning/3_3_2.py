import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.ndim)
print(a.shape)

b = np.array([[1, 2], [3, 4]])
print(b.shape)
c = np.array([[5, 6], [7, 8]])
print(c.shape)

print(np.dot(b, c))

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape)
print(np.dot(A, B))