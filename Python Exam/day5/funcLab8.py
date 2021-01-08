def print_triangle_withdeco(num,deco):
    if 1<=num<=10:
        for i in range(1,num+1):
            print((deco*i).rjust(num),sep='')

print_triangle_withdeco(5,'*')