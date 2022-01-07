n=5

#1
for i in range(n-1,-1,-1):
    for j in range(i+1):   # we can write range as range(0,i+1)
        if(j<=i):
            print(" ", end=" ")
    for j in range(n-i):
        print('*', end=' ')

    print()
print()
#2

for i in range(n):
    for j in range(i,n):       # range can be written as range (n-i)
        print("$",end=" ")
    for j in range(n):
        if(j<=i):
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*', end=' ')

    print()
