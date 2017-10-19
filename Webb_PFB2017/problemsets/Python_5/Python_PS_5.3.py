#!/usr/bin/env python3

#Open and print the reverse complement of each sequence in Python_05.fasta. Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.k
#Refer to PS 3.3.py for reverse comple
fasta_read = open('Python_05.fasta', 'r')

fasta_seqs = {}
fasta_keys = None

for line in fasta_read:
	line = line.rstrip()
	if line.startswith('>'):
		line = line.replace('>', '')
		fasta_keys = line
		fasta_seqs[fasta_keys] = ''
	else:
		fasta_seqs[fasta_keys] += line

#print(fasta_seqs)
fasta_read.close()

#reqrite with no loops and list comprehension

for seq_key in fasta_seqs:
	fasta_seqs[seq_key] = fasta_seqs[seq_key].replace('A', 't')
	fasta_seqs[seq_key] = fasta_seqs[seq_key].replace('G', 'c')
	fasta_seqs[seq_key] = fasta_seqs[seq_key].replace('C', 'g')
	fasta_seqs[seq_key] = fasta_seqs[seq_key].replace('T', 'a')
	print('>'+ seq_key + ' This is the reverse complement:\n' + fasta_seqs[seq_key][::-1].upper())











