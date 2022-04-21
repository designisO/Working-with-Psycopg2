
hostname = 'localhost'
dbname = 'obioscorp'
username = 'postgres'
pwd = ''
port_id = 5432

import psycopg2
import psycopg2.extras


connection = psycopg2.connect(dbname = dbname, user = username, password = pwd, host=hostname)


cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

# create statements

# cursor.execute('CREATE TABLE test (id SERIAL PRIMARY KEY, name VARCHAR);')

# cursor.execute('INSERT INTO test (name) VALUES (%s)', ("John",))

# cursor.execute('SELECT * FROM test;')

cursor.execute('SELECT * FROM test WHERE id = %s;', (1,))

print(cursor.fetchone()['name']) # try id to see what happens.


# print(cursor.fetchall())


# using the with cursor 
with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    cur.execute("SELECT * FROM test WHERE id = %s;", (1,))

    print(cur.fetchone()['name'])

connection.commit()


cursor.close()
connection.close()
