
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        if(i==n-1 or j==0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(i+1):
        if(i==n-1  or j==i ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print()
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1): # range(n-i-1)
        if(i==0 or j==i):
            print("*",end=" ")
        else:
            print(' ',end=' ')
    for j in range(n-i):   # range (i,n)
        if (i == 0 or i+j==n-1):
            print("*", end=" ")
        else:
            print(' ', end=' ')
    print()
