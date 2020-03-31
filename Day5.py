"""
This function returns the nth faithful number
"""

import math


def faithful(n):
	if (n == 1): 
		print("1")

	elif (math.log(n)/math.log(2)) % 1 == 0:
		
		power = int((math.log(n)/math.log(2)) /1)
		retVal = int(math.pow(7,power))

		print(retVal)
		

	# Creating a set of dummy variable to handle cases beside when n is 1 or when n is a perfect 2
	prev = 1
	nex = 1
	diff = 0

	while nex < n:
		
		prev = nex
		nex = nex * 2
		

	diff = n - prev

	print(faithful(diff) + faithful(prev))


faithful(8)


