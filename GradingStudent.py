def gradingStudents(marks):
    for i in range(0,len(marks)):
        if(marks[i]>=38):
            rm=marks[i]%5
            if(rm!=0):
                if(rm>2):
                    marks[i]=marks[i]+(5-rm)
    return marks
