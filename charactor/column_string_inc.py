
s="CODER"
n=len(s)

for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=' ')
        p=p+1
    print()
print()

for i in range(n):
    p=0
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(n-i):
        print(s[p],end=' ')
        p=p+1
    print()

print()
for i in range(n):
    p=0
    for j in range(n-i):
        print(' ',end=" ")
    for i in range(i+1):
        print(s[p],end=" ")
        p+=1
    print()
print()
for i in range(n-1,1,-1):
    p=0
    for j in range(n-1):
        if(j<i):
            print(" ",end=' ')
        else:
            print(s[p],end=' ')
            p=p+1
    for j in range(n-i):
        print(s[p],end=' ')
        p=p+1
    print()