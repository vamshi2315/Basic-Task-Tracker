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
