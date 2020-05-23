import csv
import random

print('Select an action:\n')
print('1. Add a new project\n')
print('2. Draw a project\n')
choice = raw_input()

if choice == '1':

	string = raw_input('Enter project name: ')

	with open('project_list.csv', mode='a+') as project_list:
		project_writer = csv.writer(project_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		project_writer.writerow([string])

elif choice == '2':
	projects = list(csv.reader(open('project_list.csv',"r")))
	project_name = random.choice(list(projects))
		
	print('Chosen project is: ', project_name)
	acceptance = raw_input('Do you accept this quest(y/n)?')

	if acceptance == 'y' or acceptance =='Y':
			projects.remove(project_name)

			with open('project_list.csv', mode='w') as project_list:
				project_writer = csv.writer(project_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				
				for project in projects:				
					project_writer.writerow(project)
	else:
			print('n')

else:
	print('Invalid choice\n')
