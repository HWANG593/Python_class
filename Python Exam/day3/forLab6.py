multi3=0

for i in range(1,51):
    if i%3 == 0:
        if i % 15 == 0:
            continue
        else:
            multi3+=i

print(multi3)
