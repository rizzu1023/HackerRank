def plusMinus(arr):
    n,p,z=0,0,0
    for i in range(0,len(arr)):
        if(arr[i]>0):
            p+=1
        if(arr[i]<0):
            n+=1
        if(arr[i]==0):
            z+=1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))
