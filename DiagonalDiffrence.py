
def diagonalDifference(a):
    sum1=0
    sum2=0
    key=len(a)-1
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if(i==j):
                sum1+=a[i][j]
            if(j==key):
                sum2+=a[i][j]
            else:
                pass
        key-=1
    return abs(sum1-sum2)
       

