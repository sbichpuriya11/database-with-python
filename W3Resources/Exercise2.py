import mysql.connector as connection
con = connection.connect(
    host='localhost',
    username='root',
    password='',
)

if con:
    print('Connection Successful')
my_cursor = con.cursor()
my_cursor.execute('Create database if not exists NobelPrize')
my_cursor.execute('create table if not exists NobelPrize.nobel_win(year year,subject varchar(50),winner varchar(50),country varchar(50),category varchar(50))')
# records = [(1970,'Physics','Hannes Alfven','Sweden','Scientist'),
# (1970,'Physics','Louis Neel','France','Scientist'),
# (1970,'Chemistry','Luis Federico Leloir','France','Scientist'),
# (1970,'Physiology','Ulf von Euler','Sweden','Scientist'),
# (1970,'Physiology','Bernard Katz','Germany','Scientist'),
# (1970,'Literature','Aleksandr Solzhenitsyn','Russia','Linguist'),
# (1970,'Economics','Paul Samuelson','USA','Economist'),
# (1970,'Physiology','Julius Axelrod','USA','Scientist'),
# (1971,'Physics','Dennis Gabor','Hungary','Scientist'),
# (1971,'Chemistry','Gerhard Herzberg','Germany','Scientist'),
# (1971,'Peace','Willy Brandt','Germany','Chancellor'),
# (1971,'Literature','Pablo Neruda','Chile','Linguist'),
# (1971,'Economics','Simon Kuznets','Russia','Economist'),
# (1978,'Peace','Anwar al-Sadat','Egypt','President'),
# (1978,'Peace','Menachem Begin','Israel','Prime Minister'),
# (1987,'Chemistry','Donald J. Cram','USA','Scientist'),
# (1987,'Chemistry','Jean-Marie Lehn','France','Scientist'),
# (1987,'Physiology','Susumu Tonegawa','Japan','Scientist'),
# (1994,'Economics','Reinhard Selten','Germany','Economist'),
# (1994,'Peace','Yitzhak Rabin','Israel','Prime Minister'),
# (1987,'Physics','Johannes Georg Bednorz','Germany','Scientist'),
# (1987,'Literature','Joseph Brodsky','Russia','Linguist'),
# (1987,'Economics','Robert Solow','USA','Economist'),
# (1994,'Literature','Kenzaburo Oe','Japan','Linguist')
#            ]
# query = 'INSERT INTO NOBELPRIZE.nobel_win(year,subject,winner,country,category) values(%s,%s,%s,%s,%s)'
# for record in records:
#     my_cursor.execute(query,record)


# Write a SQL query to display the Nobel prizes for 1970
# my_cursor.execute('select * from nobelPrize.nobel_win where year =1970')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to know the winner of the 1971 prize for Literature.
# my_cursor.execute('select * from nobelPrize.nobel_win where year =1971 and subject="Literature"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to display the year and subject that won 'Dennis Gabor' his prize.
# my_cursor.execute('select year,subject from nobelprize.nobel_win where winner="Dennis Gabor"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to give the name of the 'Physics' winners since the year 1950.
# my_cursor.execute('select winner from nobelprize.nobel_win where year>1950 and subject = "Physics"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to Show all the details (year, subject, winner, country ) of the Chemistry prize winners between the year 1965 to 1975 inclusive.
# my_cursor.execute('select * from nobelprize.nobel_win where (year between 1965 and 1975) and subject="Chemistry"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to show all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin.
# my_cursor.execute('select * from nobelprize.nobel_win where year>1971 and winner in ("Menachem Begin","Yitzhak Rabin")')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to show all the details of the winners with first name Louis.
# my_cursor.execute('select * from nobelprize.nobel_win where winner like "Louis%"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to show all the winners in Physics for 1970 together with the winner of Economics for 1971.
# my_cursor.execute('select * from nobelprize.nobel_win where subject="Physics" and year=1970 union (select * from nobelprize.nobel_win where subject="Economics" and year=1971)')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to show all the winners of nobel prize in the year 1970 except the subject Physiology and Economics.
# my_cursor.execute('select * from nobelprize.nobel_win where year=1970 and subject not in ("Physiology","Economics")')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to show the winners of a 'Physiology' prize in an early year before 1971 together with winners of a 'Peace' prize in a later year on and after the 1974.
# my_cursor.execute('select * from nobelprize.nobel_win where year<1971 and subject= "Physiology" union (select * from nobelprize.nobel_win where subject="Peace" and year>=1974)')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to find all details of the prize won by Johannes Georg Bednorz.
# my_cursor.execute('select * from nobelprize.nobel_win where winner="Johannes Georg Bednorz"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to find all the details of the nobel winners for the subject not started with the letter 'P' and arranged the list as the most recent comes first, then by name in order.
# my_cursor.execute('select * from nobelprize.nobel_win where subject not like "P%" order by year desc, winner')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL query to find all the details of 1970 winners by the ordered to subject and winner name; but the list contain the subject Economics and Chemistry at last.
my_cursor.execute('select * from nobelprize.nobel_win where subject not like "P%" order by year desc, winner')
result = my_cursor.fetchall()
for record in result:
    print(record)


con.commit()