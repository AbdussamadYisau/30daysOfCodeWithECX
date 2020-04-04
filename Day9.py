def decryptor(text,key):
	"""
	Given a paragraph text as a string and its decryption key, create
	a function named decryptor that returns the decrypted text.

	Input: Gvvrk, -6
	Output: Apple


	"""

	translation = " "


	for ele in text:
		if ele.isalpha():
			message = ord(ele)
			message += key

			if ele.isupper():
				if message > ord("Z"):
					message -= 26

				elif message < ord("A"):
					message += 26

			elif ele.islower():
				if message > ord("z"):
					message -= 26

				elif message < ord("a"):
					message += 26

			translation += chr(message)

		else:
			translation += ele

	return(translation)


print(decryptor("Gvvrk", -6))

