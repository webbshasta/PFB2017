#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

sorted_numbers = sorted(numbers)	
even_sum = 0
odd_sum = 0

for number in sorted_numbers:
	print(number)
	if number %2 == 0:
		even_sum = even_sum + number
		number += 1
	elif number %2 != 0:
		odd_sum = odd_sum + number
		number += 1

print("The sum of all even numbers is:", even_sum)
print("The sum of all odd numbers is:", odd_sum)
