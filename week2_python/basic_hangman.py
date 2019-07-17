

#ask player 1 for a secret word
#show player 2 the dashes

#ask player 2 for a letter
#figure out if the letter is correct or wrong
#figure out if the player wins or loses

print("Welcome to Hangman!")
secret_word = input("Player 1, please enter a secret word \n")
print("\n"*50) #shift the screen down

dashes = [] #dashes will store the current word with all the player's guesses so far
for i in range(len(secret_word)):
	dashes.append("_")

print ("Your current word is: ", dashes)

lives = 5
while lives > 0:
	print( "\n"*5 + "-------------------------------------------------") #to separate different rounds of the game
	guess = input("Player 2, guess a letter \n")
	
	if guess in secret_word: #if the guess is correct
		print("You got a letter! You have ", lives, "lives left")
		
		#update dashes, and print updated values
		for i in range(len(secret_word)):
			letter = secret_word[i] 
			if letter == guess:
				dashes[i] = guess #replace the dash with the correct letter
	
	if guess not in secret_word: #if the guess is incorrect
		lives = lives - 1
		print("You're wrong. You have ", lives, "lives left")
		
	if list(secret_word) == dashes:
		print("Congratulations, you won hangman!")
		break
	
	print(dashes)
	
if lives == 0:
	print("You lose!")		

