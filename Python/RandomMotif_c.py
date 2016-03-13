'''
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) 1000 times.

from GreedyMotif import BuildProfilePseudo, _AMINO_INDEX_, ScoreMotifs
from ProfileMost import ProfileMost'''
from random import randint
from itertools import groupby as g

def MostCommon(L):
      return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]

def Prob(motif, amino_index, matrix):
    motif_len  = len(motif)
    total_prob = 1
    for i in range(motif_len):
        a_index = amino_index.index(motif[i])
        total_prob *= matrix[i][a_index]
    return total_prob

def ProfileMost(seq, k, amino_index, matrix):
    seq_len   = len(seq)
    prob_dict = dict()
    min_prob  = 0
    min_motif = seq[:k]
    for i in range(seq_len - k + 1):
        motif = seq[i:i + k]
        prob  = Prob(motif, amino_index, matrix)
        if prob > min_prob:
            min_motif = motif
            min_prob  = prob
    #print minval, prob_dict[minval]
    return min_motif



_AMINO_INDEX_ = ["A", "C", "G", "T"]

def BuildProfile(motif_list):
    motif_len = len(motif_list[0])
    profile   = []
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        count_list = []
        for each in _AMINO_INDEX_:
            num_amino = ith.count(each)
            count_list.append(num_amino)
        count_prob = [ float(x)/sum(count_list) for x in count_list ]
        profile.append(count_prob)
    return profile

def BuildProfilePseudo(motif_list):
    motif_len = len(motif_list[0])
    profile   = []
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        count_list = []
        for each in _AMINO_INDEX_:
            num_amino = ith.count(each) + 1
            count_list.append(num_amino)
        count_prob = [ float(x)/sum(count_list) for x in count_list ]
        profile.append(count_prob)
    return profile


def ScoreMotifs(motif_list):
    motif_len = len(motif_list[0])
    score_total = 0
    for i in range(motif_len):
        ith        = [ x[i] for x in motif_list ]
        mostcommon = MostCommon(ith)
        score      = len([ x for x in ith if x != mostcommon ])
        score_total += score
    return score_total

def GreedyMotifSearch(Dna_list, k, t):
    best_motif = [ x[:k] for x in Dna_list ]
    Dna_len    = len(Dna_list[0])
    Dna_num    = len(Dna_list)
    for i in range(Dna_len - k + 1):
        motif_list = []
        motif_list.append( Dna_list[0][i:i + k] )
        for j in range(1, Dna_num):
            profile = BuildProfile(motif_list)
            motif = ProfileMost(Dna_list[j], k, _AMINO_INDEX_, profile)
            motif_list.append(motif)
        if ScoreMotifs(motif_list) < ScoreMotifs(best_motif):
            best_motif = motif_list
    return best_motif

def GreedyMotifSearchPseudo(Dna_list, k, t):
    best_motif = [ x[:k] for x in Dna_list ]
    Dna_len    = len(Dna_list[0])
    Dna_num    = len(Dna_list)
    for i in range(Dna_len - k + 1):
        motif_list = []
        motif_list.append( Dna_list[0][i:i + k] )
        for j in range(1, Dna_num):
            profile = BuildProfilePseudo(motif_list)
            motif = ProfileMost(Dna_list[j], k, _AMINO_INDEX_, profile)
            motif_list.append(motif)
        if ScoreMotifs(motif_list) < ScoreMotifs(best_motif):
            best_motif = motif_list
    return best_motif


def RandomizedMotif(dna, k):
    start = randint(0, len(dna) - k)
    return dna[start:start + k]

def RandomizedMotifList(dna_list, k):
    motif_list = []
    for i in range(len(dna_list)):
        motif_list.append(RandomizedMotif(dna_list[i], k))
    return motif_list

def MotifsBuildfromProfile(dna_list, k, profile):
    motifs = []
    for i in range(len(dna_list)):
        motif = ProfileMost(dna_list[i], k, _AMINO_INDEX_, profile)
        motifs.append(motif)
    return motifs

def RandomizedMotifSearch(dna_list, k, t):
    motifs = RandomizedMotifList(dna_list, k)
    best_score = 1000000
    while True:
        profile = BuildProfilePseudo(motifs)
        motifs  = MotifsBuildfromProfile(dna_list, k, profile)
        score   = ScoreMotifs(motifs)
        if score < best_score:
            best_motifs = motifs[:]
            best_score  = score
        else:
            return best_motifs

def Runs1000Times(dna_list, k, t):
    best_score = 1000
    for i in range(1000):
        motifs = RandomizedMotifSearch(dna_list, k, t)
        if ScoreMotifs(motifs) < best_score:
            best_motifs = motifs
            best_score = ScoreMotifs(motifs)
    print best_score
    return best_motifs

if __name__ == "__main__":
    #dna = "ABC"
    #k = 2
    #print RandomizedMotif(dna, k)
    infile  = "dataset.txt"
    content = [line.strip() for line in open(infile).readlines()]
    k, t    = [int(x) for x in content[0].split()]
    seqs    = content[1:]
    content = [line.strip() for line in open(infile).readlines()]
    #print RandomizedMotifSearch(seqs, k, t)
    print "\n".join(RandomizedMotifSearch(seqs, k, t))
