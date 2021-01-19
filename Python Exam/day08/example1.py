score = [78,95,87,45,12]

for i,v in enumerate(score,1):
    print(i)        # i 는 인덱스 기본값 0부터 시작
    print(v)        # score[0]부터 순서대로


yoil = ['월','화','수','목','금','토','일']
food = ['갈비탕','순대국','칼국수','삼겹살']
menu = zip(yoil,food)

def flunk(s):
    return s<60     #반드시 return 값이 부울형이여야한다.

score = [45,89,72,53,94]
for s in filter(flunk,score):   # flunk에 score 인자가 들어가서 true면 s로 전달
    print(s)

def half(s):
    return s/2

score = [45,89,72,53,94]
for s in map(half,score):   # half 함수에 score 먼저 돌린 후 s로 전달
    print(s)

score = [45,89,72,53,94]
for s in filter(lambda x:x<60,score):
    print(s)

a = lambda x:x+1
a(score[0])

import time

t = time.time()
print(time.ctime(t))

a = 3
b = a
print(a,b)