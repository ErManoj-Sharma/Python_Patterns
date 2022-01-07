n=3
# increasing triangle
for i in range(n-1):
        for j in range(i+1):
            print('*', end=' ')
        for j in range(i, n-1):  # range(n-i-1)
            print(" " , end=" ")
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(i + 1):
            print('*', end=' ')

        print()
# decreasing triangle
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n):
        if(j<i):
            print(" ",end=" ")
    for j in range(n+1):
        if(j<=i):
            if(i==0 and j==0):
                print('*',end=' ')
            else:
                print(" ",end=" ")
        else:
            print('*',end=' ')

    print()
print()
