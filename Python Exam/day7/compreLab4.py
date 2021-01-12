from random import *

tmp_list = [randint(1,100) for _ in range(10)]
print(tmp_list)

dic_score = {i+1:'pass' if tmp_list[i]>=60 else 'nopass' for i in range(len(tmp_list))}
print(dic_score)