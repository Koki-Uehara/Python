# 関数内関数　関数を他の関数の中で定義できる。
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

def knigths(saying):
    def inner(quote):
        return "we are the knigth who say : '%s'" % quote
    return inner(saying)

print(knigths('Ni!'))

# クロージャとは関数内関数で、動的に生成されたものである。
# 今回はinnerに引数はなく、代わりにsayingをそのまま使う。
# これは関数であると同時に動的に生成されたクロージャでもある。
def knigths2(saying):
    def inner2():
        return "we are the knigth who say : '%s'" % saying
    return inner2

a = knigths2('duck')
b = knigths2('hasenpfeffer')
print(a, type(a))
print(b, type(b))

# これらは自分が生成されたとき状態を覚えているため、以下のように呼び出すと
# aはwe are the knigth who say : 'duck'
# bはwe are the knigth who say : 'hasenpfeffer'が出力できる。
print(a())
print(b())