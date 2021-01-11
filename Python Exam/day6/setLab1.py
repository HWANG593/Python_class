from random import *

a = set()
b = set()

while len(a) < 10:
    a.add(randint(1,20))

while len(b) < 10:
    b.add(randint(1,20))

print('집합 1 :',a,'\n','집합 2:',b,'\n','두 집합에 모두 있는 데이터',a&b)
print('집합1 또는 집합2에 있는 데이터',a|b)
print('집합 1에는 있고 집합 2에는 없는 데이터',a-b)
print('집합 2에는 있고 집합 1에는 없는 데이터',b-a)
print('집합 1과 집합 2가 각자 가지고 있는 데이터',a^b)