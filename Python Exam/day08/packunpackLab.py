listv3 = ['p','y','t','h','o','n']

v1,v2,v3,v4,v5,v6 = listv3
# 동적 변수 할당
for i in range(len(listv3)):
    globals()['v{}'.format(i+1)] = listv3[i]

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

print(*listv3)
print(listv3)