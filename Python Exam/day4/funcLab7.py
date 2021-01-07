from random import *

def differtwovalue(a,b):

    if a>b:
        ans = a-b
    elif a<b:
        ans = b-a
    else:
        ans = 0

    return ans


cycle = 0
while True:
    p = randint(1,30)
    q = randint(1,30)
    res = differtwovalue(p,q)
    print(p,'와',q,'의 차는',res,'입니다')

    cycle +=1
    if cycle == 5:
        break
