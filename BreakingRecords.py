def breakingRecords(score):
    h,l=0,0
    high=score[0]
    low=score[0]
    for i in range(0,len(score)):
        if(score[i]>high):
            h+=1
            high=score[i]
        if(score[i]<low):
            l+=1
            low=score[i]
    return h,l
