n=5

# i\j 0 1 2 3 4
#  0  * * * * *
#  1  * * * *
#  2  * * *
#  3  * *
#  4  *

# method 1 :
# in row 0 , no of star print (column ):5(5-0)
# in row 1 , no of star print (column ):4(5-1)
# in row 2 , no of star print (column ):3(5-2)
# in row i , no of star print (column ):n-i
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

#method 2:

# i\j 4 3 2 1 0
#  4  * * * * *
#  3  * * * *
#  2  * * *
#  1  * *
#  0  *
# we just change numbering  of rows,column no we can see
# for row no 4 , column are 0,1,2,3,4 (i.e range (4+1))
# for row no 3 , column are 0 1,2,3 ( i.e range(3+1))
# for row no 2 , column are 0,1,2    ( i.e range(2+1))
# so for row no i , column are 0,i (i.e range(i+1))
# so range is shrinking for j as i is increasing
# so ,     if j<=i then print *
for i in range(n-1,-1,-1):
    for j in range(i+1):   # we can write range as range(0,i+1)
        if(j<=i):
            print("*", end=" ")
    print()


for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()


for i in range(n-1,-1,-1):
    for j in range(n):
        if(j<=i):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()