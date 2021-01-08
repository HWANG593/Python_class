from random import *

tmp = []

while len(tmp) != 6:
    num = randint(1,45)
    if num in a:
        continue
    else:
        tmp.append(num)

print('행운의 로또번호 :',tmp)