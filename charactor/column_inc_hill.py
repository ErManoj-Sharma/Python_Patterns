n=3
for i in range(n-1,-1,-1):
    p=65
    for j in range(n-1):
        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p+1
    for j in range(n-i):
        print(chr(p),end=' ')
        p=p+1
    print()
print()

# with same logic we can print diamond & butter fly
for i in range(n-1):
        p=65
        for j in range(i+1):
            print(chr(p), end=' ')
            p=p+1
        for j in range(i, n-1):  # range(n-i-1)
            print(" " , end=" ")
        for j in range(i,n):
            print(" ", end=" ")
        p=65
        for j in range(i + 1):
            print(chr(p), end=' ')
            p=p+1

        print()
# decreasing triangle
for i in range(n):
    p=65
    for j in range(n-i):
        print(chr(p),end=" ")
        p=p+1
    for j in range(n):
        if(j<i):
            print(" ",end=" ")
    p=65
    for j in range(n+1):
        if(j<=i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p+1
    print()
print()

# diamond

for i in range(n-1):
    p=65
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p), end=' ')
        p=p+1
    for j in range(i):
        print(chr(p), end=' ')
        p=p+1
    print()
for i in range(n):
    p=65
    for j in range(n):
        if (j <= i):
                print(' ', end=' ')
        else:
                print(chr(p), end=' ')
                p=p+1
    for j in range(n - i):
        print(chr(p), end=" ")
        p=p+1
    print()
