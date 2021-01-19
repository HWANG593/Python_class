from random import *

pairNum1=0
pairNum2=1

while pairNum1 != pairNum2:
    pairNum1 = randint(1,6)
    pairNum2 = randint(1,6)

    if pairNum1 > pairNum2:
        print('pairNum1이 pairNum2 보다 크다')
    elif pairNum1 < pairNum2:
        print('pairNum2이 pairNum1 보다 크다')
    else:
        print('게임 끝')
