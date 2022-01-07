n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1): # range(n-i-1)
        print("*",end=" ")
    for j in range(n-i):   # range (i,n)
        print("*", end=" ")
    print()

print()
for i in range(n):
    for j in range(n ):
        if (j <= i):
                print(' ', end=' ')
        else:
                print('*', end=' ')
    for j in range(n):
        if (j>=i):
            print('*', end=' ')

    print()
print()
# special type
for i in range(n):
    for j in range(n-i):

        if(j<i):
            print(" ",end=' ')
        else:
            print("*",end=' ')

    print()
print()




