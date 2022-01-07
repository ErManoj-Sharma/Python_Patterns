n=5

for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(n):
        if (j <= i):
                print(' ', end=' ')
        else:
                print('*', end=' ')
    for j in range(n - i):
        print("*", end=" ")
    print()

