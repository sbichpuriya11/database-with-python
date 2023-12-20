import mysql.connector as con
# connection = con.connect(host='127.0.0.1', user='root', password='')
connection = con.connect(host='localhost', user='root', password='')
print('Conncetion Successfull')

print('\n', connection)

my_cursor = connection.cursor()

# my_cursor.execute("CREATE DATABASE testDB")
my_cursor.execute('Show Databases')

for db in my_cursor:
    print(db[0])