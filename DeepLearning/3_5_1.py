import numpy as np

# ソフトマックス関数の実装（分類問題）
b = np.array([0.3, 2.9, 4.0])
exp_p = np.exp(b)
print(exp_p)

sum_exp_a = np.sum(exp_p)
print(sum_exp_a)
y = exp_p / sum_exp_a
print(y)

# ソフトマックス関数
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# ソフトマックス関数では容易に数値が大きくなりやすく、オーバフローをする。
# そのため返される値はnan(not a number 不安定)
a = np.array([1010, 1000, 990])
print(softmax(a))

# オーバフローの対策として一番大きな値を取得するというもの。
c = np.max(a)
print(a - c)
print(np.exp(a-c) / np.sum(np.exp(a-c)))
# 普通なら出力されない値も、このように最大値を引くことで正常に計算できる。
 
# 以上のことを踏まえてオーバフロー対策したソフトマックス関数を実装。
def softmax2(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

print(softmax2(a))

# 自作したソフトマックスの計算式の結果とオーバフロー対策した関数が同じ結果
print(softmax2(b))

# ソフトマックス関数の出力結果の合計は必ず１になる。
# そのため確率につかえる。
# a[0]は１％、a[1]は２５％、a[2]は７４％なので、正解はa[2]になるという判断。
