import sqlite3 as sql

conn = sql.connect('main.db')
cur = conn.cursor()
createProductsTable = 'CREATE TABLE PRODUCTS (ID INTEGER not null primary key, NAME VARCHAR(30), PRICE FLOAT, TYPE VARCHAR(30))'
createTokensTable = 'CREATE TABLE TOKENS (ID INTEGER not null primary key, TOKEN VARCHAR(30))'
cur.execute('DROP TABLE IF EXISTS PRODUCTS')
cur.execute('DROP TABLE IF EXISTS TOKENS')
cur.execute(createProductsTable)
cur.execute(createTokensTable)

cur.execute('INSERT INTO PRODUCTS VALUES (0, "Apple", 4.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (1, "Orange", 8.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (2, "Tomato", 3.99, "Fruit")')
cur.execute('INSERT INTO PRODUCTS VALUES (3, "Cabbage", 1.99, "Vegetable")')
cur.execute('INSERT INTO PRODUCTS VALUES (4, "Potato", 2.50, "Vegetable")')
cur.execute('INSERT INTO PRODUCTS VALUES (5, "Carrots", 1.49, "Vegetable")')

cur.execute('INSERT INTO TOKENS VALUES (0, "abcdefg")')
cur.execute('INSERT INTO TOKENS VALUES (1, "hijklmn")')
cur.execute('INSERT INTO TOKENS VALUES (2, "1234567")')


print(cur.execute('SELECT * from PRODUCTS').fetchall())
print(cur.execute('SELECT * from TOKENS').fetchall())
conn.commit()
conn.close()