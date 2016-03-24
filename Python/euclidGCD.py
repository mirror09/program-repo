def euclidGCD(a,b):
	while (b != 0):
		print a,b
		a , b = b , a % b
	return a

print euclidGCD(315770789798798798,11)
