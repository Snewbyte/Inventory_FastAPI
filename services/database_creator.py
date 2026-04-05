import sqlite3 as sql

conn = sql.connect('main.db')
cur = conn.cursor()
createTable = 'CREATE TABLE USER (ID INTEGER not null primary key, FIRST_NAME VARCHAR(30), LAST_NAME VARCHAR(30), AGE VARCHAR(30), COUNTRY VARCHAR(30))'
cur.execute(createTable)

cur.execute('INSERT INTO USER VALUES (0, "Ross", "Geller", "32", "USA")')
cur.execute('INSERT INTO USER VALUES (1, "Rachel", "Green", "30", "USA")')
cur.execute('INSERT INTO USER VALUES (2, "Phoebe", "Buffay", "31", "France")')
cur.execute('INSERT INTO USER VALUES (3, "Joe", "Tribbiani", "29", "Italy")')
cur.execute('INSERT INTO USER VALUES (4, "Chandler", "Bing", "32", "Ireland")')
cur.execute('INSERT INTO USER VALUES (5, "Monica", "Geller", "30", "USA")')


print(cur.execute('SELECT * from USER').fetchall())

conn.commit()
conn.close()