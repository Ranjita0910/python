import sqlite3
connection=sqlite3.connect('ranju.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF 
NOT EXISTS users(id INTEGER PRIMARY KEY, 
name TEXT,age INTEGER)''')
cursor.EXECUTE('''INSERT INTO users
(name,age)Values(?,?)''',
('ram'30))
connection.commit()
cursor.execute('''SELECT*FROM 
user''')
rows=cursor.fetchall()
for row in rows:
    print(row)
close the Connection
connection.close()

