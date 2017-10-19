#!/usr/bin/env python3
import sys

#This is a script to find the start position of an EcoRI in the variable dna.

dna  = 'TTTGATTTGATTTTGATTTGATTT'
ga_count = dna.count('GA')
ga_first = dna.find('GA')
ga_second = dna.find('GA',len('GA') + ga_first)

string = "There are {0} restriction sites in the sequence and they are located at positions {1} and {2}.".format(ga_count, ga_first, ga_second)

print("\n" + string + "\n")
 
