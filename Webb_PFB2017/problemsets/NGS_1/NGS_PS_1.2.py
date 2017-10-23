#!/usr/bin/env python3

import re
import statistics

#Write a script to trim each sequence in a FASTQ file starting from the first base in each sequence lower than Q=20 to the end of the sequence. (don't forget to trim the quality scores as well)

fastq_input = open('pfb.fastq', 'r')

line_counter = 1
seq_count = 0
lengths = [] #creating empty list of sequence lengths
quality_scores = [] #creating empty list of q scores
raw_seq = ''

for line in fastq_input:
	line = line.strip()
	if line_counter%4 == 1: #this represents all the header lines
		seq_count += 1
		header = line 
	elif line_counter%4 == 2:
		raw_seq = line #this represents all the sequence lines
	elif line_counter%4 == 3:
		comment_line = line	
	elif line_counter%4 == 0: #this represents all the quality score lines
		for pos, score in enumerate(line):
			if (ord(score) - 33) < 20:
				trim_score = line[:pos]
				trim_seq = raw_seq[:pos]
				print(header+'\n'+ trim_seq+'\n'+ comment_line+'\n'+ trim_score)
				break
	line_counter += 1			

'''
print('Number of sequences:', seq_count)
print('Mean sequence length:', sum(lengths)/len(lengths))
print('Standard dev. of sequence length: {:.2f}'.format((statistics.stdev(lengths))))
print('Mean quality score: {:.2f}'.format(sum(quality_scores)/len(quality_scores)))
print('Standard dev. of quality score: {:.2f}'.format(statistics.stdev(quality_scores)))
''' 







