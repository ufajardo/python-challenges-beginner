"""


9/19/2018

This is the first Dice Rolling py file for testing. This seems
like a general idea, so it may not need anything more than just
one file. 

The Goal: Like the title suggests, this project involves writing a 
program that simulates rolling dice. When the program runs, it will 
randomly choose a number between 1 and 6. (Or whatever other integer 
you prefer — the number of sides on the die is up to you.) The program 
will print what that number is. It should then ask you if you’d like 
to roll again. For this project, you’ll need to set the min and max 
number that your dice can produce. For the average die, that means 
a minimum of 1 and a maximum of 6. You’ll also want a function that 
randomly grabs a number within that range and prints it.

Concepts to keep in mind:

    Random
    Integer
    Print
    While Loops


A good project for beginners, this project will help establish a 
solid foundation for basic concepts. And if you already have 
programming experience, chances are that the concepts used in 
this project aren’t completely foreign to you. Print, for example, 
is similar to Javascript’s console.log.


"""

import random


def rolling_dice():
	rolling = True

	print("Welcome to dice rolling simulator!")

	while rolling:


		answer = input("Ready to roll some dice?")

		if answer.lower()[0] == 'y':
			print("Let's roll!")
			 
			print("Looks like you rolled: {}".format(random.randint(1,6)))

		else:
			print("Oh, sorry to hear. :c ")
			rolling = False


rolling_dice()



