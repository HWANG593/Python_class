from random import *

oper_num = randint(1,10)

if oper_num == 1 or oper_num == 6:
    print('300+50 = ',300+50)

elif oper_num == 2 or oper_num == 7:
    print('300-50 = ', 300-50)

elif oper_num == 3 or oper_num == 8:
    print('300*50 = ', 300*50)

elif oper_num == 4 or oper_num == 9:
    print('300/50 = ', 300/50)

else:
    print('300%50 = ', 300%50)