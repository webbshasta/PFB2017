#!/usr/bin/env python3

import sys
from Bio import SeqIO

#with the Bio.SeqIO module, generate a list of all the IDs in the fasta file. How many are there?

records = list(SeqIO.parse("uniprot_sprot.fasta", "fasta")) #creates a list of all records in the fasta file
print(len(records))
