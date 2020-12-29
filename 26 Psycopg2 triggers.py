# well if we want to use triggers withut pl/pgsql that will be difficult and hard coded in python.
# here is an example of before trigger. in this we have to work with the inputs before executing the operation into the DB
# For after trigger we need to add the function after the coonection is commited as we need to work after the operation.
# For instead of trigger we need to change the behaviour of the operation but it is not usually done.

# here we used the for each row appproach
# for each statement approach is little different. 
# it wont matter if we inserted single or multiple operation in one statement.
# it will be only executed once per a statement like logging.

import os
import psycopg2
passw = os.environ.get("POSTGRES_PASSWORD")

initial_names = []
initial_marks = []
initial_gpa = []

def trigger_function(name,marks):
	triggerred_name = name.strip().title()
	triggerred_marks = marks * 2
	if triggerred_marks >= 1000:
		triggerred_gpa = "A"
	elif triggerred_marks < 1000 and triggerred_marks >= 800:
		triggerred_gpa = "B"
	else:
		triggerred_gpa = "C"
	
	return (triggerred_name, triggerred_marks, triggerred_gpa)

def asking_info():
	users_num = int(input("NUMBER OF USERS: "))
	for user in range(users_num):
		print()
		name = input("NAME: ")
		marks = int(input("MARKS: "))
		triggerred_name, triggerred_marks, triggerred_gpa = trigger_function(name,marks)

		initial_names.append(triggerred_name)
		initial_marks.append(triggerred_marks)
		initial_gpa.append(triggerred_gpa)
	print("\nSUBMISSION SUCCESSFUL :)\n")
	return (initial_names,initial_marks,initial_gpa)

def adding_info_to_db(initial_names,initial_marks,initial_gpa):
	with psycopg2.connect(host = "localhost", port = 5432, database = "test", user = "postgres", password = passw) as conn1:
		cur0 = conn1.cursor()
		cur0.execute("""
			DROP TABLE IF EXISTS student;
			""")
		conn1.commit()

		cur0.execute("""
			CREATE TABLE student (
				id SERIAL NOT NULL PRIMARY KEY,
				name TEXT NOT NULL,
				marks INT NOT NULL,
				gpa TEXT NOT NULL );
			""")
		conn1.commit()
		cur0.close()


		cur1 = conn1.cursor()
		for i in range(len(initial_names)):
			cur1.execute("""
				INSERT INTO student (name, marks, gpa) VALUES (%s, %s, %s); 
				""", (initial_names[i],initial_marks[i], initial_gpa[i]))
			print(cur1.statusmessage)
		cur1.close()
		conn1.commit()
		print("\n INSERTATION COMPLETED :)")
	conn1.close()


adding_info_to_db(*asking_info())





# testing
if __name__ == "__main__":
	print("\n\n\nTESTING...\n")
	with psycopg2.connect(host = "localhost", port = 5432, database = "test", user = "postgres", password = passw) as test_conn:
		test_cur = test_conn.cursor()
		test_cur.execute("""
			SELECT * FROM student
			""")
		rows = test_cur.fetchall()
		for row in rows:
			print(row[0], "->", row[1], "->", row[2], "->", row[3])
		test_cur.close()
	test_conn.close()