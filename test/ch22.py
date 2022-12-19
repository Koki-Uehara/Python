# docstring 関数の先頭に文字列を打ち込めば、ドキュメントを付けることができる。
def echo(anything):
    'echoは与えられた入力引数を返す。'
    return anything

def print_if(thing, check):
    '''
    第二引数が真なら第一引数を表示する
    好みのも問題だが、こうやって長い文章も書ける。
    '''
    if check:
        print(thing)
# 関数のドキュメントを表示するにはhelp関数を使う。
help(echo)

print(echo.__doc__)