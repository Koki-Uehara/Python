while True:
    value = input("数字を入力してください。 :")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        print("奇数を入力したら？")
        continue
    print(number, "自乗したら", number*number)