#Using binary search algorithm to check if a number exists in a list

# def bin_search(numList, num):
# 	#Sorting the list
# 	numList = numList.sort()
# 	#Getting the position for the splitting to occur
# 	half = len(numList)//2

# 	#First half of the list
# 	firstList = numList[:half]

# 	#Second half of the list 
# 	secondList = numList[half:]

# 	#Getting the last element in the first list and comparing that to the element being searched for

# 	if num == firstList[-1]: 
# 		return ("1")
# 	elif num < firstList[-1]:
# 		return (bin_search(numList, num))

# 	elif num >= secondList[-1]:
# 		return (bin_search(numList, num))

# 	else:
# 		return -1



# arr = [1,2,3,4,5,6]



# x = 3 

# print(bin_search(arr,x))



def bin_search(numList, num):

	#Sort the list

	numList.sort()

	# Create a variable to represent the lowest index of the list at any given time
	low = 0

	# Create a variable to represent the highest index of the list at any given time
	high = len(numList) - 1

	# Create a variable to represent the binary respone that the function gives
	found = False


	# Loop to continue doing binary search iteravely till element is found (or not)
	while(low <= high and not found):
		#Create a variable which represents the middle index at any given time
		mid = (low + high) // 2

		if num == numList[mid]:
			found = True
		elif num < numList[mid]:
			high = mid - 1
		elif num > numList[mid]:
			low = mid + 1
	return found


arr = [8,5,3,2,1]
x = 2
print(bin_search(arr, x))


