def count_substring(string, sub_string):
    count=0
    strg=''
    for i in range(0,len(string)):
        if(len(string)-i>=len(sub_string)):
            for j in range(i,i+len(sub_string)):
                strg=strg+string[j]
            if (strg==sub_string):
                count+=1
            strg=''
    return count

