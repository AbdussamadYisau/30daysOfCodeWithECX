# This code returns the power set of a particular list, in the form of sublists.


def power_list(arr):
	powerSet = [[]]

	for num in arr:
		#Iterate over the sub sets so far

		for subSet in powerSet:
			# Add a new subset consisting of the subset at hand

			powerSet = powerSet + [list(subSet) + [num]]
		

	return(powerSet)


print(power_list([2,4,6]))

