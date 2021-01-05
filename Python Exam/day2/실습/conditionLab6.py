from random import *

score = randint(0,100)

if score >= 90:
    grade = 'A'

elif score >=80 and score<90:
    grade = 'B'

elif score >=70 and score<80:
    grade = 'C'

elif score >=60 and score<70:
    grade = 'D'

else:
    grade = 'E'

print(score,'점은 ',grade,'등급입니다.')
