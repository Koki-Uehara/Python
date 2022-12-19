# 関数の作成
def do_nothing():
    pass
# 何もしない場合はpassを記述する。

def make_sound():
    print('quack')
    
make_sound()

def echo(anyting):
    return anyting + ' ' + anyting

print(echo('Rumplestiltslin'))

def commentary(color):
    if color == 'red':
        return 'tomato'
    elif color =='green':
        return 'kyuuri'
    elif color == 'bee purple':
        return 'unknow'
    else:
        return 'color push!'

print(commentary('blue'))

# Pythonは何もないときにnoneを返す。noneはfalseだが、falseとは区別しなければならない。
def is_none(thing):
    if thing is None:
        print('is None')
    elif thing:
        print('True')
    else:
        print('False')
    
is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
