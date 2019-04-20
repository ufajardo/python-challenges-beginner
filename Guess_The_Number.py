"""
9/19/2018

Guess the number!

The Goal: Similar to the first project, this project 
also uses the random module in Python. The program will 
first randomly generate a number unknown to the user. 
The user needs to guess what that number is. (In other 
words, the user needs to be able to input information.) 
If the user’s guess is wrong, the program should return 
some sort of indication as to how wrong (e.g. The number 
is too high or too low). If the user guesses correctly, 
a positive indication should appear. You’ll need 
functions to check if the user input is an actual 
number, to see the difference between the inputted 
number and the randomly generated numbers, and to 
then compare the numbers.

Concepts to keep in mind:

    Random function
    Variables
    Integers
    Input/Output
    Print
    While loops
    If/Else statements


Jumping off the first project, this project continues 
to build up the base knowledge and introduces user-inputted 
data at its very simplest. With user input, we start to get 
into a little bit of variability.



"""

import random



def guess_the_num():
	print("Time for another game of GUESS THE NUMBER!!")
	print("You will have 3 chances to guess a number between 1 and 10!")
	print("Let's begin!")

	guess_try = 0

	game = True
	randnum = random.randint(1, 10)

	while game:

		num = int(input("What number do you think it is? "))

		if guess_try == 2:
			print("You blew it.")
			print("The number was {}".format(randnum))
			game = False
		else:
			if not num == randnum:
				if num > randnum:
					guess_try += 1
					print("Oh no! Your number is too HIGH.")
					print("You have {} more trys!".format(abs(guess_try-3)))
				else:
					guess_try += 1
					print("JESUS. Your number is too low.")
					print("You have {} more trys!".format(abs(guess_try-3)))
			else:
				print("Congratulations.. it only took you {} time(s) to guess {}!".format(guess_try, randnum))
				game = False





while True:
	guess_the_num()

	replay = input("Want to play again?")
		
	if replay.lower()[0] == 'y':
		print("Great choice!")
		continue
	else:
		print("I see how it is..")
		break
