
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert' : dessert}
# 位置引数（実引数と仮引数のポジションがあってないと意図しない値が入ってしまう。）
print(menu('ロマネコンティ', '鶏肉', 'チーズケーキ'))

# 位置引数のような現象をさけるためにはキーワード引数を遣えばよい。
print(menu(entree='鶏肉', dessert='チーズケーキ', wine='ロマネコンティ'))

# デフォルト引数
def menu(wine, entree, dessert = 'pudding'):
    return {'wine': wine, 'entree': entree, 'dessert' : dessert}
print(menu('ロマネコンティ', 'チーズケーキ'))

# 引数のデフォルトに空のリストを作成しているが、これは定義された最初だけが空であり、
# 2回目以降は前のリストが残ったままである。
def buggy(arg, result = []):
    result.append(arg)
    print(result)
    
buggy('b')
buggy('a')

def buggy_2(arg):
    result = []
    result.append(arg)
    return result

print((buggy_2('b')))
print((buggy_2('a')))