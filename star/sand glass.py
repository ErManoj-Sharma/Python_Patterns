n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1): # range(n-i-1)
        print("*",end=" ")
    for j in range(n-i):   # range (i,n)
        print("*", end=" ")
    print()


for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()

print()