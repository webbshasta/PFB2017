#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

seq_lengths = [(len(seq) , seq) for seq in seqs]
count = 1

for len in seq_lengths :
	print('Count:', count , str(len[0]), '\t', str(len[1]))
	count += 1
