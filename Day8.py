
def Hangman(word, trials):
	"""
	This task rewuires us to give a user N trials to guess all the letters in a word. If a user correctly guesses a letter, we print it, other wise, we print an underscore.

	There's also a return statement indicating whether they won or lost



	"""
	# This makes all the elements in the word lowercase
	word = word.lower()

	print("The number of underscores here tell you how many letters the word that you are to guess has:")
	# Create a variable which stores the guesses 
	guessWord = " "
	while trials > 0:
		#Keep track of the number of times a user has failed
		fails = 0

		#Comparing characters in the secret word and those in guesses
		for ele in word:
			if ele in guessWord:
				print(ele)

			else:
				print("_")

				#For every underscore, 1 will be added to the number of fails

				fails += 1

		if fails == 0:

		# That means the user got everything
			print("The word is:", word)

			return("You win")

		# If the user has inputed the wrong character, he/she should input another one

		guess = input("guess a character (use lowercase): " )

		# Keeping track of the number of guesses
		guessWord += guess

		# check the new guess with word

		if guess not in word:
			trials -= 1

			#If the character doesn't match the word, let the user know
			print("Wrong")

			# Also, let him know the number of trials he has left

			print("Trials remaining: ", + trials )

			if trials == 0:
				return("You lose")




print(Hangman("Samuel", 10))





