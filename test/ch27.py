# デコレータ
# 主にデバックに使用される。
# ソースコードを変えずに既存の関数に変更を加えたい時がある。
def document_it(func):
    def new_function(*args, **kwargs):
        print('running function : ', func.__name__)
        print('positional arguments : ', args)
        print('keyword arguments : ', kwargs)
        result = func(*args, **kwargs)
        print('result : ', result)
        return result
    return new_function

# 以下の関数を対象とする。
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

# このように手作業でデコレータの戻り値を入れてもいいが、、、
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

# 下のように@を付けて関数を定義すれば簡単にデコレートできる。
@document_it
def add_ints(a, b):
    return a + b

add_ints(4, 5)

# デコレータは複数持てる。
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)