#!/usr/bin/env python2

import sys

def main():
	"""
	Main of cipher.py.

	Everything starts here.
	"""
	table = generateTable()
	printTable(table)

def generateTable():
	"""
	Generates a table known as a "Tabula Recta"
	This table is 26 different rotations of the 
	English alphabet.

	Example rows:
	A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
	B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
	C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
	D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
	E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
	.
	.
	.
	Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
	"""
	n = 0  # Start with the letter A
	table = [] # Create a list
	# 26 letters in the English alphabet so create 26 rows 
	for i in range(0, 26):
		# Check to make sure n is bounded [0, 25]
		n = n % 26
		# Create a new row
		row = ""
		# Loop 26 times to generate a shifted alphabet of 26 letters
		for j in range(0, 26):
			# Check to make sure n is bounded [0, 25]
			n = n % 26
			'''
			ord(c) converts an ASCII character to its numeric ASCII value.
			Ex: ord('A') = 65

			Then add the offset of n which is a value [0, 25]
			Ex: n = 3 
			ord('A') + n = 68 
			68 is the decimal ASCII value of D 

			chr(d) converts an integer value back to its ASCII form.
			chr(68) = 'D'
			
			Then append this to the row string.
			'''
			row += chr(n + ord('A'))
			# Increment n by 1 to get the next letter in the alphabet
			n += 1
		# Increment n by 1 to get the next letter in the alphabet
		n += 1
		# Add the newly created row to the table (which is a list of strings)
		table.append(row)
	return table

def printTable(table):
	"""
	Prints out the table to the terminal.
	"""
	for i in range(0, 26):
		for char in table[i]:
			# Trick to printing without a newline put a , after string
			# This also has the added benefit of printing a space between characters
			print "{}".format(char),
		# Print a newline
		print ""

if __name__ == "__main__":
    sys.exit(main())
