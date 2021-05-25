a_dict = {}
while True:
	print("!!!***Searching and saving the birthdays***!!!")
	print("1. Show all the Birthdays which are saved")
	print("2. Add a new Birthday to the list")
	print("3. Finish and exit")
	option = int(input("Enter your chioce: "))
	if option == 1:
		if len(a_dict.keys()) == 0:
			print("No Birthday is added here")	
		else:
 			person_name = input("Enter the name of person: ")
			birth_date = a_dict.get(person_name,"We have no data for this person")
			print(birth_date)
	elif option == 2:
		person_name = input("Enter the person's name to be saved: ")
		birth_date = input("Enter the birth date: ")
		a_dict[person_name] = birth_date
		print("Birthday added succeddfully")
			
	elif option == 3:
		print("Thanks for saving the birthdays!!!")
		break
	else:
		print("You have chosen the invalid option")