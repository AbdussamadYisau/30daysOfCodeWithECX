def captains_room(arr):
	"""
	A couple of finite tourists lodge at an infinite hotel. The tourists are divided into two: A captain and an an unknown group of families consisiting of N members per group where N>1. The captain was given a seperate room and the rest were given one room per group. I'm trying to find the captain's room

	Basically, this function takes in a list and returns the element which appears only once. 

	Input: [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
	Output: 8

	"""

	# First, i want to get the elements that appear more than once

	n = len(arr)

	# Storing elements and their respective counts in a hashtable

	countElements = [0] * 100

	for i in range(0,n):
		countElements[arr[i]] += 1

	# List to store elements that occur more than once

	eleMorThanOnce = []

	# Since we want elements in the same order, we traverse the array again and print elements that appear more than once

	for i in range(0,n):

		if (countElements[arr[i]] > 1):
			eleMorThanOnce.append(arr[i])
#			print(arr[i], end = " ")


	#This is tricky, it is done to make sure the current element is not printed again
			countElements[arr[i]] = 0
		
	# List of the initial array to be put in a set 
	iniArr = set(arr)

	#Convert it back into a list 

	iniArr = list(iniArr)

	#This variable would contain the only element that is not repeated 
	answer = [item for item in iniArr if item not in eleMorThanOnce]

	return(answer)	




# Another implementation, a more efficient one

def captains_number(arr):

	"""
		A couple of finite tourists lodge at an infinite hotel. The tourists are divided into two: A captain and an an unknown group of families consisiting of N members per group where N>1. The captain was given a seperate room and the rest were given one room per group. I'm trying to find the captain's room

		Basically, this function takes in a list and returns the element which appears only once. 

		Input: [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
		Output: 8

		"""

	dict = {}
	for num in arr:
		if num not in dict:
			dict[num] = 0
		dict[num] += 1

	for num in dict:
		if dict[num] == 1:
			return num


arr = [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
print(captains_room(arr))

print(captains_number(arr))
