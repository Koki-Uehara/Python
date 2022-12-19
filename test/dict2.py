pythons = {
    'chapman' : 'graham',
    'cleese' : 'john',
    'idle' : 'eric',
    'jones' : 'terry',
    'palin' : 'michael'
}

print(pythons)

pythons['gilliam'] = 'gerry'
print(pythons)

pythons['gilliam'] = 'terry'
print(pythons)
# 辞書のキーは一意の値でなくてはならない。
# 同じキーが存在する場合は、最後に使用されたキーが残る。

others = {'marx' : 'gtoucho', 'howard' : 'moe'}
pythons.update(others)
print(pythons)

del pythons['marx']
print(pythons)

print(pythons.get('howard'))