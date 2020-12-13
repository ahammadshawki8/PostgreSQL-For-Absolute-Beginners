# in this modeule, we will see how to use postgresql with python.

# we can use postgres with python with 2 methods,
	# 1. using the os module.
	# 2. using the psycopg2 module.
# But os module do the same work if we try to do with postgres itself.
# so, if we want to grab the values, pplay with them and finally save them using python, 
# we need to use psycopg2 module.

# so first lets install that with pip.
"""pip install psycopg2"""

# now lets import psycopg2 module
import psycopg2

# first lets see what functions we hava in this libaray.
#print(dir(psycopg2))

# we can see that we have
['BINARY', 'Binary', 'DATETIME', 'DataError', 'DatabaseError', 'Date', 'DateFromTicks', 'Error', 'IntegrityError', 
'InterfaceError', 'InternalError', 'NUMBER', 'NotSupportedError', 'OperationalError', 'ProgrammingError', 'ROWID', 
'STRING', 'Time', 'TimeFromTicks', 'Timestamp', 'TimestampFromTicks', 'Warning', '__builtins__', '__cached__', 
'__doc__', '__file__', '__libpq_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 
'__version__', '_connect', '_ext', '_json', '_psycopg', '_range', 'apilevel', 'compat', 'connect', 'errors', 'extensions', 
'paramstyle', 'threadsafety', 'tz']

# I will not show you my pasword
import os
passw = os.environ.get("POSTGRES_PASSWORD")

# first lets connect to our database,
connection = psycopg2.connect(host = "localhost", port = "5432", user = "postgres", password = passw, database = "test")

# all the commands of postgre we can pass through cursors.
# so lets create a cursor
cursor = connection.cursor()

# ***QUERY
# now lets start querying. we can do that with execute() command.
cursor.execute("SELECT * FROM person;")
# this line wont give us the rows.

# for printing rows we can use fetchall() command. 
rows = cursor.fetchall()
# this is a iterable.
for row in rows:
	print(row)
# we can see we have successfully printed the rows.
# the rows are actually tuples.


# ***INSERT
# now lets do insert.
cursor.execute("INSERT INTO person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) \
	VALUES (uuid_generate_v4(), 'Ahammad', 'Shawki', 'Male', 'ahammadshawki8@gmail.com', DATE '2004-12-28', 'Bangladesh');")
# now lets again see the table.
print("\n")
# we cant fetch again if we've already fetched from that cursor.
cursor2 = connection.cursor()
cursor2.execute("SELECT * FROM person;")
rows = cursor2.fetchall()
for row in rows:
	print(row)
# but all that stuffs we've done here won't be saved because we need to commit our results.
connection.commit()
# By default, Psycopg opens a transaction before executing the first command: 
# if commit() is not called, the effect of any data manipulation will be lost.
# The connection can be also set in “autocommit” mode: 
# no transaction is automatically open, commands have immediate effect.
# NOTE: NOT to use autocommit is recommanded because if it is on, 
# then there will be a huge probability of losing db data of production.

# lets do another quick change to our person table.
cursor3 = connection.cursor()
cursor3.execute("UPDATE person SET country_of_birth = 'America' WHERE first_name = 'Ahammad';")
# what if we change our mind and we dicided not to commit this transaction.
# for this reason we can use rollback() method.
connection.rollback()
# It will not commit the transaction, 
# it will roll back to the first of the transaction and close that transaction.
# the method is automatically called if an exception is raised.

# after we done with our cursor we need to close the cursor,
cursor.close()
# after our work we neeed to close the connection.
connection.close()
# Closing a connection without committing the changes,
# will cause an implicit rollback() to be performed.

# we will go little deeply in psycopg2 module using their official documentation in next module.