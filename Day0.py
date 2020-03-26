# Scrabble word score generator

# Creating a dictionary that contains each letter and its respective point

score = { "a": 1 , "b": 3 , "c": 3 , "d": 2 , "e": 1 , "f": 4 , "g": 2 ,
		  "h": 4 , "i": 1 , "j": 8 , "k": 5 , "l": 1 , "m": 3 , "n": 1 ,
		  "o": 1 , "p": 3 , "q": 10, "r": 1 , "s": 1 , "t": 1 , "u": 1 ,
		  "v": 4 , "w": 4 , "x": 8 , "y": 4 , "z": 10 }

 # Creating a function that takes in a word as an argument and give you the total score

def scrabbleScore(word):

 # Score as at the beginning of the word is 0

	initScore = 0

 # Looping throught the word and calculating the total score

	for i in word:
	#Make each letter of the word lowercase 
		i = i.lower()

		initScore = initScore + score[i]

	return initScore

example = input("Enter word here: " )
print(scrabbleScore(example))
