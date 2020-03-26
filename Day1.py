# GuessingGame
import random
def guessTheNumber(numOfGuesses, targNum):
	tempNumOfGuesses = 0 

	# Takes player's username
	userName = input("Yo, who you be? Talk your name for here: ")

	# targNum = random.randInt(1,100)
	print("Well, " + userName + ", I am thinking of a number between 1 and 100.")

	while tempNumOfGuesses < numOfGuesses:
		print("Take a guess. ")

		guess = input()
		guess = int(guess)

		tempNumOfGuesses = tempNumOfGuesses + 1

		if guess < targNum:
			print("Your guess is too low. ")

		if guess > targNum: 
			print("Your guess is too high")

		if guess == targNum:
			break

	if guess == targNum:
		tempNumOfGuesses = str(tempNumOfGuesses)
		print("Good job, " + userName +"! You guessed the right number in " + tempNumOfGuesses + " tries!")

	if guess != targNum:
		targNum = str(targNum)
		print("No, you are wrong. The number I was thinking of was " + targNum)


print(guessTheNumber(6,20))
