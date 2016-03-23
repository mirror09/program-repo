def fizzbuzz(n):
	
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def print_fizzbuzz(limit):
	return "\n".join(fizzbuzz(n) for n in xrange(1, limit+1))


def print_fizzbuzz_times(n,seq):
	for i in range(n):
		fo = open('Output/fuzzbuzz.txt', 'wb')
		fo.write(print_fizzbuzz(seq[i]))
		print print_fizzbuzz(seq[i])
	return 0

with open('Input/fuzzbuzz.txt', 'r') as f:
    lines = f.readlines(1)
listed=[]
line =lines[1]
for u in line.split(' '):
    listed.append(int(u))
    
nth=int(lines[0][:-1])
print_fizzbuzz_times(nth,listed)



