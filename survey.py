import json

def ask_questions():
	questions = ["What is your date of birth? (MM/DD/YYYY)", "What is your age?", "Where do you call home? (City, State, Country)", "How many people live in your home more than 50% of the time?", "How many hours per week do you spend on the phone?", "Name the app, program, or website that you use most frequently."]
	responses = {}
	for i in range(len(questions)):
		answer = input(questions[i])
		responses[i] = answer

	print("Here are all your responses: \n ")
	print(responses)

	return responses

def save_file(filename, dictionary):
	with open(filename, 'w') as f:
		json.dump(dictionary, f)

def read_file(filename):
	if filename:
		with open(filename, 'r') as f:
			responses_read = json.load(f)
		return responses_read

def run_survey():
	survey = {}
	while True:
		name = input("What is your name?")
		responses = ask_questions()
		survey[name] = responses
		again = input("Do you want to survey another person?")
		if again == "yes":
			print("Your current survey dictionary looks like: \n")
			print(survey)
			continue
		else:
			break
	return survey



survey = run_survey()

save_file("survey.txt", survey)
dictionary = read_file("survey.txt")
print(dictionary)