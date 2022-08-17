import datetime


def user_information(ussnm, pssd):		# pssd means password, ussnm is username
	print("Enter your details\n")
	name = input("Name: ")
	address = input("Address: ")
	age = input("Age: ")
	ussnm_ = ussnm + " task.txt"

	f = open(ussnm_, 'a')
	f.write(pssd)
	f.write("\nName: ")
	f.write(name)
	f.write('\n')
	f.write("Address :")

	f.write(address)
	f.write('\n')
	f.write("Age :")
	f.write(age)
	f.write('\n')
	f.close()


def view_data(username):
	ff = open(username, 'r')
	print(ff.read())
	ff.close()


def task_add(username):
	print("Please enter the number of tasks you want to add")
	j = int(input())
	f1 = open(username, 'a')

	for i in range(1, j + 1):
		task = input("Name of the task: ") + '\n'
		target = input("Target of this task: ")
		pp = "TASK " + str(i) + ' :'
		qq = "TARGET " + str(i) + " :"

		f1.write(pp)
		f1.write(task)
		f1.write('\n')
		f1.write(qq)
		f1.write(target)
		f1.write('\n')
		print("Please press space bar if you want to stop \notherwise press enter to continue adding tasks")
		s = input()
		if s == ' ':
			break
	f1.close()


def task_update(username):
	username = username + " TASK.txt"
	print("Please enter the tasks which are completed ")
	task_completed = input()

	print("Enter task which are still not started by you")
	task_not_started = input()

	print("Enter task which you are currently doing")
	task_ongoing = input()

	fw = open(username, 'a')
	dt = str(datetime.datetime.now())
	fw.write(dt)
	fw.write("\n")
	fw.write("COMPLETED TASK \n")
	fw.write(task_completed)
	fw.write("\n")
	fw.write("ONGOING TASK \n")
	fw.write(task_ongoing)
	fw.write("\n")
	fw.write("NOT YET STARTED\n")
	fw.write(task_not_started)
	fw.write("\n")


def task_status(username):
	ussnm = username+" TASK.txt"
	o = open(ussnm, 'r')
	print(o.read())
	o.close()


def signup():
	print("Please enter the user details by which you want to access your account")
	username = input("choose your username: ")
	password = input("choose your password: ")
	user_information(username, password)
	print("Congratulations on signing up!\nNow you can proceed to login.\n")
	login()


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

			if a == '1':
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
			print("Seems like you have entered wrong credentials.\n")
			print("Please enter the same login details as you have entered during your signup process")
			login()

	except Exception as e:
		print("Seems like you have entered wrong credentials.\n")
		print("Please enter the same login details as you have entered during your signup process")
		login()


def welcome():
	print("WELCOME TO PERSONALIZED TASK MANAGER\n\
	1--Signup\n\
	2--Login")
	a = int(input())
	if a == 1:
		signup()
	elif a == 2:
		login()
	else:
		print("Oops!\nSeems like you've entered wrong input.\nPlease select from above options i.e, 1 or 2")
		welcome()


if __name__ == '__main__':
	welcome()
