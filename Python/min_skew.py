# Input:  A String Genome
# Output: Skew(Genome)
def MinimumSkew(Genome):
	positions = [] # output variable
	# your code here
	skew=Skew(Genome)
	minskew = min(skew.values())
	for j in range(1,len(skew)):
		if skew[j] == minskew:
			positions.append(str(j))
	return positions  



def Skew(Genome):
	skew = {}
	count =0
	skew[0] =count
	for i in range(1,(len(Genome)+1)):
		if(Genome[i-1]=='G'):
			count=count+1
			skew[i] =count
		elif(Genome[i-1]=='C'):
			count=count-1
			skew[i] =count
		elif(Genome[i-1]=='A'):
			skew[i] =count
		elif(Genome[i-1]=='T'):
			skew[i] =count
	return skew
Genome= "CATTCCAGTACTTCGATGATGGCGTGAAGA"
print(MinimumSkew(Genome))
print(Skew(Genome))
