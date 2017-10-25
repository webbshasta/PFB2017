#!/usr/bin/env python3

import sys
import os

#files = open(sys.argv[1], 'r')
directory = '/Users/admin/Webb_PFB2017/problemsets/Blast_1'
field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']
current_data = {}

matrix_names = ['BL50', 'BP62'] #'VT160', 'VT80', 'VT40']
matrix = {}
count = 0

for file_name in os.listdir(directory):
	if file_name.endswith(".txt"):
		file_handle = open(file_name, 'r')
		matrix_name = file_name.split('_')[-1].rstrip('.txt')
		for line in file_handle:
			line = line.strip()
			if not line.startswith('#'):	
				current_data = dict(zip(field_names, line.split('\t')))	
				print(matrix_name + '\t' + current_data['percid'] + '\t' + current_data['alen'] + '\t' + current_data['evalue'])
				break
			






