    def sumEven1(*a):
        total = 0
        if len(a) == 0:
            return -1

        for i in range(len(a)):
            if a[i] >= 1:
                if a[i]%2 == 0:
                    total += a[i]
            else:
                return -1
        return total


    print(sumEven1(2,7,1,3))