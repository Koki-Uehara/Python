def answer():
    print(42)

def run_something(func):
    func()

# funcにanswerが代入されることでanswer関数が実行される。
# answerを渡していることに注意する。（関数はオブジェクトでもある。）
# Pythonではすべてがオブジェクトと言える。
run_something(answer)
print(type(run_something))

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

# *argsを使って複数の引数を受け取って関数を実行できる。
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

