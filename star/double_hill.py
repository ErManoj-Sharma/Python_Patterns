n=3

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")                 # decreasing pattern(" ")
    for j in range(i+1):
        print('*', end=' ')                # right triangle    (*)
    for j in range(i):
        print('*', end=' ')                 # increasing triangle (*)

    for j in range(i,n-1):                  # left downword triangle (" ")
        print(" ", end=" ")
    for j in range(i,n-1):                  #right downword triangle(" ")
        print(" ", end=" ")
    for j in range(i+1):
        print('*', end=' ')                 #right triangle    (*)
    for j in range(i):
        print('*', end=' ')                    # # increasing triangle (*)
    print()
print()
