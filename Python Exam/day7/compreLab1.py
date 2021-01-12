def createList(*p,type = 1):
    if len(p) == 0:
        ans = [x for x in range(1,31)]
        return ans
    else:
        if type == 1:
            ans = [x for x in p]
            return ans
        if type == 2:
            ans = [x for x in p if x%2==0]
            return ans
        if type == 3:
            ans = [x for x in p if x%2==1]
            return ans
        if type == 4:
            ans = [x for x in p if x>10]
            return ans