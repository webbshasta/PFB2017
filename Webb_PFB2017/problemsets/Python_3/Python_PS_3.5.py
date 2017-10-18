#!/usr/bin/env python3
import sys

#This is a script to find the start position of an EcoRI in the variable dna.

dna = 'GAATTCGAATTCGATTT'

ga_count = dna.count('GA')
ga_first = dna.find('GA')
ga_second = dna.find('GA',len('GA') + ga_first)
ga_third = dna.find('GA',len('GA') + ga_second)

string = "There are {0} restriction sites in the sequence and they are located at positions {1}, {2}, and {3}.".format(ga_count, ga_first, ga_second, ga_third)

print("\n" + string + "\n")
 
