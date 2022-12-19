empty_tuple = ()
print(empty_tuple)
# 空のタプルを作る。
# タプルは定数リストであり、変更はできない。

one_max = 'tuple',
print(one_max)

one_marx = 'a', 'b', 'c'
print(one_marx)

a, b, c = one_marx
# タプルなら一度に複数の変数に代入できる。
print(a, b, c)

one_list = ['one', 'two', 'three']
two_list = tuple(one_list)
print(two_list)