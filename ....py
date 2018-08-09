def miniMaxSum(arr):
    s=sum(arr)
    res=[]
    for i in range(0,len(arr)):
        var=s-arr[i]
        res.append(var)
    print("{} {}".format(min(res),max(res)))
