#!/usr/bin/env python3

import sys
from Bio import SeqIO
import re
#Make a list of all the descriptions. The description field almost always has a field OS=... that includes a species or strain designation.Here the genus is Salmonella and the species is paratyphi. There is also a strain 'B (strain ATCC BAA-1250 / SPB7). You can ignore this part. Using regular expressions, extract just the genus and species and count the number of sequences present for that genus/species combination. List comprehensions make this kind of data processing quick to code, but you might want to start by going step by step in a for loop.

record_dict = SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta", "fasta"))

descriptions = []

for seq_id, seq in record_dict.items():
	m = re.search(r"(OS=)", seq_id)
	if m:
		seq_id = m.group(1)
	descriptions += descriptions.append(seq_id)

print(descriptions)
		



