empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)
print(type(odd_numbers))

empty_dict = {}
print(type(empty_dict))

letters = set('letters')
print(letters)
print(type(letters))
# 集合はset関数で宣言する。
# 波かっこで使用するが、キーの集まりと考える。
# 集合の中には一意の値しか存在できない。
# setで集合化する際に同じ値はまとめられる。