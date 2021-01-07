def print_gugudan(a):
    if type(a)== int:
        if 1 <= a <= 9:
            for i in range(1,10):
                print(a,'*',i,'=',a*i)


print_gugudan(5)