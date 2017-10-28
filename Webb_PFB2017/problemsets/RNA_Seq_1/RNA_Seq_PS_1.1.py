#!/usr/bin/env python3

import sys
import re

kmer_length = int(sys.argv[1])
filename = open(sys.argv[2] , 'r')
num_top_kmers = int(sys.argv[3]) 
line_counter = 1
kmer_dict = {}
sequence = ''

for line in filename:
	line = line.strip()
	if line_counter%4 == 2:
		sequence = line
		for pos in range(0,len(sequence)-kmer_length+1): 
			kmer = sequence[pos:kmer_length + pos]
			if len(kmer) ==  kmer_length:
				if kmer in kmer_dict:
					kmer_dict[kmer] += 1
				else:
					kmer_dict[kmer] = 1
	line_counter += 1 


sorted_kmers = sorted(kmer_dict, key = lambda x:kmer_dict[x], reverse=True)
print(sorted_kmers[0:num_top_kmers])

#still need to have it print out column of top kmers and column of counts of those kmers

	
