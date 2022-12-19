drinks = {
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua', 'vodka'},
    'manhattan' : {'rye', 'vermouth', 'bitters'},
    'screwdriver' :{'orange juice', 'vodka'}
}
# 辞書はキーと値になっているが、集合は値のシーケンスである。

# ウォッカの入ったドリンクが飲みたい。
# for name, contents in drinks.items():
#     if 'vodka' in contents:
#         print(name)
        
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)
        
# オレンジジュースかベルモットが入ったカクテルが飲みたいとき。
for name, contents in drinks.items():
    if contents & {'orange juice', 'vermouth'}:
        print(name)
# ＆で積集合を取れる。（C言語の論理積のこと。）
# 同じ集合（値）を掛けたときに1が出力される。→trueである。　

# 一個前の書き直し。
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
# 集合の中にvodkaがあるかつ、集合の中にどちらかの材料が含まれていなけらばtrueとする。