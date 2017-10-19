#!/usr/bin/env python3

import re
#In the file Python_06_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).

poem_fo = open('Python_06_nobody.txt', 'r')
poem_output = open('Somebody.txt', 'w')

for line in poem_fo:
	line = line.rstrip()
	line = re.sub(r'Nobody', 'Somebody', line, re.I)
	poem_output.write(str(line) + '\n')	

print('Wrote to Somebody.txt')
poem_fo.close()
poem_output.close()
