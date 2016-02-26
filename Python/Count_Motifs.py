#!/usr/bin/env python
#Sample Input: 	AACGTA
#				CCCGTT
#				CACCTT
#				GGATTA
#				TTCCGG
# k = length of each string --> 6
# j = number of string		--> 5
# matrix 5x6
#Sample Output: {	'A': [1, 2, 1, 0, 0, 2], 
#					'C': [2, 1, 4, 2, 0, 0], 
#					'G': [1, 1, 0, 2, 1, 1], 
#					'T': [1, 1, 0, 1, 4, 2]}
# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0]) #Motifs[0], the first string in Motifs, which is the length of every string in Motifs i.e AACGTA =6
		for symbol in "ACGT": #COUNT FOR EACH SYMBOL A C G T
			count[symbol]=[]
			for i in range(k):
				count[symbol].append(0) #set value as zero 
	t = len(Motifs)
	for i in range(t):
		for j in range(k):
			symbol = Motifs[i][j]
			count[symbol][j] += 1		
    return count
