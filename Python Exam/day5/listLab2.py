listnum = [10,5,7,21,4,8,18]
smallest = listnum[0]

for i in listnum:
    if i < smallest:
        smallest = i

print('최솟값 :'smallest)