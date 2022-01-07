s="PROGRAM"
n=len(s)

for i in range(n):
    p=n-1
    for j in range(i+1):
        print(s[p],end=' ')
        p=p-1
    print()
print()

# important program uderstand use of k,p
k=n-1
for i in range(n):
    p=k
    for j in range(n):
        if(j<i):
            print(" ",end=' ')
        else:
            print(s[p],end=' ')
            p=p-1
    k=k-1
    print()