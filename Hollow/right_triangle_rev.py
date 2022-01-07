n=5
for i in range(5):
    for j in range(i,n):
        if(i==j or i==0 or j==n-1 ):
            print("*",end='  ')
        else:
            print(' ',end='  ')
    print()
