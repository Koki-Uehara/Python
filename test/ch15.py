# rangeはスライス関数とよく似ており、スタートからエンドまでステップを刻んで範囲を作る。
for x in range(0, 3):
    print(x)
    
print(list(range(0, 3)))

for y in range(2, -1, -1):
    print(y)
    
print(list(range(2, -1, -1)))

z = list(range(0, 11, 2))
print(z)