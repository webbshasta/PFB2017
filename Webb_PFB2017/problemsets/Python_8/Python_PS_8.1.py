#!/usr/bin/env python3
import re
import sys
#Take a mulit-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count

fasta_open = open(sys.argv[1], 'r')
seqs = {}

for line in fasta_open:
	line = line.rstrip()
	m = re.search(r'^>(\S+) ?.*$', line)
	if m:
		seq_id = m.group(1)		
		seqs[seq_id] = {'A':0, 'C':0, 'T':0, 'G':0} 
	else:
		for nt in line:
			if nt in seqs[seq_id]:
				seqs[seq_id][nt] += 1

for seq_id in seqs:
	print(seq_id,'\t',seqs[seq_id]['A'],'\t',seqs[seq_id]['C'],'\t',seqs[seq_id]['G'],'\t',seqs[seq_id]['T'])

fasta_open.close()	
