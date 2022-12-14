# Now we are ready to code our software. Initially, we will start by creating our sign-up function. 
#The signup function will be taking the username by which the user is going to make his/her account and ask to set a password for that account.
def signup():
	print("Please enter the user details by which you want to access your account")
	username = input("choose your username: ")
	password = input("choose your password: ")
	user_information(username, password)		#taking user info
	print("Congratulations on signing up!\nNow you can proceed to login.\n")
	login()

#The log-in function will take the username and ask for the password connected to it. 
#Once the user enters the password the function will check if the password saved in the text file is the same as that entered.
def login():
	print("Please enter your username and password to login to your account")
	user_nm = input("username: ") + '\n'
	pssd_wr = (input("password:")) + '\n'
	try:
		usernm = user_nm + " task.txt"
		f_ = open(usernm, 'r')
		k = f_.readlines(0)[0]		# variable 'k' contains the password as saved in the file
		f_.close()

		if pssd_wr == k:		# Checking if the Password entered is same as the password saved while signing in
			print(
				"Welcome to your personalized task tracker!\n \
				Please choose from below options:\n \
				1--View personal data\n \
				2--New task\n \
				3--Update current tasks\n \
				4--Status of tasks")
			a = input()

			if a == '1':						#lets user to choose from varous options
				view_data(usernm)
			elif a == '2':
				task_add(usernm)
			elif a == '3':
				task_update(user_nm)
			elif a == '4':
				task_status(user_nm)
			else:
				print("Wrong input ! Please select one of the options form above mentioned i.e, either 1 or 2 or 3 or 4")
		else:
			print("Seems like you have entered wrong credentials.\n")	#when wrong password is entered
			print("Please enter the same login details as you have entered during your signup process")
			login()		#lets user to try again

	except Exception as e:
		print("Seems like you have entered wrong credentials.\n")
		print("Please enter the same login details as you have entered during your signup process")
		login()		#lets user to try again

