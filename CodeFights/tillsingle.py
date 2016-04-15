#

def tillsingle(n):
	n=n.split("^")+[1]
	print n
	n=int(n[0])**int(n[1])   
	print n 
	return n and (n % 9 or 9)
    
print(tillsingle('123243'))
