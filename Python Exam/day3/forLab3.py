from random import *

X = randint(1,10)
Y = randint(30,40)

total = 0
for i in range(X,Y+1):
    if i%2 == 0:
        total = total+i

print('X 부터 Y 까지의 짝수의 합: ',total)