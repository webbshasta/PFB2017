#!usr/bin/env python3
import sys
my_variable = float(sys.argv[1])

if bool(my_variable) == True :
	message = "is True."
	print my_variable, message
else :
	message = "is not True."


