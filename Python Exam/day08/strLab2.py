s1 = 'pythonjavascript'
print(len(s1))

s2 = '010-7777-9999'
tmp = s2.split('-')
print(''.join(tmp))

s3 = 'PYTHON'
print(s3[::-1])

s4 = 'Python'
print(s4.lower())

s5 = 'https://www.python.org'
tmp = s5.split('/')
print(tmp[-1])

s6 = '891022-3473837'
tmp = s6.split('-')
if tmp[1][0] == '1' or tmp[1][0] == '3':
    print('남자')
if tmp[1][0] == '2' or tmp[1][0] == '4':
    print('여자')

s7 = '100'
print(int(s7))
print(float(s7))

s8 = 'The Zen of Python'
print(s8.count('n'))
print(s8.index('Z'))
tmp = s8.upper()
print(tmp.split(' '))