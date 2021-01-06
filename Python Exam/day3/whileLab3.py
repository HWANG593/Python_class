from random import *

#ASCII chr(65)는 A chr(90)는 Z
a = 0
cycle = 0


while True:
    a = randint(0,30)
    if a == 0 or a >= 27:
        break
    else:
        print(chr(64+a),'(',a,')',sep='')
        cycle += 1

print('수행횟수는',cycle,'번입니다')