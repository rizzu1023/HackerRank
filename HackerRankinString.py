def hackerrankInString(s):
    # Complete this functio
    h='hackerrank'
    score=0
    k=-1
    for i in range(len(h)):
        for j in range(k+1,len(s)):
            if(h[i]==s[j]):
                k=j
                score+=1
                break
    if(score>=10):
        return 'YES'
    else:
        return 'NO'
