import re
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
        u,l,d,c=0,0,0,0
        for s in password:
            if(s.isupper()):
                u=1
            if(s.islower()):
                l=1
            if(s.isdigit()):
                d=1
        if(re.search(r"\W",password)):
            c=1
        test=4-(c+u+l+d)
        if(n>=6):
            return test
        else:
            if(n<=3 or test==0 or test==1):
                return 6-n
            else:
                return test

