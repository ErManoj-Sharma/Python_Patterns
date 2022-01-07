n=3
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()

print()


for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(n):
        if(j<=i):
            print("&",end=" ")
    for j in range(n):
        if(j<i):
            print("#",end=" ")


    print()