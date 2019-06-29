#Generates a random user password that includes
#characters from user's name and birth year

import random


first = str(input("Enter your First Name: "))
last = str(input("Enter your Last Name: "))
year = str(input("Enter your Birth year: "))

# join all the user chars
characters = first + last + year 

# add extra chars
extra = '%&*$@!'

# put them all in a list
pw = list(characters + extra)
pw_length = 16
chars = []

# for however many characters....
for character in range(pw_length):

	# choose a random one and  
	# add it to the chars list
	chars.append(random.choice(pw))

# join them all back together
charstr = ''.join(chars)

print("Thanks {}".format(first.capitalize()))
print("Your new password is: {}".format(charstr.upper()))
