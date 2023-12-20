import mysql.connector as connection
con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)
print('Connection Successfull')

my_cursor = con.cursor()

query = 'INSERT INTO users(NAME,EMAIL,AGE) VALUES(%s,%s,%s)'
record1 = ('John', 'john@codemy.com', 40)

my_cursor.execute(query,record1)

#to save the data into  the database
con.commit()