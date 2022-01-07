# if we have pattern like
# a             z z z z z        a
# b b           0 0 0 0        b b b
# a a a         z z z        a a a a a
# b b b b       0 0        b b b b b b b
# a a a a a     z        a a a a a a a a a

# here in odd rows we have 1,#,a and in even rows we have 2,$,b
n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print('a',end=' ')
        else:
            print('b',end=' ')
    print()
print()

for i in range(n):
    for j in range(n-i):
        if(i%2==0):
            print('z',end=' ')
        else:
            print('0',end=' ')
    print()
print()
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i+1):
        if(i%2==0):
            print('a',end=' ')
        else:
            print('b',end=' ')
    for j in range(i):
        if(i%2==0):
            print('a',end=' ')
        else:
            print('b',end=' ')
    print()

