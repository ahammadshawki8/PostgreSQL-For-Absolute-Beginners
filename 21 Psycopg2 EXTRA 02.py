import psycopg2
import os
passw = os.environ.get("POSTGRES_PASSWORD")

# Copying Data From file to Database.
with psycopg2.connect(host = "localhost", port = "5432", database = "test", user = "postgres", password = passw) as conn3:
    cur7 = conn3.cursor()
    
    # Importing data from a csv file.
    with open("F:\\Study_Work\\Python\\Python WorkSpace\\17. PostgreSQL\\# Created Files\\results.csv") as file:
        file.readline()
        cur7.execute("CREATE TABLE result ( \
        id BIGSERIAL NOT NULL PRIMARY KEY, \
        first_name VARCHAR(75) NOT NULL, \
        last_name VARCHAR(75) NOT NULL, \
        gender VARCHAR(75) NOT NULL, \
        email VARCHAR(75), \
        date_of_birth DATE NOT NULL, \
        country_of_birth VARCHAR(75) NOT NULL, \
        car_id VARCHAR(100), \
        make VARCHAR(75), \
        model VARCHAR(75), \
        price VARCHAR(1000) \
        );")
        cur7.copy_from(file, table = "result", sep = ",", null= 'null', columns = ("id","first_name","last_name","gender","email","date_of_birth","country_of_birth","car_id","make","model","price"))
        cur7.execute("SELECT * FROM result;")
        print(cur7.fetchall())
        cur7.close()
    conn3.commit()

    # Exporting data to a csv file,
    # well we can do that with SQL directly, that would be lot more easier.
    # But lets see how to do that in psycopg2.
    with open("F:\\Study_Work\\Python\\Python WorkSpace\\17. PostgreSQL\\# Created Files\\toResults.csv", "w") as write_file: 
        cur8 = conn3.cursor()
        write_file.write("id,first_name,last_name,gender,email,date_of_birth,country_of_birth,car_id,make,model,price\n")
        cur8.copy_to(write_file, "result", sep = ",", columns = ("id","first_name","last_name","gender","email","date_of_birth","country_of_birth","car_id","make","model","price"))
        cur8.close()

    # Exporting Direct Queries to csv file.
    write_file2 = "F:\\Study_Work\\Python\\Python WorkSpace\\17. PostgreSQL\\# Created Files\\toResults2.csv"
    cur9 = conn3.cursor()
    cur9.copy_expert(f"COPY result TO '{write_file2}' WITH CSV HEADER", open(write_file2,'w'))
    cur9.close()

    # but this method is way too complicated instead of that we can,
    write_file3 = "F:\\Study_Work\\Python\\Python WorkSpace\\17. PostgreSQL\\# Created Files\\toResults3.csv"
    cur10 = conn3.cursor()
    cur10.execute(f"COPY result TO '{write_file3}' DELIMITER ',' CSV HEADER")
    cur10.close()
conn3.close()