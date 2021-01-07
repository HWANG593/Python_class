import math

while True:
    num = int(input('숫자를 입력해 주세요 : '))

    if num == 0:
        print('종료')
        break
    elif num < -10 or num > 10:
        continue
    elif num > 0 and num <= 10:
        print(math.factorial(num))

    elif num<0 and num> -10:
        print(math.factorial(-num))

