#!/usr/bin/env python2

import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
SHIFTED  = "DEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABC"

def main():
	"""
	Main of cipher.py.

	Everything starts here.
	"""
	running = True
	while running:
		while True:
		# Loop until the Option D or E was provided.
			option = raw_input('Type E for encryption or D for decryption: ')
			if option.upper() == 'D' or option.upper() == 'E':
				# If it was valid break out of this loop
				break
			else:
				# We didn't get a valid input so let the user know and try again
				print "Incorrect option was provided: {}".format(option)

		# Select the correct function for the method selected 
		if option.upper() == 'E':
			ciphertext = encrypt()
			print "Ciphertext: {}".format(ciphertext)
		elif option.upper() == 'D':
			plaintext = decrypt()
			print "Plaintext: {}".format(plaintext)
		# Ask the user if they want to use the program again
		while True:
			option = raw_input('Encrypt or decrypt another string?(Y/N): ')
			if option.upper() == 'Y' or option.upper() == 'N':
				break
			else:
				print "Incorrect option was provided: {}".format(option)
		# Determine if the user wants to run again
		running = option.upper() == 'Y'
	print "Exiting.."

def encrypt():
	"""
	Asks the user for a string to encrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the encrypted text.
	"""
	plaintext = raw_input('Please enter a string to encrypt: ')
	# Loop through each character in the string and replace it with the correct substitution
	ciphertext = ""
	for character in plaintext:
		# Check to see if we have a letter or digit [A-Z][a-z][0-9]
		if character.isalnum():
			"""
			Uses the index function of a string to find the 
			integer position of the character in ALPHABET
			and grab the character in SHIFTED at that same index. 
			""" 
			ciphertext += SHIFTED[ALPHABET.index(character)]

		else:
			# if its not a letter or digit [A-Z][a-z][0-9] just append it to the string
			ciphertext += character
	return ciphertext

def decrypt():
	"""
	Asks the user for a string to decrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the decrypted text.
	"""
	ciphertext = raw_input('Please enter a string to decrypt: ')
	# Loop through each character in the string and replace it with the correct substitution
	plaintext = ""
	for character in ciphertext:
		# Check to see if we have a letter or digit [A-Z][a-z][0-9]
		if character.isalnum():
			"""
			Uses the index function of a string to find the 
			integer position of the character in SHIFTED
			and grab the character in ALPHABET at that same index. 
			""" 
			plaintext += ALPHABET[SHIFTED.index(character)]
		else:
			# if its not a letter or digit [A-Z][a-z][0-9] just append it to the string
			plaintext += character
	return plaintext

if __name__ == "__main__":
    sys.exit(main())
