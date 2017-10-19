#!/usr/bin/env python3
#Write a script to do the following to Python_05.txt

#Open and read the contents.
#Uppercase each line
#Print each line to the STDOUT
fo_read = open('Python_05.txt.1', 'r')
fo_write = open('Python_05_uc.txt', 'w') 

#file_contents = file_object.read()

for lyric in fo_read:
	lyric = lyric.rstrip()
	#lyric.upper()
	fo_write.write(lyric.upper() + '\n') 

fo_read.close()
fo_write.close()

print('Script has written to "Python_05_uc.txt"')






