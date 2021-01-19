from random import *

a = set()

while len(a)<6:
    a.add(randint(1,45))


print('행운의 로또번호 :',end='')

for i in range(len(a)-1):
    print(list(a)[i],end=',')

print(list(a)[len(a)-1])