def compressor(nums):
    """
    The compressor function takes in a string of numbers as its parameter,
    and returns a tuple of tuple, with each subtuple containing a number in the string as the 
    first element and the number of times it appears as the second element.

    Eg

    Input - 11111222222333333
    Output - ((1, 5), (2, 6), (3, 6))
    
    """

    count = {}

    for i in nums:
        count[i] = count.get(i,0) + 1
    answer = [(int(k),v) for k,v in count.items()]

    answer = tuple(answer)

    return answer

print(compressor("11111222222333333"))

