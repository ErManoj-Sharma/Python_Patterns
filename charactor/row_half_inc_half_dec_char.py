#          1
#        2 2 2
#      3 3 3 3 3
#    4 4 4 4 4 4 4
#  5 5 5 5 5 5 5 5 5
#    4 4 4 4 4 4 4
#      3 3 3 3 3
#       2 2 2
#          1

# till now , our row are same but what if our column are same

n=3
p=65
for i in range(n-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p), end=' ')
    for j in range(i):
        print(chr(p), end=' ')
    p=p+1                           # increasing value for first half
    print()
for i in range(n):
    for j in range(n):
        if (j <= i):
                print(' ', end=' ')
        else:
                print(chr(p), end=' ')
    for j in range(n - i):
        print(chr(p), end=" ")
    p=p-1                           # decresing values for second half
    print()
print()


#
# same logic for butterfly pattern
#
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

    p=p-1
    print()
print()

