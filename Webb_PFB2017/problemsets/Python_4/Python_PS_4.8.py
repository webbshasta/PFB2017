#!/usr/bin/env python3
import sys
#Write a script that uses range() in a for loop to print out every number between 0 and 99

number_1 = int(sys.argv[1])
number_2 = int(sys.argv[2]) 

for num in range(number_1, number_2 + 1):
	if num %2 != 0:
		print(num)

print("Script is done.")
