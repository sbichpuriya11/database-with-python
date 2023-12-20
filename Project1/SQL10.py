import mysql.connector as connection

con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)

my_cursor = con.cursor()

# my_cursor.execute('insert into users(name,email,age) values ("Jose Portila","portila11@jose.com",30)')

my_cursor.execute('DELETE from users where userID = 13 ')
# result = my_cursor.fetchall()
# for records in result:
#     print(records)

con.commit()