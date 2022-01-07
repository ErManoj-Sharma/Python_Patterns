# rules to create number pattern
# 1 create pattern first
# 2 then enter no
# it means use different logic for pattern and number
# don't use index for no , it may leads error and confusion
n=5
p='A'
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    print()
print()


for i in range(n):
    for j in range(n-i):
        print(p,end=" ")
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(n-i):
        print(p,end=" ")
    print()
print()

for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for i in range(i+1):
        print(p,end=" ")
    print()

# and all other star  pattern  replce * with number