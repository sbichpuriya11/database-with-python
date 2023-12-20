import mysql.connector as connection

con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)

my_cursor = con.cursor()


my_cursor.execute("UPDATE users set age = 35 where userID=5")

#to commit change in database
con.commit()