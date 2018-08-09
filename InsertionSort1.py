def insertionSort1(n, arr):
    key=arr[-1]
    v=0
    for i in range(n-2,-1,-1):
        if(arr[i]>key):
            arr[i+1]=arr[i]
        else:
            arr[i+1]=key
            v+=1
            break

    
        for i in range(0,n):
            print("{} ".format(arr[i]),end='')
        print('\n',end='')
    if(v==0):
        arr[0]=key
    for i in range(0,n):
        print("{} ".format(arr[i]),end='')

