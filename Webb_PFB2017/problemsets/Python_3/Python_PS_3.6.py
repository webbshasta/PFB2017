#!/usr/bin/env python3
import sys

#This is a script to find the start position of an EcoRI in the variable dna.

dna_raw = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

dna = dna_raw.strip()

ga_count = dna.count('GAATTC') #These 2 lines first count the number of occurrances in the raw seq, then find the first instance of the EcoRi site
ga_first = dna.find('GAATTC')

#print("Number of restriction sites:", ga_count, "\nStart position of EcoRI:",  ga_first)

len_fragment_1 = len(dna[0:ga_first+1]) #This finds the length of fragment 1
len_fragment_2 = len(dna[ga_first+1:])  #This finds the length of fragment 2

#print(len_fragment_1, len_fragment_2)

fragment_1 = (dna[0:ga_first]) #These are the bases in fragment 1
fragment_2 = (dna[ga_first:])  #These are the bases in fragment 2

position_1 = dna.find(fragment_1) #This is the position of the start of fragment one 
position_2 = dna.find(fragment_2) #This is the position of the start of fragment two

#print(fragment_1, "\t", position_1, "\t", len_fragment_1)
#print(fragment_2, "\t", position_2, "\t", len_fragment_2)

frag_list = []   		#Creating an empty list 
frag_list.append(fragment_1)	#Populating list with the dna fragments using append
frag_list.append(fragment_2)

sorted_frag_list = sorted(frag_list, key = len)	#sorting the fragmented list by length

print(sorted_frag_list)






