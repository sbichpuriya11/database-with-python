import mysql.connector as connection

con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)

my_cursor = con.cursor()

# my_cursor.execute("select * from users where name like 'John' ")

my_cursor.execute("select * from users where name like '%a%' ")
result = my_cursor.fetchall()
for records in result:
    print(records[0],records[1],records[2])
