# 以下、リストを作成する方法であり、すべて同じ結果となる。
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)
    
print(list(range(1, 6)))