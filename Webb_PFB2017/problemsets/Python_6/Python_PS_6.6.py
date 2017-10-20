#!/usr/bin/env python3
import re

#The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence Python_06_ApoI.fasta.

#Y can be C or T
#R can be A or G

fasta_open = open('Python_06_ApoI.fasta', 'r')

for line in fasta_open:
	line = line.rstrip()
	if not line.startswith('>'):
		for ApoI in re.findall(r'[A|G]AATT[C|T]', line):
			print(ApoI)

print("Script has finished.")
