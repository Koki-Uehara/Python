test_list = ['a', 'b', 'c']
del test_list[-1]
# リストはミュータブルのため後から変更は可能。
# 変更不能なタプルもリストへ変換することも可能。
# delは先頭につけて命じ、リストの指定した要素を削除できる。
# もちろんスライスが使える。
print(test_list)

test_list.remove('b')
# removeは要素のどこにあるか分からない場合や、どこを削除しても
# 問題ない場合に使用する。
# メモリの開放は自動的に行う。
print(test_list)

test_list.append('d')
d_string = test_list.pop()
# popはリストの要素を取り出し、そのまま削除まで実行する。
# 引数に何も指定しなければ最後の要素から取り出す。
# -1を指定するのと同じことである。
print(d_string)

print(test_list.index('a'))

print('a' in test_list)