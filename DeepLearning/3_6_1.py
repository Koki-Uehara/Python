import sys, os
sys.path.append(r'C:\Users\pc12h\Python\deep-learning-from-scratch-master')
from dataset.mnist import load_mnist
import numpy as np
import matplotlib.pyplot as plt
import pickle 

(x_train, t_train), (x_test, t_test) = load_mnist()

# 訓練用のデータ形状
print(x_train.shape)
print(t_train.shape)

# テスト用のデータ形状
print(x_test.shape)
print(t_test.shape)

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    
    return x_test, t_test

def init_network():
    with open(r"C:\Users\pc12h\Python\deep-learning-from-scratch-master\ch03\sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# オーバフロー対策したソフトマックス関数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    
    return y
    
x, t = get_data()
network = init_network()
xaccuracy_cut = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y) #最も確率の高い要素のインデックスを取得
    if p == t[i]:
        accuracy_cut += 1
# 正解率出力
print("Accuracy:" + str(float(accuracy_cut) / len(x)))

x, _ = get_data()
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']

print(x.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)

