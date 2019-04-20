"""
9/20/2018

Hangman!

The Goal: Despite the name, the actual “hangman” part isn’t necessary. 
The main goal here is to create a sort of “guess the word” game. The 
user needs to be able to input letter guesses. A limit should also 
be set on how many guesses they can use. This means you’ll need a 
way to grab a word to use for guessing. (This can be grabbed from 
a pre-made list. No need to get too fancy.) You will also need functions
to check if the user has actually inputted a single letter, to 
check if the inputted letter is in the hidden word (and if it is, 
how many times it appears), to print letters, and a counter variable 
to limit guesses.

Concepts to keep in mind:

    Random
    Variables
    Boolean
    Input and Output
    Integer
    Char
    String
    Length
    Print


"""

import random



def check_guess(letter):
	for ind,x in enumerate(ran_word):
		if x == letter:
			dsp_word[ind] = letter


while True:

	print("\n" *30)

	words = ["jazz", "buzz", "jazzed", "jinx", "runaway"]
	random.shuffle(words)
	ran_word = words.pop()

	dsp_word = ["_"]*len(ran_word)
	wrg_str = ""
	count = 0
	playing = True

	print("\tWelcome to Hangman!")
	print("\tYour word is {} letters long! and you have 7 tries to figure it out!".format(len(ran_word)))

	while count < 7 or playing == False:
		print("\n")
		print("\t {}".format(" ".join(dsp_word)))
		print("\n")

		print("\tThings you've guessed wrong: {}".format(wrg_str))
		guess = input("What's your guess?  ")

		if len(guess) == 1:
			if guess in ran_word:
				check_guess(guess)
				if "".join(dsp_word) == ran_word:
					print("\tYou've won!")
					print("\tThe word is {}!".format(ran_word))
					break
				continue
			else:
				print("\tYou'll have to try again if you want to win.")
				wrg_str += " {} ".format(guess)
				count += 1
				print("\tYour count is now at {}!".format(count))
		else:
			if guess == ran_word:
				print("\tYou've won!")
				print("\tThe word is {}!".format(ran_word))
				break
			else:
				print("\tNot even close, bby!")
				wrg_str += " {} ".format(guess)
				count += 1

				print("\tYour count is now at {}!".format(count))

	if count == 7:
		print("\tWow.. Of course you lost.")
		print("\tThe word is {}!".format(ran_word))

	replay = input("Would you like to play again? y/n:")

	if replay.lower() == "y":
		print("\tNice, let's do it.")
		continue
	else:
		print("\tWhatever.")
		break