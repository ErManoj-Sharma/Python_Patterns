n=5
m=n-5
for i in range(n):
    p=69+m
    for j in range(i+1):
        print(chr(p),end=' ')
        p=p-1
    print()
print()

# important program uderstand use of k,p
k=69+m
for i in range(n):
    p=k
    for j in range(n):
        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p-1
    k=k-1
    print()