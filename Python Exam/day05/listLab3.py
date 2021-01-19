listnum = [10,5,7,21,4,8,18]

largest = listnum[0]
smallest = listnum[0]

for i in listnum:
    if i > largest:
        largest = i

for i in listnum:
    if i < smallest:
        smallest = i

print('최솟값 :',smallest,',','최댓값 :',largest)