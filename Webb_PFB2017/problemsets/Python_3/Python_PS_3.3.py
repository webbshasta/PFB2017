#!/usr/bin/env python3
import sys

dna = "AAATTTGGGCCC" #reverse complement should read GGGCCCAAATTT

#First need to find complement, then reverse it

dna_complement_A = dna.replace('A', 't')
dna_complement_T = dna_complement_A.replace('T', 'a')
dna_complement_G = dna_complement_T.replace('G', 'c')
dna_complement_C = dna_complement_G.replace('C', 'g')

#reverse_complement = dna_complement_A + dna_complement_T +dna_complement_G + dna_complement_C

print(dna_complement_C[::-1].upper())
