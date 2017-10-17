#$/usr/bin/env python3

import sys

my_number = float(sys.argv[1])

if my_number > 0 :			#This line tests if my_number is positive.
	message = "is positive."
	print my_number, message	
	if my_number > 50 :
		message = 'is greater than 50.'
		print my_number, message
		if my_number%3 == 0:
			message = 'is divisble by 3.'
			print my_number, message
	elif my_number < 50 :
		message = 'is less than 50.'
		print my_number, message
		if my_number%2 == 0:
			message = 'is even.'
			print my_number, message
elif my_number < 0 :			#This line tests if my_number is negative.
	message = "is negative."
	print my_number, message

print "Script is complete!" 


