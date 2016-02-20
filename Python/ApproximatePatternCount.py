# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
	count = 0 # initialize count variable
    # your code here
	for i in range(len(Text) - len(Pattern)+1):
		if HammingDistance(Text[i:i+len(Pattern)], Pattern) <=d:
			count+=1
	return count

# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
	# your code here
	dist_count=0
	for i in range(len(p)):
		if p[i] != q[i]:
			dist_count+=1
	return dist_count
	
# Input
Pattern="ATTCTGGA"
Sequence="CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
integer = 3

print(ApproximatePatternCount(Pattern, Sequence, integer))

