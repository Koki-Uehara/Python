# **を使えばキーワード引数を一個にまとめることができる。
def print_kwargs(**kwargs):
    print('keyword argument : ', kwargs)
    
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')