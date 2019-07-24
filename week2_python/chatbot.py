import random

# --- Define your functions below! ---
def introduction():
	introductions = ["Hello", "Hey there", "What's up"]
	greeting = random.choice(introductions)
	print(greeting)

def tell_joke():
	print("Unfinished")

def tell_random_fact():
	print("Unfinished")
	
# --- Put your main program below! ---
def main():
	while True:
		answer = input("Type something")
		if answer == "Hi":
			introduction()
		elif answer == "Tell me a joke":
			tell_joke()
		elif answer == "Tell me a random fact":
			tell_random_fact()
		else:
			print("Uhhhh idk what to say")
			


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
	main()