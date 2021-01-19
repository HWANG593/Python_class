class Member:
    def __init__(self):         #초기화 메서드에 아규먼트를 받지 않으면 각각 초기화 해줘야한다
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None


mem1 = Member()
mem2 = Member()
mem3 = Member()

mem1.name = '이철희'
mem1.account = 'kipers'
mem1.passwd = 123
mem1.birthyear = 1993

mem2.name = '최성욱'
mem2.account = 'kardinal'
mem2.passwd = 456
mem2.birthyear = 1991

mem3.name = '현재웅'
mem3.account = '미래웅'
mem3.passwd = 789
mem3.birthyear = 1996

print(f"회원1 : {mem1.name}({mem1.account},{mem1.passwd},{mem1.birthyear}")
print(f"회원2 : {mem2.name}({mem2.account},{mem2.passwd},{mem2.birthyear}")
print(f"회원3 : {mem3.name}({mem3.account},{mem3.passwd},{mem3.birthyear}")


print('회원 1:',mem1.name,'(',mem1.account,',',mem1.passwd,',',mem1.birthyear,')',sep='')
print('회원 2:',mem2.name,'(',mem2.account,',',mem2.passwd,',',mem2.birthyear,')',sep='')
print('회원 3:',mem3.name,'(',mem3.account,',',mem3.passwd,',',mem3.birthyear,')',sep='')

