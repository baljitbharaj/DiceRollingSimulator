#importing the random module 
import random

#Set two variables (min and max), that will hold 1 and 6
min = 1
max = 6

#Create a flag if user would like to roll again
roll_again = "Yes"

#While Loop to generate random numbers as requested by the user
while roll_again == "Yes" or roll_again == "y" or roll_again == "yes":
	print("Rolling the dice")
	print("The results are...")
	print(random.randint(min,max))
	print(random.randint(min,max))

	roll_again = input("Roll the dice again?")
