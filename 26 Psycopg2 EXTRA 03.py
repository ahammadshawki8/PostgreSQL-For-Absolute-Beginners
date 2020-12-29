# Few more basic module usages

import psycopg2
import os
passw = os.environ.get("POSTGRES_PASSWORD")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
with psycopg2.connect(host = "localhost", port = "5432", database = "test", user = "postgres", password = passw) as conn1:
    cur1 = conn1.cursor()
    cur1.execute("DROP TABLE tab_test;")
    cur1.execute("""
        CREATE TABLE tab_test ( 
        id SERIAL NOT NULL PRIMARY KEY,
        salary INT NOT NULL,
        name VARCHAR(15) NOT NULL);
        """)
    cur1.close()
    conn1.commit()
    
    cur2 = conn1.cursor()
    cur2.execute("INSERT INTO tab_test (salary, name) VALUES (%s, %s)", (10000, "Ahammad Shawki"))
    print(cur2.statusmessage)
    cur2.close()
    conn1.commit()
    # basically the advantage of using place holders is that they works like variables.
    # and we can change the value continuosly and use the same chunck of code.
    # NOTE that the placeholders second arguement must be a tuple or list.
    # so if we have only one element, we can use (elem,) or [elem]

    salary_list = [10, 20, 30, 40, 50]
    name_list = ["Mr. X", "Mr. Y", "Mr. Z", "Mr. A", "Mr. B"]
    cur3 = conn1.cursor()
    for i in range(len(name_list)):
        cur3.execute("INSERT INTO tab_test (salary, name) VALUES (%s, %s)", (salary_list[i], name_list[i]))
        print(cur3.statusmessage)
        conn1.commit()
    cur3.close()

    # now lets see our database,
    print()
    cur4 = conn1.cursor()
    cur4.execute("SELECT * FROM tab_test;")
    rows = cur4.fetchall()
    for row in rows:
        print(str(row[2]) + "  <-->  " + str(row[1]))
    cur4.close()

    # but in SQL, we use % for modulo and in psycopg2 we use it for place holder.
    # so their is one problem remaining.
    # what if we want to use % for modulo in one of the SQL commands. 
    # we can use it easily.
    cur5 = conn1.cursor()
    cur5.execute("SELECT 4 % 2")
    print(cur5.fetchall())
    cur5.close()

    # but if we want to add placeholders and modulo at the same command.
    # we have put another % before the modulo %, more like backslash\
    # now lets look at this complex example.
    cur6 = conn1.cursor()
    numbers = [1,2,3,4,5,6,7,8,9]

    print("IsEven")
    print("------")
    for num in numbers:
        cur6.execute("SELECT %s %% 2 = 0 AS even", (num,))
        print(cur6.fetchall()[0][0])
        # first [0] is for fetching the first tuple and
        # second [0] is for fetching the first value of that tuple.
        cur6.close()
        cur6 = conn1.cursor()
    cur6.close()

    # we can only use the placeholders for query values, 
    # we cant insert table name or field name using it.
    # for inserting table or firld name in the SQL command we need to use format() method.
    cur7 = conn1.cursor()
    blah_text = "tab_test (salary , name)"
    salary_list = [100, 200, 300]
    name_list = ["Mr. C", "Mr. D", "Mr. E"]
    for i in range(len(name_list)):
        cur7.execute(("INSERT INTO {} VALUES (%s, %s)".format(blah_text)), (salary_list[i], name_list[i]))
        print(cur7.statusmessage)
        conn1.commit()
    cur7.close()

    # now we can see if the insertation works or not.
    print()
    cur8 = conn1.cursor()
    cur8.execute("SELECT * FROM tab_test ORDER BY salary DESC;")
    rows = cur8.fetchall()
    for row in rows:
        print(str(row[2]) + "  <-->  " + str(row[1]))
    cur8.close()
    
conn1.close()

# We have also different adaptation of 
# Python Datatypes, integers, constant, strings, date-time etc adapations
# to SQL 
# to learn more about adaptations visit this page,
"""https://www.psycopg.org/docs/usage.html"""

# There are few more Advanced topics covered in psycopg2 official docs.
# I won't describe them in this module now.
# So, you should read the official docs,
"""https://www.psycopg.org/docs"""