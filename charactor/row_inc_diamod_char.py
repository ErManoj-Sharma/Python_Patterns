#       A
#     B B B
#   C C C C C
#     D D D
#       E


n=3
p=65
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p), end=' ')
    for j in range(i):
        print(chr(p), end=' ')
    p=p+1
    print()
for i in range(n):
    for j in range(n):
        if (j <= i):
                print(' ', end=' ')
        else:
                print(chr(p), end=' ')

    for j in range(n - i):
        print(chr(p), end=" ")
    p=p+1
    print()

# same modification will also work for butterfly code
# A           A
# B B       B B
# C C C C C C C
# D D       D D
# E           E

p=65
for i in range(n-1):
        for j in range(i+1):
            print(chr(p), end=' ')
        for j in range(i, n-1):  # range(n-i-1)
            print(" " , end=" ")
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(i + 1):
            print(chr(p), end=' ')
        p=p+1
        print()
# decreasing triangle

for i in range(n):
    for j in range(n-i):
        print(chr(p),end=" ")
    for j in range(n):
        if(j<i):
            print(" ",end=" ")
    for j in range(n+1):
        if(j<=i):
            if(i==0 and j==0):
                print(chr(p),end=' ')
            else:
                print(" ",end=" ")
        else:
            print(chr(p),end=' ')

    p=p+1
    print()
print()
