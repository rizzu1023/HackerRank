def mouseCat(a,b,c):
	if(a<b<c or c<b<a):
		return 'Cat B'
	elif(b<a<c or c<a<b):
		return 'Cat A'
	elif(a==b):
		return 'Mouse C'
	else:
		ca,cb=0,0
		if(a<c):
			for i in range(a+1,c+1):
				ca+=1
		else:
			for i in range(a-1,c-1,-1):
				ca+=1
		if(b<c):
			for j in range(b+1,c+1):
				cb+=1
		else:
			for j in range(b-1,c-1,-1):
				cb+=1
	if(ca<cb): 
		return 'Cat A'
	elif(ca==cb): 
		return 'Mouse C'
	else:
	    return 'Cat B'

