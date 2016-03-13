#  -----------------------------------------------------------------
#  File Name	:CountWithPseudocounts.py
#  DEVELOPER	:Victor Frankenstein (Banerjee)
#  Email		:<recervictory@gmail.com>
#  Date			:2016-02-28
#  
#  
#  Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
#  -----------------------------------------------------------------


def CountWithPseudocounts(Motifs):
	count = {} # initializing the count dictionary
    # your code here
	t = len(Motifs)
	k = len(Motifs[0])
	for symbol in "GACT":
		count[symbol]=[]
		for i in range(k):
			count[symbol].append(1) #set value as zero 
	for i in range(t):
		for j in range(k):
			symbol = Motifs[i][j]
			count[symbol][j] += 1
	return countC	

def ProfileWithPseudocounts(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	profile = {} # output variable
    # your code here
	count=CountWithPseudocounts(Motifs)
	for symbol in "GACT":
		profile[symbol]=[]
		for i in range(k):
			profile[symbol].append(float(float(count[symbol][i])/float(t+4))) #set value as zero
	return profile


 
with open('CountWithPseudocounts.txt') as input_data:
	dna_list = [line.strip() for line in input_data]
	print(ProfileWithPseudocounts(dna_list))
