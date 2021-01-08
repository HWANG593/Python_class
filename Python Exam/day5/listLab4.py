from random import *

listnum = []

for i in range(10):
    listnum.append(randint(1,50))

print(listnum)

for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] = 100

print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[::])
del listnum[4]
print(listnum[::])
del listnum[1:3]
print(listnum[::])