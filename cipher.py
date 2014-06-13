#!/usr/bin/env python2

import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFTED  = "DEFGHIJKLMNOPQRSTUVWXYZABC"

def main():
	"""
	Main of cipher.py.

	Everything starts here.
	"""
	running = True
	while running:
		while True:
		# Loop until the Option D or E was provided.
			option = raw_input('Type E for encryption or D for decryption or C to crack: ')
			if option.upper() == 'D' or option.upper() == 'E' or option.upper() == 'C':
				# If it was valid break out of this loop
				break
			else:
				# We didn't get a valid input so let the user know and try again
				print "Incorrect option was provided: {}".format(option)
		# Select the correct function for the method selected 
		if option.upper() == 'E':
			plaintext = raw_input('Please enter a string to encrypt: ')
			ciphertext = encrypt(plaintext)
			print "Ciphertext: {}".format(ciphertext)
		elif option.upper() == 'D':
			ciphertext = raw_input('Please enter a string to decrypt: ')
			plaintext = decrypt(ciphertext)
			print "Plaintext: {}".format(plaintext)
		elif option.upper() == 'C':
			ciphertext = raw_input('Please enter a string to crack: ')
			crack(ciphertext)
		# Ask the user if they want to use the program again
		while True:
			option = raw_input('Encrypt, decrypt, or crack another string?(Y/N): ')
			if option.upper() == 'Y' or option.upper() == 'N':
				break
			else:
				print "Incorrect option was provided: {}".format(option)
		# Determine if the user wants to run again
		running = option.upper() == 'Y'
	print "Exiting.."

def crack(ciphertext):
	"""
	Cycles through all possible rotations of a string
	and prints them to the terminal.
	"""
	# Perform a simple check to make sure the varaible is not None
	if ciphertext is not None:
		ciphertext = ciphertext.upper()
		for i in range(0, 26):
			rot_alpha = rotateAlphabet(i)
			cracked_text = decrypt(ciphertext, rot_alpha)
			print "Attempt {}: {}".format(i, cracked_text)
		print ""  # Print a newline


def rotateAlphabet(n):
	"""
	Creates a shifted alphabet to use for 
	encryption an decryption.
	@param n Amount to shift the alphabet by.
	@return Returns a string containing the shifted alphabet.
	"""
	# Bound the value entered by 26
	n = n % 26
	# Counter to keep track of how many letters generated
	i = 0
	# String to store new alphabet
	alphabet = ""
	for i in range(0, 26):
		# 0 <= n <= 25
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
		
		Then append this to the alphabet string.
		'''
		alphabet += chr(ord('A') + n)
		# Increment n by one to generate the next letter in alphabet
		n += 1
	return alphabet

def encrypt(plaintext, shifted=SHIFTED):
	"""
	Asks the user for a string to encrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the encrypted text.
	"""
	# Convert all text to uppercase
	plaintext = plaintext.upper()
	# Loop through each character in the string and replace it with the correct substitution
	ciphertext = ""
	for character in plaintext:
		# Check to see if we have a letter [A-Z]
		if character.isalpha():
			"""
			Uses the index function of a string to find the 
			integer position of the character in ALPHABET
			and grab the character in shifted at that same index. 
			"""  
			ciphertext += shifted[ALPHABET.index(character.upper())]
		else:
			# if its not a letter [A-Z] just append it to the string
			ciphertext += character
	return ciphertext

def decrypt(ciphertext, shifted=SHIFTED):
	"""
	Asks the user for a string to decrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the decrypted text.
	"""
	# Remove all whitespace from the string; Trick from http://stackoverflow.com/a/3739939
	# ciphertext = "".join(ciphertext.split())
	# Convert all text to uppercase
	ciphertext = ciphertext.upper()
	# Loop through each character in the string and replace it with the correct substitution
	plaintext = ""
	for character in ciphertext:
		# Check to see if we have a letter [A-Z]
		if character.isalpha():
			"""
			Uses the index function of a string to find the 
			integer position of the character in shifted
			and grab the character in ALPHABET at that same index. 
			"""  
			plaintext += ALPHABET[shifted.index(character.upper())]
		else:
			# if its not a letter [A-Z] just append it to the string
			plaintext += character
	return plaintext

if __name__ == "__main__":
    sys.exit(main())
