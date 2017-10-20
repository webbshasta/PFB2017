#!/usr/bin/env python3
import re

#If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns (groups).
#Print lines something like this id:"extracted seq name" desc:"extracted description"

fasta_open = open('Python_06.fasta', 'r')

for line in fasta_open:
	line = line.rstrip()
	if line.startswith('>'): 
		for (seq_id, desc) in re.findall(r'^>(\S+)(.*)$', line):
			print('Sequence ID is:', seq_id, 'Description:', desc)


fasta_open.close()
