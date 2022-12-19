english = 'monday', 'tuesday', 'wednesday'
french = 'lundi', 'mardi', 'mercredi'

# zipでタプルを渡すと要素が同じところでペアができる。
# zipの戻り値はタプルでもリストでもどちらでも対応可能な値である。
print(list(zip(english, french)))

# そのまま辞書に渡すことで辞書が出来上がる。
print(dict(zip(english, french)))