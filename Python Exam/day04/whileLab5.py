wordlength = 1

while wordlength!=0:
    word = input('문자열을 입력하세요: ')
    wordlength = len(word)
    if 5<=wordlength<=8:
        continue
    elif wordlength < 5:
        result = str('*')+word+str('*')
    elif wordlength > 8:
        result = str('$') + word + str('$')

    print('유효한 입력 결과 : ',result)