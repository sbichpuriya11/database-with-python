import mysql.connector as connection
country = input('Enter Country Name:- ')
country = country.upper()
con = connection.connect(host='127.0.0.1',username='root',password='',database='countries')
if(con):
    print('Connection Successful')

cursor = con.cursor()
#
cursor.execute('Select * from country where name="%s" '%country)
#
result = cursor.fetchall()

if(result):
    print(result[0])
else:
    print('Not Found')




