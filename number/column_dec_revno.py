n=5
for i in range(n):
    p=n
    for j in range(i+1):
        print(p,end=' ')
        p=p-1
    print()
print()

# important program uderstand use of k,p
k=n
for i in range(n):
    p=k
    for j in range(n):
        if(j<i):
            print(" ",end=' ')
        else:
            print(p,end=' ')
            p=p-1
    k=k-1
    print()