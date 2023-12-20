import mysql.connector as connection

con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)

my_cursor = con.cursor()

my_cursor.execute('select * from users where age > 30')
result = my_cursor.fetchall()
for record in result:
    print(record[0])