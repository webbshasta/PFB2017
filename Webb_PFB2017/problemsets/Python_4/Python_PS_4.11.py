#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

count = 0
for seq in seqs :
	count += 1
	print('Count:', count, 'Sequence:', seq, 'Length:', len(seq))
