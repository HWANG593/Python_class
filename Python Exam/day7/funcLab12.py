def myprint(*p1,**p2):
    if len(p1) == 0:
        print('Hello Python')

    else:
        # deco = p2.get('deco','**')  p2에서 deco를 갖고오지만, 없다면 '**'
        # sep = p2.get('sep',',')     p2에서 sep을 갖고오지만 , 없다면 ','

        deco = '**'
        sep = ','

        if 'deco' in p2.keys():
            deco = p2['deco']
        if 'sep' in p2.keys():
            sep = p2['sep']

        print(deco,end='')
        print(*p1,sep=sep,end='')
        print(deco)


myprint(10,20,30,deco='@',sep='-')
myprint('python','Javascript','R',deco='$')
myprint('가','나','다')
myprint(100)
myprint(True,111,False,'abc',deco='&',sep='')
myprint()