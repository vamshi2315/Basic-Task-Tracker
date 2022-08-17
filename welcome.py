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
