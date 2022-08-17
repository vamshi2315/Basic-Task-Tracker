import datetime

#Now we will create a ‘user_information’ function which will take the data from the ‘signup’ function and make a text file to save the user data. 
#The below code will show how things will proceed.


def user_information(ussnm, pssd):		# pssd means password, ussnm is username
	print("Enter your details\n")
	name = input("Name: ")
	address = input("Address: ")
	age = input("Age: ")
	ussnm_ = ussnm + " task.txt"		#creating a text fil with name of the user as the name of the file

	f = open(ussnm_, 'a')		#storing all the user information in that file
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
