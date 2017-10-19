#!/usr/bin/env python3
import re

#In the file Python_06_nobody.txt find every occurrence of 'Nobody' and print out the position.

poem = open('Python_06_nobody.txt', 'r')
poem_contents = poem.read()
line_number = 1

for line in re.finditer(r"(Nobody)", poem_contents, re.I):
	start_position = line.start(1) + 1
	print("Line number:", line_number, "Start position of Nobody:", start_position)
	line_number += 1
		
print('Done!')
