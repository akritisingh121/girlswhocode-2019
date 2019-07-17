

#ask player 1 for a secret word
#show player 2 the dashes

#ask player 2 for a letter
#figure out if the letter is correct or wrong
#figure out if the player wins or loses

print("Welcome to Hangman!")
secret_word = input("Player 1, please enter a secret word")
print("\n"*50)

dashes = []
for i in range(len(secret_word)):
	dashes.append("_")

print ("Your current word is: ", dashes)

lives = 5
while lives > 0:
	guess = input("Player 2, guess a letter")
	
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

