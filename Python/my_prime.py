
def is_prime(nbr):
	flag=True
	for i in range(2,nbr/2):
		if nbr % i ==0:
			flag=False
	return flag

def my_prime(n,lists):
	for i in range(n):
		if is_prime(lists[i]):
			print lists[i],
n=5
lst=[40,101,89,97,674]

my_prime(n,lst)
		
