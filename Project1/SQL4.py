import mysql.connector as connection
con = connection.connect(
    host='localhost',
    username='root',
    password='',
    database='testdb'
)
print('Connection Successfull')

my_cursor = con.cursor()


# Adding Multiple records
query = 'INSERT INTO users(NAME,EMAIL,AGE) VALUES(%s,%s,%s)'
records = [
    ('Tim','tim@tim.com',32),
    ('Mary','mary@mary.com',21),
    ('Tina','tina@somethingelse.com',19),
    ('Steve','steve@steveDomain.com',41)
]

my_cursor.executemany(query,records)
# for i in range(0,len(records)):
#     my_cursor.execute(query,records[i])


#to save the data into  the database
con.commit()