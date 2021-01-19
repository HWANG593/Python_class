import calendar

try:
    while True:
        ym = input('년도와 달을 입력해주세요 예)2019_03 :')
        y = ym.split('_')[0]
        m = ym.split('_')[1]
        print(calendar.month(int(y),int(m)))
        break

except ValueError:
    print('조건에 맞게 입력해 주세요.')
