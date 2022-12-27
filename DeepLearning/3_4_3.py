import numpy as np

# これまでのニューラルネットワークをまとめて実装する。
# 重みとバイアスのディクショナリ作成
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['b2'] = np.array([0.1, 0.2])
    network['b3'] = np.array([0.1, 0.2])
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ニューラルネットワーク（フォワード）の実装
def forward(network, x):
    # 初期化
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = a3 #そのまま値を出力する。
    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
# 前回と同じ出力結果になっていることを確認する。
# このようにまとめて書くと入力を変えたい時に簡単に対応できる。