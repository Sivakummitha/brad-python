n = 5
for i in range(n):
    for j in range(1+i):
        print('', end='')
    for j in range(i,n):
        print('*', end=' ')
    print()