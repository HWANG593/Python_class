a = [['B','C','A','A'],
     ['C','C','B','B'],
     ['D','A','A','D']]

b = ['A','B','C','D']

for i in range(len(b)):
    count = 0
    for j in range(len(a)):
        count += a[j].count(b[i])
    print(b[i],'는',count,'개 입니다.')