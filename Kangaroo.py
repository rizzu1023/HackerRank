def kangaroo(x1, v1, x2, v2):
    # Complete this function
    t1,t2=0,0
    
    if(v2>v1 and x2>x1):
        return 'NO'
    while(t1!=t2 or x1!=x2):
        x1=x1+v1
        t1+=1
        x2=x2+v2
        t2+=1
        if(x2>=20000000 or x1>=20000000):
            return 'NO'
    return 'YES'
