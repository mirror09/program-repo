#  -----------------------------------------------------------------
#  File Name	:RandomMotifs.py
#  DEVELOPER	:Victor Frankenstein (Banerjee)
#  Email		:<recervictory@gmail.com>
#  Date			:2016-03-07
#  
#  
#  Copyright 2016 Victor Frankenstein (Banerjee) <recervictory@gmail.com>
#  -----------------------------------------------------------------

## this function stochastically tries to find a set of motifs that minimizes the sum of Hamming's distance to its consensus
def find_good_motifs_rand_srch(DNA_list, k):
	n = len(DNA_list[0])
	t = len(DNA_list)

    ## randomly select k-mer motifs in each string in DNA_list
	motifs = []
	for DNA_str in DNA_list:
		rand_ind_strt = random.randrange(0, n-k+1)
		rand_ind_end = rand_ind_strt + k
		motif = DNA_str[rand_ind_strt:rand_ind_end]
		motifs.append(motif)
	best_motifs = motifs

    ## loop until cumulative Hamming distance stops minimizing
	while True:
		prof_mtrx = create_prof_mtrx_from_motifs(motifs)
		motifs = create_motifs_based_on_prof_mtrx(prof_mtrx, DNA_list, k)
		cur_motifs_cum_dist = calc_cum_dist_btwn_motifs_and_consensus(motifs)
		best_motifs_cum_dist = calc_cum_dist_btwn_motifs_and_consensus(best_motifs)
		if cur_motifs_cum_dist < best_motifs_cum_dist:
			best_motifs = motifs
		else:
			return best_motifs

def create_prof_mtrx_from_motifs(motifs, zero_prob_adj=False):

    ## calculate nucleotide count matrix
    nuc_cnt_mtrx = create_nuc_cnt_mtrx_from_motifs(motifs)
    nuc_cnt_mtrx = np.array(nuc_cnt_mtrx)
    if zero_prob_adj:
        nuc_cnt_mtrx += 1

    ## calculate profile matrix
    prof_mtrx = nuc_cnt_mtrx / nuc_cnt_mtrx.sum(axis=0, keepdims=True)
    prof_mtrx = prof_mtrx.tolist()

    ## return
    return prof_mtrx

def create_motifs_based_on_prof_mtrx(prof_mtrx, DNA_list, k, zero_prob_adj=True):
    motifs = []
    for DNA_str in DNA_list:
        most_prob_kmer = find_most_prob_kmer_based_on_prof_mtrx(DNA_str, k, prof_mtrx, zero_prob_adj)
        motifs.append(most_prob_kmer)
    return motifs

def calc_cum_dist_btwn_motifs_and_consensus(motifs):
    consensus_str = find_consensus_str_from_motifs(motifs)
    cum_dist = calc_cum_dist_btwn_motifs_and_str(motifs, consensus_str)
    return cum_dist    
    
def create_nuc_cnt_mtrx_from_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)

    ## convert 2-dim list to 2-dim numpy array
    motifs = [list(motif) for motif in motifs]
    motifs = np.array(motifs)

    ## initialize (transpose of) nucleotide count matrix
    nuc_cnt_mtrx_T = np.zeros([k, 4])
    
    ## for each column in motifs matrix, count by nucleotide (A, C, T, G)
    for i in range(0, len(motifs.T)):
        col = motifs.T[i]
        nuc_cnt_dict = dict(collections.Counter(col))
        nuc_cnt_list = conv_nuc_cnt_dict_to_list(nuc_cnt_dict)
        nuc_cnt_mtrx_T[i] = nuc_cnt_list

    ## return 
    nuc_cnt_mtrx = nuc_cnt_mtrx_T.T
    nuc_cnt_mtrx = nuc_cnt_mtrx.tolist()
    return nuc_cnt_mtrx

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
