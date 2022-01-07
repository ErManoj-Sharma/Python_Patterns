n=3
# increasing triangle
for i in range(n-1):
        for j in range(i+1):
            print('*', end=' ')
        print()
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")

    print()
print()
