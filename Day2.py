# Password generator
import random

def password_generator(passLength):
	#Create characters, from which letters that make the password would be chosen from 
	chars = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#}$]%^&*()_+={[?/;:<>"

	#Create a password variable to store the generated password
	password = " "

	if passLength < 8:
		print("This password is weak")
	#Based on the length, start picking elements randomly
	for i in range(passLength):
		password = password + random.choice(chars)


	return (password)

print("How long would you like your password to be? How many characters? ")
passLength = input()
passLength = int(passLength)
print(password_generator(passLength))
