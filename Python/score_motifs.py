# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
	# insert your code here
	k = len(Motifs[0])
	count = Count(Motifs)
	consensus=""
	for j in range(k):
		m=0
		frequentSymbol = ""
		for symbol in "ACGT":
			if count[symbol][j] > m:
				m = count[symbol][j]
				frequentSymbol = symbol
		consensus+=frequentSymbol
	return consensus

  
# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
	count = {}
	# your code here
	k = len(Motifs[0])
	for symbol in "ACGT": 
			count[symbol]=[]
			for i in range(k):
				count[symbol].append(0)
	t = len(Motifs)
	for i in range(t):
		for j in range(k):
			symbol = Motifs[i][j]
			count[symbol][j] += 1
	return count
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    consensus=Consensus(Motifs)
    count= Count(Motifs)
    k =len(consensus)
    j= len(count)
    t=len(Motifs)
    mscore =0
    score =0
    for i in range(k):
        mscore= t - count[consensus[i]][i]
        score+=mscore
    return score
