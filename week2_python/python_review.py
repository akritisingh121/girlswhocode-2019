#1
def number_1():
	count = 7
	if count < 10:
		print("cool")
	else:
		print("nice")

#2
def number_2():
	lives = 5
	while lives > 0:
		lives = lives - 1
		print("Lives = ", lives)

#3
def number_3():
	for i in range(6,9):
		i = i + 2
		print("i = ", i)

#4
def number_4():
	i = 1
	while i < 64:
		i = 1
		if i == "4":
			print("yay")
		else:
			print("i = ", i)
		i = i * 2

#5
toppings = ["onion", "pepperoni", "olives", "peppers"]
def number_5():
	for topping in toppings:
		print(topping)
		

def number_6():
	i = len(toppings)-1 #initializing i
	#count down starting from length up until 0
	while i >= 0:
		print(toppings[i])
		i = i - 1 #updating i, could write i -= 1





list1 = ["Funmi", "Franyi", "Asanti", "Sika", "Angel"]

def find_length_of_list():
	#count items in list
	counter = 0 #initialized counter
	for name in list1:
		counter = counter + 1 #updating counter
	
	print(counter)
		

def create_to_do_list():
    #user enters a task
	#task gets saved into a list
	to_do_list = [] #create an empty list
	
	while True: #forever loop
		task = input("Add a task") #asks the user to input a task repeatedly
		to_do_list.append(task) #keep adding tasks to the list
		
		print(to_do_list)
		break


def find_sum(list_of_numbers):
	total = 0 #initialized counter
	for num in list_of_numbers:
		total = total + num
	return(total)
	
def find_average(list_of_numbers):
	#sum together list_of_numbers
	total_amount = find_sum(list_of_numbers)
	average = total_amount / len(list_of_numbers)
	return(average)
	

print(find_average([66, 77, 35, 37]))












