#  1             1 2 3 4 5               1
#  1 2           1 2 3 4               1 2 3
#  1 2 3         1 2 3               1 2 3 4 5
#  1 2 3 4       1 2               1 2 3 4 5 6 7
#  1 2 3 4 5     1               1 2 3  4 5 6 7 8 9
# in this kin of pattern column are same but row are changing so we write condition in inner loop only


n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p=p+1
    print()
print()

for i in range(n):
    p=1
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(n-i):
        print(p,end=' ')
        p=p+1
    print()

print()

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
        p=p+1
    print()