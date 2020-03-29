# Write a function which validates phone numbers

#Using regex

#Importing the module
# import re

# def isValid(s):
# 	#The string can begin with 0 or 234
# 	#Then, contains 7, 8 or 9
# 	# Then contains 

# #	Pattern = re.compile("(0/234)?[7-9][0-9]{9}")


# 	return Pattern.match(s)


# s = "2348123884098"

# if(isValid(s)):
# 	print("Valid number")
# else:
# 	print("Invalid number")


def is_Nigerian(phoneNum):
	telcoPrefixes = ["0703", "0706", "0803", "0806", "0810", "0813", "0814", "0816", "0903", "0705", "0805", "0811", "0815", "0905", "0701", "0708", "0802", "0808", "0812", "0902", "0809", "0817", "0818", "0909", "0804"]
	

	if(len(phoneNum) == 11 and phoneNum[0:4] in telcoPrefixes):
		return ("This phone number is valid" + ": " + phoneNum)
	elif (len(phoneNum) == 13 and phoneNum[0:3] == "234"):
		return ("This phone number is valid" + ": " + phoneNum)
	elif (len(phoneNum) == 14 and phoneNum[0:4] == "+234"):
		return ("This phone number is valid" + ": " + phoneNum)
	elif (len(phoneNum) == 14 and phoneNum[0:4] == "2340"):
		return ("This phone number is valid" + ": " + phoneNum)
	elif (len(phoneNum) == 15 and phoneNum[0:5] == "+2340"):
		return ("This phone number is valid" + ": " + phoneNum)
	
	else:
		return("Invalid phone number" + ": " + phoneNum)



print(is_Nigerian("23408123884098"))
print(is_Nigerian("2348123884098"))
print(is_Nigerian("+2348123884098"))
print(is_Nigerian("+23408123884098"))
print(is_Nigerian("08123884098"))


