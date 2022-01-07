# rules to create number pattern
# 1 create pattern first
# 2 then enter no
# it means use different logic for pattern and number
# don't use index for no , it may leads error and confusion

s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p=p-1
    print()
print()

p=n-1
for i in range(n):
    for j in range(n-i):
        print(s[p],end=" ")
    p = p - 1
    print()
print()
p=n-1
for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(n-i):
        print(s[p],end=" ")
    p = p - 1
    print()
print()
p=n-1
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for i in range(i+1):
        print(s[p],end=" ")
    p = p - 1
    print()
print()
p=n-1
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for i in range(i+1):
        print(s[p],end=" ")
    for j in range(i):
        print(s[p], end=' ')
    p = p - 1
    print()
print()

p=n-1
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(' ',end=" ")
    for i in range(i+1):
        print(s[p],end=" ")
    for j in range(i):
        print(s[p], end=' ')
    p = p - 1
    print()
print()
# and all other star  pattern  replce * with number