# エラーと例外処理
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('need a position between 0 and', len(short_list)-1,
          'but got', position)

# 上の例外処理ではすべての例外について捉えて処理を行うが、詳細が掴めない。
# 下の例では起きうる例外をあらかじめ設定し、その内容を表示するようにしている。
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('bad index : ', position)
    except Exception as other:
        print('something else broke : ',other)
