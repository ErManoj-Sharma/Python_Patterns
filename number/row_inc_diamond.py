#        1
#       2 2
#    3 3 3 3 3
#  4 4 4 4 4 4 4
#5 5 5 5 5 5 5 5 5
#  6 6 6 6 6 6 6
#    7 7 7 7 7
#      8 8 8
#        9


n=3
p=1
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(p, end=' ')
    for j in range(i):
        print(p, end=' ')
    p=p+1
    print()
for i in range(n):
    for j in range(n):
        if (j <= i):
                print(' ', end=' ')
        else:
                print(p, end=' ')

    for j in range(n - i):
        print(p, end=" ")
    p=p+1
    print()

# same modification will also work for butterfly code
# 1                   1
# 2 2               2 2
# 3 3 3           3 3 3
# 4 4 4 4       4 4 4 4
# 5 5 5 5 5 5 5 5 5 5 5
# 6 6 6 6       6 6 6 6
# 7 7 7           7 7 7
# 8 8               8 8
# 9                   9


p=1
for i in range(n-1):
        for j in range(i+1):
            print(p, end=' ')
        for j in range(i, n-1):  # range(n-i-1)
            print(" " , end=" ")
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(i + 1):
            print(p, end=' ')
        p=p+1
        print()
# decreasing triangle

for i in range(n):
    for j in range(n-i):
        print(p,end=" ")
    for j in range(n):
        if(j<i):
            print(" ",end=" ")
    for j in range(n+1):
        if(j<=i):
            if(i==0 and j==0):
                print(p,end=' ')
            else:
                print(" ",end=" ")
        else:
            print(p,end=' ')

    p=p+1
    print()
print()
