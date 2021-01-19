a = [[10,12,14,16],
     [18,20,22,24],
     [26,28,30,32],
     [34,36,38,40]]

print(a[0][0])
print(a[2][3])
print(len(a))
print(len(a[0]))
print(a[2])

list2 = []
for i in range(len(a)):
    list2.append(a[i][1])
print(list2)

list3 = []
for i in range(len(a)):
    list3.append(a[i][i])
print(list3)

list4 = []
for i in range(len(a)):
    list4.append(a[i][3-i])
print(list4)