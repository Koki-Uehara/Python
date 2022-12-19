# リスト内包表記でリスト作成する。
# forで回すよりも簡潔に記述でき、見やすくなる。
number_list = [i * 2 for i in range(11)]
print(number_list)

number_list = [i for i in range(11)]
print(number_list)

# ifによる条件式の追加も可能。
# この場合、ifで0になるものはfalse、0以外の値になる場合はtrueと判定されて値が代入される。
number_list = [number for number in range(1, 6) if number % 2]
print(number_list)

# 内包表記でforをネストさせることも可能。
# 今回はrow, colをタプルにしているが、リストにすることもできる。
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
print(cells)

# タプル形式から値だけを取り出すことも可能。
for row, col in cells:
    print(row, col)

# 集合の内包表記もある。
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# よりPythonらしい記述。出力順序が変わるのはset関数によるもの。
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# 辞書型の内包表記の長いバージョンも当然可能。
a_set = {number for number in range(1, 11) if number % 2 == 0}
print(a_set)