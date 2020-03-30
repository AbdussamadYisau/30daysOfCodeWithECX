# This code returns the power set of a particular list, in the form of sublists.

# import math

# def powerSet(list):

# 	list_size = len(list)
# 	print(list_size)
# 	# We are setting the power set of a list with size n as 2**n

# 	powerSetSize = (int)(math.pow(2,list_size))

# 	counter = 0

# 	j = 0

# 	# Now, we loop for counter from 0 to powerSetSize

# 	for counter in range (0, powerSetSize):
# 		for j in range(0, list_size):


# 			if((counter & (1 << j)) > 0):
# 				print(list[j], end = " ")
# 		print(" ")


# list = [2,4,6]

# powerSet(list)


# Another implementation

# def power_list(arr):
# 	# This gets the size of the array
# 	list_size = len(arr)

# 	for num in range(1 << list_size):
# 		print ([arr[j] for j in range(list_size) if (i & (1 << j))])


# power_list([2,4,6])

def power_list(arr):
	powerSet = [[]]

	for num in arr:
		#Iterate over the sub sets so far

		for subSet in powerSet:
			# Add a new subset consisting of the subset at hand

			powerSet = powerSet + [list(subSet) + [num]]
			print(powerSet)

	return(powerSet)


print(power_list([2,4,6]))

