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
