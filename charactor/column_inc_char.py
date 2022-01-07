# A
# A B
# A B C
# A B C D
# A B C D E
#
#   A B C D E
#     A B C D
#       A B C
#         A B
#           A
#
#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I
# in this kind of pattern column are same but row are changing so we write condition in inner loop only


n=5
for i in range(n):
    p=65
    for j in range(i+1):
        print(chr(p),end=' ')
        p=p+1
    print()
print()

for i in range(n):
    p=65
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(n-i):
        print(chr(p),end=' ')
        p=p+1
    print()

print()

for i in range(n-1,-1,-1):
    p=65
    for j in range(n-1):
        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p+1
    for j in range(n-i):
        print(chr(p),end=' ')
        p=p+1
    print()