def camelcase(s):
    v=1
    for i in s:
        if(i.isupper()):
            v+=1
    return v
