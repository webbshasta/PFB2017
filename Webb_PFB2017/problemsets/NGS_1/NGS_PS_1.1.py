#!/usr/bin/env python3

import re
import statistics

#Write a script to count the number of sequences in a FASTQ file.
#Output the mean and standard deviation of sequence lengths
#Calculate the mean and standard deviation of base quality scores.

fastq_input = open('pfb.fastq', 'r')

line_counter = 1
seq_count = 0
lengths = [] #creating empty list of sequence lengths
quality_scores = [] #creating empty list of q scores

for line in fastq_input:
	line = line.strip()
	if line_counter%4 == 1:
		seq_count += 1
	elif line_counter%4 == 2:
		lengths.append(len(line))#find length and add to length list
	elif line_counter%4 == 0:
		for score in line:
			quality_scores.append(ord(score) + 33)#translate phred score & add to quality score list
	line_counter += 1

print('Number of sequences:', seq_count)
print('Mean sequence length:', sum(lengths)/len(lengths))
print('Standard dev. of sequence length: {:.2f}'.format((statistics.stdev(lengths))))
print('Mean quality score: {:.2f}'.format(sum(quality_scores)/len(quality_scores)))
print('Standard dev. of quality score: {:.2f}'.format(statistics.stdev(quality_scores)))
 







