n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end='  ')
    for j in range(n-i):
        if(i==0 or j==0 or i+j==n-1):
            print('*',end='  ')
        else:
            print(' ',end='  ')
    print()