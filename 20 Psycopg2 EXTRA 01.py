import psycopg2

# The connection class

# we have directly called the connection class in previous module.
# But we can also use it as a context manager.
# though the context manager dont close the connection automatically,
# but it is helpful to catagorize the operations occuring in each connection.

# I will not show you my pasword
import os
passw = os.environ.get("POSTGRES_PASSWORD")

with psycopg2.connect(host = "localhost", port = "5432", database = "test", user = "postgres", password = passw) as conn1:
    # now we can do specific stuffs
    cur = conn1.cursor()
    cur.execute("SELECT country_of_birth FROM person ORDER BY country_of_birth;")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    # closing the cursor
    cur.close()

    # we can cancel current database operation with cancel() method.
    # conn1.cancel()
    # And we also can reset the connection which will cancel all the new operations.
    # conn1.reset()

# rememeber to close the connection
conn1.close()
# we can see if the connection is closed or not
print(conn1.closed)



# The cursor class

# As we know, Allows Python code to execute PostgreSQL command in a database session.
# let us create a cursor first,
with psycopg2.connect(host = "localhost", port = "5432", database = "test", user = "postgres", password = passw) as conn2:
    cur2 = conn2.cursor()
    # we can see if the cursor is closed or not.
    print(cur2.closed)
    # we can see the connection which is related to this cursor.
    print(cur2.connection)
    # we can see the name of the cursor.
    print(cur2.name)
    # it will return None[Default] if it is a client side cursor.

    # closing the cursor.
    cur2.close()
    # we can't use that any more.


    cur3 = conn2.cursor()
    # executing a command
    cur3.execute("SELECT * FROM person;")
    print(cur3.fetchall())

    # execute manay commands
    # cur3.executemany()
    # but this function is too slow. 
    # So, the official documentation recommend to use the execute() command in a loop.
    cur3.close()

    # now we will learn about different types of fetch*() methods.
    cur4 = conn2.cursor()
    cur4.execute("SELECT * FROM person;")
    # fetchone() only fetch one row each time.
    print("\n")
    print(cur4.fetchone())
    print(cur4.fetchone())

    # fetchall() fetches all the existing rows at a time.
    print("\n")
    print(cur4.fetchall())

    cur4.execute("SELECT * FROM car;")
    # fetchmany() helps us to fetch mulple existing rows.
    print("\n")
    print(cur4.fetchmany(2))
    cur4.close()

    cur5 = conn2.cursor()
    cur5.execute("SELECT * FROM person;")
    # how many row()
    print(cur5.rowcount)

    # current row number (indexing starts with 0)
    print(cur5.rownumber)

    # id last row that was inserted?
    print(cur5.lastrowid)

    # see the query
    print(cur5.query)

    # see the status message?
    print(cur5.statusmessage)
    
    # commiting the result 
    conn2.commit()
    # remember to commit.

# closing the connection
conn2.close()