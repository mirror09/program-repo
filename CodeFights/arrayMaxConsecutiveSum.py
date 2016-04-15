'''
Given array of integers, find the maximal possible sum of some of 
its k consecutive elements.

Example

for array = [2, 3, 5, 1, 6], k = 2 output should be 8

https://codefights.com/fight/z977iQjwnkWg739K7
'''
def arrayMaxConsecutiveSum(inputArray, k):

	result = 0
	currentSum = 0

	for i in range(k - 1):
		currentSum += inputArray[i]
		print currentSum
	for i in range(k - 1, len(inputArray)):
		currentSum += inputArray[i]
		print currentSum
	if currentSum > result:
		result = currentSum
		print result  
		currentSum -= inputArray[i - k + 1]

	return result
print "------"
print arrayMaxConsecutiveSum([2, 4, 10, 1], 2) #Expected 14
#print arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2) #Expected 8
print "------"
