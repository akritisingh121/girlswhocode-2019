

#ask player 1 for a secret word
#show player 2 the dashes

#ask player 2 for a letter
#figure out if the letter is correct or wrong
#figure out if the player wins or loses

play_again = True
while play_again == True:

	wrong_guesses = [] #stores all the incorrect guesses so far
	allowed_characters = "abcdefghijklmnopqrstuvwxyz" #all the letters a user is allowed to type

	print("Welcome to Hangman!")
	secret_word = input("Player 1, please enter a secret word \n")
	print("\n"*50) #shift the screen down

	dashes = [] #dashes will store the current word with all the player's guesses so far
	for i in range(len(secret_word)):
		dashes.append("_")

	print ("Your current word is: ", dashes)

	lives = 5
	while lives > 0:

		print( "\n"*3 + "-------------------------------------------------") #to separate different rounds of the game
		
		guess = input("Player 2, guess a letter or the entire word. \n")
		
		#don't allow invalid user inputs
		if len(guess) == 1 and guess not in allowed_characters: #if the guess is not a valid guess (a number, punctuation, etc.)
			print("That's not allowed. Guess again.")
			continue
		elif len(guess) != 1 and len(guess) != len(secret_word): #if the guess is a string of random characters
			print("That's not allowed. Guess again.")
			continue

		if guess in wrong_guesses or guess in dashes: #if you've already guessed this
			print("You've already guessed that. Guess again.")
			continue

		if guess in secret_word: #if the guess is correct

			if guess == secret_word: #if you guess the entire word
				print("Congratulations, you guessed the word! You won hangman!")
				break
			#if you guess a correct letter
			print("You got a letter! You have ", lives, "lives left")
			
			#update dashes, and print updated values
			for i in range(len(secret_word)):
				letter = secret_word[i] 
				if letter == guess:
					dashes[i] = guess #replace the dash with the correct letter
		
		elif guess not in secret_word or guess != secret_word: #if the guess is incorrect
			lives = lives - 1
			wrong_guesses.append(guess)
			print("You're wrong. You have ", lives, "lives left")
			
		if list(secret_word) == dashes:
			print("Congratulations, you won hangman!")
			break
		
		print("Your incorrect guesses are: ", wrong_guesses)
		print("Your word so far is: ", dashes)
		
	if lives == 0:
		print("You lose!")	

	answer = input("Do you want to play again? Enter 'yes' or 'no' \n")
	if answer == "yes":
		play_again = True
		print("\n"*50)
	if answer == "no":
		play_again = False

print("Goodbye!")