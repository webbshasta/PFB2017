#!/usr/bin/env python3

import re

#Using pattern matching, find all the header lines in Python_06.fasta. Note that the format for a header in a fasta file is a line that starts with a greater than symbol and is followed by some text (e.g. >seqName description where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)

fasta_open = open('Python_06.fasta', 'r')

for line in fasta_open:
	line = line.rstrip()
	if line.startswith('>'): 
		header = re.findall(r'^>\S+.*', line)
		print('Fasta header is:', header)

print('Script is finished running.')

fasta_open.close()
