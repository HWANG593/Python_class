while True:
    month = int(input('숫자를 입력하세요: '))
    if month == 1 or month == 2 or month == 12:
        print(month,'월은 겨울')

    elif 3<=month<=5:
        print(month, '월은 봄')

    elif 6<=month<=8:
        print(month, '월은 여름')

    elif 9<= month <=11:
        print(month, '월은 가을')
    else:
        print('1~12 사이의 값을 입력하세요!')
        break