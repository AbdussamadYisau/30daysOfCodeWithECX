# # This function returns the nth faithful number

# def faithful(n):

# 	pow = 0
# 	answer = 1


# 	#Go through every n - like recursion
# 	while(n):

# 		pow = pow * 7

# 		#If n is an odd number

# 		if (n % 2 != 0):
# 			answer = answer + pow 


# 		# This next line of code handles decimals (should there be any)

# 		n >>=  1

# 	return answer



# print(faithful(1))
for _ in range(1, 10):
    n = int(input())
    a = []
    while(n>0):
        x = int(math.log(n,2))
        n-=(2**x)
        a.append(x)
    summ=0
    for i in a:
        summ+=(7**i)
    print(summ)
