#if we have patern like
#   a            b
#   c c          d d
#   e e e        f f f
#   g g g g      h h h h
#   i i i i i    j j j j j

# same logic can ce applied to other pattern

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p=p+2
    print()
print()


p=66
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p=p+2
    print()
print()


