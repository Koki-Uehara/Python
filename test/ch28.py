# ローカル変数とグローバル変数
# Pythonではグローバルとローカル変数は同じ名前の変数だとしても別物として扱う。
# 明示的に使用を宣言しなければ別物として生成される。
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals : ', locals())
    
print(animal)
change_local()

print('globals : ', globals())