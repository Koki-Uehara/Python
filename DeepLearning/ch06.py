import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y.astype(np.int))
# numpy配列xに対して不等号の演算を行うと各要素に対して比較する。
# 初期の結果はブーリアン型で返されるが、ニューラルネットワークでは、
# 1、0の回答が欲しいため、astypeで変換している。

