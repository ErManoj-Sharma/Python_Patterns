# A B C D E
#   A B C
#     A
#
#
#
# A B C D E
#   A B C D
#     A B C
#       A B
#         A
#
#   A B C D E
#     A B C D
#       A B C
#         A B
#           A
n=5
for i in range(n):
    p=65
    for j in range(n-i):

        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p+1
    print()
print()

for i in range(n):
    p=65
    for j in range(n):

        if(j<i):
            print(" ",end=' ')
        else:
            print(chr(p),end=' ')
            p=p+1
    print()
print()
# same program
for i in range(n):
    p=65
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(n-i):        # (i,n) or  we can write  (n-i)
        print(chr(p),end=' ')
        p=p+1
    print()
print()