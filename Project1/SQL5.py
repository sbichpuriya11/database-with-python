import mysql.connector as connection

con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)

my_cursor = con.cursor()
my_cursor.execute('SELECT * FROM users order by userID asc')

# my_cursor.execute('SELECT name FROM users')
result = my_cursor.fetchall()
# result = my_cursor.fetchone()

for records in result:
    print(records[0] + "\t%s" % records[1] + "\t\t%s" % records[2] + "\t%s" % records[3])
