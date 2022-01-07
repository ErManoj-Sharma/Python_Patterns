n=5
for i in range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        if(j==i or i+j==n-1):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()
print()