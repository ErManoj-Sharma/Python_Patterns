# if we have pattern like
# 1             # # # # #       a
# 2 2           $ $ $ $       b b b
# 1 1 1         # # #       a a a a a
# 2 2 2 2       $ $       b b b b b b b
# 1 1 1 1 1     #       a a a a a a a a a

# here in odd rows we have 1,#,a and in even rows we have 2,$,b
n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print(1,end=' ')
        else:
            print(2,end=' ')
    print()
print()

for i in range(n):
    for j in range(n-i):
        if(i%2==0):
            print('#',end=' ')
        else:
            print('$',end=' ')
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

