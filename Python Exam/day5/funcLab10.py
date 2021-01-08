def sumAll(*a):
    sumnum = []

    for i in range(len(a)):
        if type(a[i])!=int and type(a[i])!=float:
            continue
        else:
            sumnum.append(a[i])

    if len(sumnum) == 0:
        return None
    else:
        return sum(sumnum)


print(sumAll(1,3,2243,'a','t','asfags','#'))