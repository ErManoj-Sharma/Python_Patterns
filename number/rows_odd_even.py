#if we have patern like
#   0            1
#   2 2          3 3
#   4 4 4        5 5 5
#   6 6 6 6      7 7 7 7
#   8 8 8 8 8    9 9 9 9 9

# same logic can ce applied to other pattern

n=5
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p=p+2
    print()
print()


p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p=p+2
    print()
print()


