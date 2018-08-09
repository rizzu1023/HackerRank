def findDigits(n):
    # Complete this function
    s=str(n)
    v=0
    for i in s:
        i=int(i)
        try:
            if(n%i==0):
                v+=1
        except:
            pass
    return v
