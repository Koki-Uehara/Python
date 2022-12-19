short_list = [x for x in range(3, -1, -1)]
print(short_list)

for x in short_list:
    print(x)
    
even_number = [number for number in range(10) if number % 2 == 0]
print(even_number)

squares = {key: key*key for key in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2}
print(odd)

def good():
    return ['h', 'r', 'herm']

print(good())

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def good():
    print ('h', 'r', 'herm')     
good()

class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException:
    print('caugth an oops')

title = ['creature of habit', 'crewel fate']
plots = ['a nun turns into a monster', 'a haunted yarn shop']
moveis = dict(zip(title, plots))
print(moveis)

# 内包表記でジェネレータを自作して、それをfor文で回しながらprintする。
# 内包とジェネレータの使い方
for things in ('Got %s' % number for number in range(10)):
    print(things)