# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
	# your code here
	dist_count=0
	for i in range(len(p)):
		if p[i] != q[i]:
			dist_count+=1
	return dist_count

seq1="CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
seq2="CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
print(HammingDistance(seq1,seq2))
