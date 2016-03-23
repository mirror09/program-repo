'''
Problem:
		Given an array of integers inputArray and an integer bound, 
		find the smallest array element strictly greater than bound.
		inputArray = [1, 3, 5, 4, 2, 6] and bound = 3, the output should be 4.
		
		https://codefights.com/task/kaAbSQQP3ioXQk3Nk
'''


def arrayMinimumAboveBound(inputArray, bound):

	best = -1
	for i in range(len(inputArray)):
		if inputArray[i] > bound and (best == -1 or inputArray[i] < best):
			best = inputArray[i]
	return best


print arrayMinimumAboveBound([1, 3, 5, 4, 2, 6],3)
print arrayMinimumAboveBound([1, 4, 10, 5, 2],1)
