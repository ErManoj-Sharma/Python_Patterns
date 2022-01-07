n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end='  ')
    for j in range(i+1):
        if(i==n-1 or j==i or j==0 ):
            print("*",end='  ')
        else:
            print(' ',end='  ')

    print()