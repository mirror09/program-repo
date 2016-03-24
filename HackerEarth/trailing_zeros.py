def trailing_zeros(n):
	zero=0
	f=5
	while not(n /5 ==0):
		f=f*5
		zero+=n/5
		n=n/5
	return zero

print trailing_zeros(17)
