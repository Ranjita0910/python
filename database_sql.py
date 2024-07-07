# import sqlite3
# connection=sqlite3.connect('data.db')
# cursor=connection.cursor()

# cursor.execute('''CREATE TABLE if not exists
# marks(id integer,name text,mark integer)''')

# cursor.execute('''insert into marks
# (id,name,marks)values(1,'ram',50)
# ''')

# cursor.execute('''insert into marks
#                (id,name,marks)
#                values(2,'sita',67)
# ''')
# cursor.execute(''' delete from marks
#                 where id=?''',(1,))
# connection.commit()
# cursor.execute ('''select*from 
# marks''')

# r=cursor.fetchall()
# for j in r:
#     print(j)




