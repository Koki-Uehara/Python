# ラムダ関数
def edit_story(words, func):
    '無名関数について'
    for word in words:
        print(func(word))
        
stairs = ['thud', 'meow', 'thud', 'hiss']

def enkiven(word):
    return word.capitalize() + '!'

edit_story(stairs, enkiven)

# 上記のような小さい関数をいちいち定義せずとも、ラムダ関数を使えば片つく。
# lambdaのコロンから末尾のカッコまでの間はすべて関数定義である。
# これで小さな関数は名前を覚える必要はなくなる。
edit_story(stairs, lambda word: word.capitalize() + '!')