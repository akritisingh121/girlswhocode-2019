# import json

# dic = {"apple":"red", "banana":"yellow", "hi":5}
# json_dic = json.dumps(dic)

# with open("this_is_a_json.txt", 'w') as f:
#     json.dump(dic, f)

questions = ["What is your name?", "What is your date of birth? (MM/DD/YYYY)", "What is your age?", "Where do you call home? (City, State, Country)", "How many people live in your home more than 50% of the time?", "How many hours per week do you spend on the phone?", "Name the app, program, or website that you use most frequently."]
responses = {}
for i in range(len(questions)):
	answer = input(questions[i])
	responses[i] = answer

print("Here are all your responses: \n ")
print(responses)

