def sieve_of_eratos(n):
	"""
	The Sieve of Eratosthenes is a technique that was developed
	more than 2,000 years ago to easily find all of the prime
	numbers between 2 and some limit

	Input: 20
	Output: 2,3,5,7,11,13,17,19


	"""
	nonPrimeList = []
	primeList = []

	if n <= 2:
		return primeList

	else:

		for num in range(2, n):
			if num not in nonPrimeList:
				primeList.append(num)

				# The following line marks out all multiples of the number that has been appended to prime list.

				for ele in range(num*num, n, num):
					nonPrimeList.append(ele)

	return(primeList)


print(sieve_of_eratos(20))
