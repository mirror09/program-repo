#  -----------------------------------------------------------------
#  File Name	:GreedyMotifSearch.py
#  DEVELOPER	:Victor Frankenstein (Banerjee)
#  Email		:<recervictory@gmail.com>
#  Date			:2016-02-26
#  
#  
#  Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
#  -----------------------------------------------------------------

# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
def Profile(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	profile = {}
    # insert your code here
	for symbol in "ACGT": #COUNT FOR EACH SYMBOL A C G T
		profile[symbol]=[]
		for i in range(k):
			profile[symbol].append(0) 
	for i in range(t):
		for j in range(k):
			symbol = Motifs[i][j]
			profile[symbol][j] += 1/t
	return profile

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

def Score(Motifs):
	# Insert code here
	consensus=Consensus(Motifs)
	count= Count(Motifs)
	k =len(consensus)
	j= len(count)
	t=len(Motifs)
	mscore =0
	score =-1
	for i in range(k):
		mscore= t - count[consensus[i]][i]
		score+=mscore
	return score

# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
	matchmax=0
	ProbablePattern=""
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		if Pr(Pattern, Profile) > matchmax:
			matchmax=Pr(Pattern, Profile)
			ProbablePattern=Pattern
	return ProbablePattern

def Pr(Text, Profile):
    # insert your code here
	pr=1
	for i in range(len(Text)):
		pr*=Profile[Text[i]][i]
	return pr

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
	# type your GreedyMotifSearch code here.
	BestMotifs = []
	for i in range(0, t):
		BestMotifs.append(Dna[i][0:k])
	n = len(Dna[0])
	for i in range(n-k+1):
		Motifs = []
		Motifs.append(Dna[0][i:i+k])
		for j in range(1, t):
			P = Profile(Motifs[0:j])
			Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs

with open('stepic.txt') as input_data:
	k, t = map(int, input_data.readline().split())
	dna_list = [line.strip() for line in input_data]
	print('\n'.join(GreedyMotifSearch(dna_list, k, t)))

