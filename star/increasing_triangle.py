n=5
# i\j 0 1 2 3 4
# 0   *
# 1   * *
# 2   * * *
# 3   * * * *
# 4   * * * * *

#method 1
# we see a pattern in which we print star only if j<=i ,
for i in range(n):
    for j in range(n):
        if(j<=i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#method 2
#we see pattern i.e.
# row : 0 , no of star print (column) : 1
# row : 1, no of star print (column) :2
# so row : i ,no of star print (column ): i+1
for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()

#3


