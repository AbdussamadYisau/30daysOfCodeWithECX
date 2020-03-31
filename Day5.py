"""
This function returns the nth faithful number
"""

import math


def faithful(n):
	if (n == 1): 
		return 1

	elif ((math.log(n)/math.log(2)) % 1 == 0):
		
		power = int((math.log(n)/math.log(2)) /1)
		retVal = int(math.pow(7,power))

		return(retVal)
		

	# Creating a set of dummy variable to handle cases beside when n is 1 or when n is a perfect 2
	prev = 1
	nex = 1
	diff = 0

	while nex < n:
		
		prev = nex
		nex = nex * 2
		

	diff = n - prev

	return(faithful(diff) + faithful(prev))


print(faithful(1))
print(faithful(2))
print(faithful(3))
print(faithful(4))
print(faithful(5))
print(faithful(6))
print(faithful(7))
print(faithful(8))
print(faithful(9))
print(faithful(10))


