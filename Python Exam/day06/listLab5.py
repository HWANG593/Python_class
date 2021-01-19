from random import *

tmp = []

while len(tmp) != 6:
    num = randint(1,45)
    if num in tmp:
        continue
    else:
        tmp.append(num)

print('행운의 로또번호 :', end='')

for i in range(len(tmp) - 1):
    print(tmp[i], end=',')

print(tmp[len(tmp) - 1])