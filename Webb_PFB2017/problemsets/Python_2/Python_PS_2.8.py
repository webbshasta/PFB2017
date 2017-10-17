#$/usr/bin/env python3

import sys

my_number = float(sys.argv[1])

if my_number > 0 :			#This line tests if my_number is positive.
	print (my_number, 'is positive.')	
	if my_number > 50 :
		print (my_number, 'is greater than 50.')
		if my_number%3 == 0:
			print (my_number, 'is divisible by 3.')
	elif my_number < 50 :
		print (my_number, 'is less than 50.')
		if my_number%2 == 0:
			print (my_number, 'is even.')
elif my_number < 0 :			#This line tests if my_number is negative."
	print (my_number, 'is negative.')

print ("Script is complete!") 


