#!/usr/bin/env python3

import subprocess

#Write a script to count the number of sequences in a FASTQ file.
#Output the mean and standard deviation of sequence lengths
#Calculate the mean and standard deviation of base quality scores.

fastq_input = open('pfb.fastq', 'r')

count = 0

for line in fastq_input:
	line = line.strip()
	count += 1

print(int(count/4))
