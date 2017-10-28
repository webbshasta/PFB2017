#!/usr/bin/env python3

import sys
import re

fasta_file = open('ecoli_6X.fasta', 'r')

length_list = []

for line in fasta_file:
	line = line.strip()
	m = re.search('len=(\d+)\s+',line)
	if m:
		line = m.group(1)
		length_list.append(int(line))

max_length = max(length_list)
min_length = min(length_list)

print('The longest contig is:', max_length, 'bases long.')
print('The shortest contig is:', min_length, 'bases long.')
