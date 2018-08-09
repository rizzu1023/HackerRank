def insertionSort2(n, arr):
    # Complete this function
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(key<arr[j] and j>=0):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        for i in range(0,n):
            print("{} ".format(arr[i]),end='')
        print("\n",end='')
