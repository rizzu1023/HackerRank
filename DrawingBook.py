def solve(n, p):
    front,back=0,0
    for i in range(1,p,2):
        front+=1
    if(n%2==0):
         for j in range(n+1,p+1,-2):
                back+=1
    else:
         for j in range(n,p+1,-2):
                back+=1
    if(front<back):
        return front
    else:
        return back

