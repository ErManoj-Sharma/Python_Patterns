n=5
for i in range(n):
    for j in range(n+1):
        if(j<=i):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()


n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()


