# Pythonにポインタは存在しない。
# 複数個の引数を受け取れる*
# printのように引数に指定のない関数を作成するときに便利である。
def print_args(*args):
    print('positional argument tuple:', args)
    
print_args()
print_args(3, 2, 1, 'wait', 'uh...')

# *argsはタプルで返される。
# *を使うときにタプル仮引数をargsと呼ぶのはコミュニティの一般的な習慣である。
def print_more(requierd1, requierd2, *args):
    print('need this one : ', requierd1)
    print('need this two : ', requierd2)
    print('all the rest: ', args)
    
print_more('cap', 'gloves', 'monocle', 'mustache wax')