#!/usr/bin/env python2

import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFTED  = None

def main():
	"""
	Main of cipher.py.

	Everything starts here.
	"""
	global SHIFTED
	while True:
		n = int(raw_input('Enter an integer >= 0: '))
		if n >= 0:
			# We had a valid input, exit this loop
			break
		else:
			# Invalid input so let the user know and try again
			print "Incorrect value was provided: {}".format(n)
	# Generate the shifted alphabet
	SHIFTED = rotateAlphabet(n)
	# Print out the shifted alphabet
	print "Shifted Alphabet: {}".format(SHIFTED)
	# Start the main loop for the program
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


def encrypt():
	"""
	Asks the user for a string to encrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the encrypted text.
	"""
	plaintext = raw_input('Please enter a string to encrypt: ')
	# Remove all whitespace from the string; Trick from http://stackoverflow.com/a/3739939
	# plaintext = "".join(plaintext.split())
	# Convert all text to uppercase
	plaintext = plaintext.upper()
	# Loop through each character in the string and replace it with the correct substitution
	ciphertext = ""
	for character in plaintext:
		# Check to see if we have a letter [A-Z]
		if character.isalpha():
			"""
			ord(c) converts an ASCII character to its ASCII value.
			Ex: ord('A') = 65

			The line ord(character) - ord(ALPHABET[0]) will take the ASCII 
			value of the character and subtract it by the ASCII value 
			of the first character of ALPHABET which is 'A'. This will give 
			us a value from [0, 26) which can be mapped to the SHIFTED list.

			Example:

			In the Caesar cipher A should map to D
			ord('A') - ord('A') 
			65 - 65 = 0
			encrypted_character = SHIFTED[0]
			SHIFTED[0] is the letter 'D' 
			""" 
			ciphertext += SHIFTED[ord(character) - ord(ALPHABET[0])]
		else:
			# if its not a letter [A-Z] just append it to the string
			ciphertext += character
	return ciphertext

def decrypt():
	"""
	Asks the user for a string to decrypt and then performs the rotation cipher
	on the provided input.
	@return Returns the decrypted text.
	"""
	ciphertext = raw_input('Please enter a string to decrypt: ')
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
			ord(c) converts an ASCII character to its ASCII value.
			Ex: ord('A') = 65

			The line ord(character) - ord(SHIFTED[0]) will take the ASCII 
			value of the character and subtract it by the ASCII value 
			of the first character of SHIFTED which is 'D'. This will give 
			us a value from [0, 26) which can be mapped to the ALPHABET list.

			Example:

			In the Caesar cipher decrypt function D should map to A
			ord('D') - ord('D') 
			68 - 68 = 0
			decrypted_character = ALPHABET[0]
			ALPHABET[0] is the letter 'A' 
			""" 
			plaintext += ALPHABET[ord(character) - ord(SHIFTED[0])]
		else:
			# if its not a letter [A-Z] just append it to the string
			plaintext += character
	return plaintext

if __name__ == "__main__":
    sys.exit(main())
