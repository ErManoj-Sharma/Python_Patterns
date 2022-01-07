#    1 2 3 4 5
#      1 2 3 4
#        1 2 3
#          1 2
#            1
n=5
for i in range(n):
    p=1
    for j in range(n-i):

        if(j<i):
            print(" ",end=' ')
        else:
            print(p,end=' ')
            p=p+1
    print()
print()

for i in range(n):
    p=1
    for j in range(n):

        if(j<i):
            print(" ",end=' ')
        else:
            print(p,end=' ')
            p=p+1
    print()
print()
# same program
for i in range(n):
    p=1
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(n-i):        # (i,n) or  we can write  (n-i)
        print(p,end=' ')
        p=p+1
    print()
print()