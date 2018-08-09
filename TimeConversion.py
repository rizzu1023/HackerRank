def timeConversion(s):
	l=list(s)
	if(l[0]=='1' and l[1]=='2' and l[8]=='P'):
		del l[8:10]
		return "".join(l)
	if(l[0]=='1' and l[1]=='2' and l[8]=='A'):
		l[0]='0'
		l[1]='0'
		del l[8:10]
		return "".join(l)
	if(l[8]=='P'):
		h=int(l[0]+l[1])
		h+=12
		hh=str(h)
		del l[0]
		l[0]=hh
		del l[7:9]
		return "".join(l)		
	if(l[8]=='A'):
		del l[8:10]
		return "".join(l)
