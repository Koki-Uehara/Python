# ジェネレータ
print(sum(range(1, 101)))

# 独自のrange関数を書いてみよう。
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

# my_rangeは通常の関数であり、ジェネレータオブジェクトである。
print(my_range())

# このジェネレータオブジェクトを対象にfor文を回すことができる。
ranger = my_range()
for x in ranger:
    print(x)
    
