"""
9/20/2018

Mad Libs!

The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. 
The program will first prompt the user for a series of inputs a la Mad Libs. 
For example, a singular noun, an adjective, etc. Then, once all the 
information has been inputted, the program will take that data and 
place them into a premade story template. You’ll need prompts for 
user input, and to then print out the full story at the end with 
the input included.

Concepts to keep in mind:

    Strings
    Variables
    Concatenation
    Print


A pretty fun beginning project that gets you thinking about how 
to manipulate userinputted data. Compared to the prior projects, 
this project focuses far more on strings and concatenating. 
Have some fun coming up with some wacky stories for this!


"""


while True:
	print("Welcome, ALL! We are going to write our own Mad Libs!")
	print("Let's begin!")

	adj1 = input("First adjective: ")
	adj2 = input("Second adjective: ")
	typeofbird = input("Type of Bird: ")
	RiaH = input("Room in a house: ")
	verPT = input("Verb (Past Tense): ")
	ver2 = input("Another Verb: ")
	relatives_name = input("A Relatives Name: ")
	noun = input("A Noun: ")
	liquid = input("A type of liquid: ")
	verbing = input("A verb ending in 'ing': ")
	body_part = input("A body part (plural): ")
	noun2 = input("Another noun (plural): ")
	verbing2 = input("A verb ending in 'ing': ")
	noun3 = input("And lastly, another noun: ")


	print("It was a {}, cold November day.".format(adj1))
	print("I woke up to the {} smell of {} roasting in the {} downstairs.".format(adj2, typeofbird, RiaH))
	print("I {} down the stairs to see if I could help {} the dinner.".format(verPT, ver2))
	print("My Mom said, 'See if {} needs a fresh {}.'".format(relatives_name, noun))
	print("So I carried a tray of glasses full of {} into the {} room.".format(liquid,verbing))
	print("When I got there, I couldn't believe my {}!".format(body_part))
	print("There were {} {} on the {}!".format(noun2, verbing2, noun3))

	replay = input("Do you want to play again? y/n :")

	if replay.lower() == 'y':
		print("Let's do it!")
		continue
	else:
		print("I don't like you either..")
		break

