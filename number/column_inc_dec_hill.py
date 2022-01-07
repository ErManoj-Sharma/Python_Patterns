n=5
for i in range(n-1,-1,-1):
    p=1
    for j in range(n-1):
        if(j<i):
            print(" ",end=' ')
        else:
            print(p,end=' ')
            p=p+1
    for j in range(n-i):
        print(p,end=' ')
        p=p-1
    print()