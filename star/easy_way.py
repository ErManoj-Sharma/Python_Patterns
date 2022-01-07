n=5
# increasing triangle
for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()
print()

# decreasing triangle
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
print()

#right triangle
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*', end=' ')

    print()
print()
#left trinangle
for i in range(n):
    for j in range(n+1):
        if(j<=i):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n+1):
        if(j<i):
            print(' ',end=' ')
    for j in range(n+1):
        if(j<=i):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
print()
for i in range(n):
    for j in range(n):
        if (j <= i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i + 1):
        print('*', end=' ')

    print()
print()