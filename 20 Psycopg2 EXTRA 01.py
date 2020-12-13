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

# closing the connection
conn2.close()