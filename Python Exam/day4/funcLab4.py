def print_triangle(a):
    if 1 <= a <= 10:
        for i in range(1,a+1):
            print('*'*i)
    else:
        return

print_triangle(4)