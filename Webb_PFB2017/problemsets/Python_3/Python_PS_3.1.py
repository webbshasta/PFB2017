#!/usr/bin/env python3

import sys

dna = sys.argv[1]
dna_AT_content = (float(dna.count('T')) + float(dna.count('A'))) / len(dna)
dna_GC_content = (float(dna.count('C')) + float(dna.count('G'))) / len(dna)

string_AT = "This sequence has an AT content of {:.2%}.".format(dna_AT_content)
string_GC = "This sequence has a GC content of {:.2%}.".format(dna_GC_content)

print(string_AT, string_GC)


