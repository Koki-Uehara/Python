import numpy as np
import matplotlib.pyplot as plt

# ステップ関数の実装（段階関数）
def step_functoin(x):
    return np.array(x > 0, dtype=np.int)
# ｘの値が1（true）を超えるとｙは1で出力される。

x = np.arange(-5.0, 5.0, 0.1)
y = step_functoin(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()