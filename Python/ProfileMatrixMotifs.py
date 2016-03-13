#  -----------------------------------------------------------------
#  File Name	:ProfileMatrixMotifs.py
#  DEVELOPER	:Victor Frankenstein (Banerjee)
#  Email		:<recervictory@gmail.com>
#  Date			:2016-03-06
#  
#  
#  Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
#  -----------------------------------------------------------------

import numpy as np

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna,zero_prob_adj=True):
    # insert your code here
    motifs=[]
    k= len(Profile)
    for dna in Dna:
		most_prob_kmer=find_most_prob_kmer_based_on_prof_mtrx(dna, k, prof_mtrx, zero_prob_adj)
		motifs.append(most_prob_kmer)
    return motifs

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
def find_most_prob_kmer_based_on_prof_mtrx(DNA_str, k, profile_matrix, zero_prob_adj=True):
    k = len(profile_matrix[0])
    n_iter = len(DNA_str) - k + 1
    most_prob_kmer = ''
    max_prob = 0

    if zero_prob_adj:
        profile_matrix = np.array(profile_matrix) + 1
        profile_matrix = profile_matrix.tolist()
    for i in range(0, n_iter):
        kmer = DNA_str[i:i+k]
        kmer_prob = get_kmer_prob_based_on_prof_mtrx(kmer, profile_matrix)
        if kmer_prob > max_prob:
            max_prob = kmer_prob
            most_prob_kmer = kmer
    return most_prob_kmer

def get_kmer_prob_based_on_prof_mtrx(kmer, profile_matrix):
	k = len(kmer)
	prob = 1
	for i in range(0, k):
		nuc = kmer[i]
		if nuc=='A':
			row = profile_matrix[0]
		elif nuc=='C':
			row = profile_matrix[1]
		elif nuc=='G':
			row = profile_matrix[2]
		else:
			row = profile_matrix[3]
		prob *= row[i]
	return prob


import sys
lines = sys.stdin.read().splitlines()
A = [float(c) for c in lines[0].split()]
C = [float(c) for c in lines[1].split()]
G = [float(c) for c in lines[2].split()]
T = [float(c) for c in lines[3].split()]
Profile = {'A':A,'C':C,'G':G,'T':T}
Dna = lines[4:]
print('\n'.join(Motifs(Profile,Dna)))

