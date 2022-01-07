n=5

for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i):
        if(j==0):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    for j in range(i+1):
        if (j==i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        if (j==i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(i,n-1):
        if (j==n-2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()