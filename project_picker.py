import csv
import random
import sys
import getch

try:
	command = sys.argv[1]
except IndexError:
	print('Missing command')
	print('Try list for a list and usage of valid commands')
	exit()
#print(command)

if command == 'add':

	try:
		string = sys.argv[2]
	except IndexError:
		print('Missing project name')
		print('Try list for a list and usage of valid commands')
		exit()

	print('Do you wish to add "', string, '"to project list(y/n)?')
	acceptance = getch.getch()

	if acceptance == 'y' or acceptance =='Y':

		with open('project_list.csv', mode='a+') as project_list:
			project_writer = csv.writer(project_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			project_writer.writerow([string])
	else:
			print('Aborted..')

elif command == 'pick':
	projects = list(csv.reader(open('project_list.csv',"r")))

	if len(projects) != 0:
		project_name = random.choice(projects)
		
		print('Chosen project is: ', project_name)
		print('Do you accept this quest(y/n)?')
		acceptance = getch.getch()

		if acceptance == 'y' or acceptance =='Y':
			projects.remove(project_name)

			with open('project_list.csv', mode='w') as project_list:
				project_writer = csv.writer(project_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				
				for project in projects:				
					project_writer.writerow(project)
		else:
			print('Aborted..')

elif command == 'list':
	print('Command List:')
	print('add - Use to add a new project to the list\n \tSyntax - python3 project_picker.py add "project_name"')
	print('list - Use to see a list of commands\n \tSyntax - python3 project_picker.py list')
	print('pick - Use to select a project to work on\n \tSyntax - python3 project_picker.py pick')

else:
	print('Invalid choice')
	print('Try list for a list and usage of valid commands\n')

