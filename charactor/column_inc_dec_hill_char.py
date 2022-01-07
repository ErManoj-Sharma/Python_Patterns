n=5
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
        p=p-1
    print()
print()
for i in range(n-1,-1,-1):
    p=69
    for j in range(n-1):
        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p-1
    for j in range(n-i):
        print(chr(p),end=' ')
        p=p+1
    print()
print()

for i in range(n-1,-1,-1):
    p=65
    for j in range(n-1):
        if(j<i):
            print(' ',end=' ')
            p=p+1
        else:
            print(chr(p),end=' ')
            p=p+1
    for j in range(n-i):
        print(chr(p),end=' ')
        p=p-1
    print()
print()

