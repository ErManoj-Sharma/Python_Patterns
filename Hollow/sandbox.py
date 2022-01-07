n=5
for i in range(n-1):
    for j in range(n):
        if(i==j or i==0):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    for j in range(n):
        if(i+j==n-1 or i==0):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()
for i in range(n):
    for j in range(n):
        if(i+j==n-1 or i==n-1):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    for j in range(n):
        if(i==j or i==n-1):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print()