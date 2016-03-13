# Insert your Count(Motifs) function here from the last Code Challenge.

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
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

with open('CountWithPseudocounts.txt') as input_data:
	dna_list = [line.strip() for line in input_data]
	print(Profile(dna_list))
