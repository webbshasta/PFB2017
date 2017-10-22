#!/usr/bin/env python3

import sys

#Create a function to format a string of DNA so that each line is no more than 60 nt long.
#INPUT: a string of DNA without newlines
#RETURNS: a string of DNA with lines no more than 60 nucleoties long

#dna_input = sys.argv[1]

fasta_input = open(sys.argv[1], 'r')
length = int(sys.argv[2])

def seq_format (fasta_input, length):
	fasta_seqs = {}
	fasta_keys = ''
	for line in fasta_input:
		line = line.strip()
		if line.startswith('>'):
			fasta_keys = line
			fasta_seqs[fasta_keys] = ''
			print(fasta_keys)
		else:		
			for pos in range(0,len(line), length):
				fasta_seqs[fasta_keys] = fasta_seqs[fasta_keys]+line[pos:pos+length]+'\n'
		print(fasta_seqs[fasta_keys], end = '')
	return('')

#fasta_input.close()
print (seq_format(fasta_input, length))
print ('end')
