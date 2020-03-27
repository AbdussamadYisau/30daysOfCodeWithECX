#Using binary search algorithm to check if a number exists in a list

# Doing this with recursion
def bin_searchR(numList, num, low = 0, high = None):
	#Sorting the list
	numList = sorted(numList)

	if high is None: 
		high = len(numList) - 1

	# Create a variable to represent the binary respone that the function gives
	found = False

	#Edge case
	if low > high: 
		return found

	#Create a variable which represents the middle index at any given time
	mid = (low + high) // 2

	if num == numList[mid]:
		found = True
		return found
	else:
		if num < numList[mid]:
			return (bin_searchR(numList,num,low, mid - 1))
		else:
			return(bin_searchR(numList, num, mid + 1, high))

    
   

arr = [1,2,3,4,5,6]

x = 78

print(bin_searchR(arr,x))



# Then, doing it iteratively 

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


