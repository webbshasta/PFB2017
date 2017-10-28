#!/usr/bin.env python3

import sys
import re

#File name: RNA_Seq_PS_1.2.py

#Write a python program that reads in the 'bowtie2.bam' file and generates a table containing the number of reads mapped to each gene.

fh = open(sys.argv[1], 'r')

gene_names = {} #value is a set from the gene name in the sam file, add read name to set

for line in fh:
	line = line.rstrip() 					#stripping white space
	fields = line.split("\t")				#splitting entire line on tabs
	read_name = fields[0]					#splitting the fields variable into two more variables by indexing
	combo_name = fields[2]
	#print(combo_name)	
	(gene_id, transcript_id) = combo_name.split("^") #splitting combo name on the "^" so extract short gene id
	
	if gene_id not in gene_names:			#check to see if gene_id is not in the initiated dictionary
		gene_names[gene_id] = set()			#filling the dictionary with values that are empty sets
		
	gene_names[gene_id].add(read_name)		#here is where we fill up the empty sets with read names

gene_ids = sorted(gene_names, key=lambda x:len(gene_names[x]), reverse = True) #sorting the keys in our dictionary in reverse order
print(gene_ids)

for gene_id in gene_ids:					#iterating through the sorted list that is gene_ids
	my_set = gene_names[gene_id]			#populating another set with gene ids
	num_reads = len(my_set)					#populating number of reads using length function

print("{}\t{}".format(gene_ids, num_reads))

			


