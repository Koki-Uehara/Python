from ch03 import AND
from ch04 import NAND
from ch05 import OR

def XOR(x1, x2): #XOR回路
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))