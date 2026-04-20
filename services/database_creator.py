import sqlite3 as sql

conn = sql.connect('main.db')
cur = conn.cursor()
createTable = 'CREATE TABLE PRODUCTS (ID INTEGER not null primary key, NAME VARCHAR(30), PRICE FLOAT, TYPE VARCHAR(30))'
cur.execute('DROP TABLE IF EXISTS PRODUCTS')
cur.execute(createTable)

cur.execute('INSERT INTO PRODUCTS VALUES (0, "Apple", 4.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (1, "Orange", 8.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (2, "Tomato", 3.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (3, "Cabbage", 1.99, "Vegetable")')
cur.execute('INSERT INTO PRODUCTS VALUES (4, "Potato", 2.50, "Vegetable")')
cur.execute('INSERT INTO PRODUCTS VALUES (5, "Carrots", 1.49, "Vegetable")')


print(cur.execute('SELECT * from PRODUCTS').fetchall())

conn.commit()
conn.close()