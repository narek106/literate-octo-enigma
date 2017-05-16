import math
def F(n):
    return int(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))
while 1:
    x=int(input())
    print(F(x))
