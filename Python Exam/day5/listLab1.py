listnum = [10,5,7,21,4,8,18]
largest = listnum[0]

for i in listnum:
    if i > largest:
        largest = i

print('최댓값 :',largest)