import mysql.connector as con1
con = con1.connect(host='localhost',
                   username='root',
                   password='',
                   database='testdb'
                   )

print('Connection Successfull')

my_cursor = con.cursor()

my_cursor.execute(" CREATE TABLE users(name varchar(100),email varchar(100),age integer(2), userID integer AUTO_INCREMENT PRIMARY KEY )")
my_cursor.execute('Show Tables')
for table in my_cursor:
    print(table[0])