dic = {'월':(-12,-3),'화':(-4,2),'수':(-8,8),'목':(-3,5),
       '금':(-7,7),'토':(-13,-3),'일':(-6,-2)}

a = input('요일명을 한글로 입력하세요:')

if a in dic.keys():
    print(a,'요일의 최저온도는',dic[a][0],'이고 최고 온도는',dic[a][1],'입니다.')
else:
    print(a,'요일의 정보를 찾을 수 없습니다.')