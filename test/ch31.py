#独自の例外処理をクラスを使って生成する。 
class UppercaseExcepion(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseExcepion(word)
