multi3 = 0
multi15 = 0

for i in range(1,51):
    if i%3 ==0:
        multi3+=i

    if i%15 ==0:
        multi15+=i


print(multi3,multi15, multi3-multi15)