import mysql.connector as connection
con = connection.connect(
    host='localhost',
    username='root',
    password=''
)

if con:
    print('Connection Successful')

my_cursor = con.cursor()
# my_cursor.execute('drop database if exists products')
# my_cursor.execute('create database if not exists products')
# my_cursor.execute('create table if not exists products.item_mast( pro_id int primary key not null auto_increment,pro_name varchar(30),pro_price float,pro_com float)auto_increment=101')

# products = [('Mother Board',3200,15),
#             ('Key Board',450,16),
#             ('ZIP Drive',250,14),
#             ('Speaker',550,16),
#             ('Monitor',5000,11),
#             ('DVD Drive',900,12),
#             ('CD Drive',800,12),
#             ('Printer',2600,13),
#             ('Refill Cartridge',350,13),
#             ('Mouse',250,12)
#             ]
# query = 'insert into products.item_mast(pro_name,pro_price,pro_com) values(%s,%s,%s)'
# for column in products:
#     my_cursor.execute(query,column)
#

# Write a SQL query to find all the products with a price between Rs.200 and Rs.600.
# my_cursor.execute('select * from products.item_mast where pro_price between 200 and 600')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to calculate the average price of all products of the manufacturer which code is 16.
# my_cursor.execute('select avg(pro_price) from products.item_mast where pro_com=16 ')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to find the item name and price in Rs.
# my_cursor.execute('select pro_name,pro_price as "price(Rs)" from products.item_mast')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to display the name and price of all the items with a price is equal or more than Rs.250, and the list contain the larger price first and then by name in ascending order.
# my_cursor.execute('select pro_name,pro_price from products.item_mast where pro_price >=250 order by pro_price desc, pro_name')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to display the average price of the items for each company, showing only the company code.
# my_cursor.execute('select avg(pro_price), pro_com from products.item_mast group by pro_com')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to find the name and price of the cheapest item(s)
# my_cursor.execute('select pro_name, pro_price from products.item_mast where pro_price = (select min(pro_price) from products.item_mast)')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# my_cursor.execute('create table if not exists products.emp_details(emp_id int primary key not NULL,emp_fname varchar(20),emp_lname varchar(20),emp_dept int )')
# emp_data = [
#     (127323,'Michale','Robbin',57),
#     (526689 ,'Carlos','Snares',63),
#     (843795 ,'Enric','Dosio',57),
#     (328717 ,'John','Snares',63),
#     (444527 ,'Joseph','Donsi',47),
#     (659831 ,'Zanifer','Emily',47),
#     (847674 ,'Kuleswar','Sitaram',57),
#     (748681 ,'Henrey','Gabriel',47),
#     (555935 ,'Alex','Manuel',57),
#     (539569 ,'George','Mardy',27),
#     (733843 ,'Mario','Saule',63),
#     (631548 ,'Alan','Snappy',27),
#     (839139 ,'Maria','Foster',57),
# ]
#
# query = 'insert into products.emp_details(emp_id,emp_fname,emp_lname,emp_dept) values(%s,%s,%s,%s)'
# for row in emp_data:
#     my_cursor.execute(query,row)



# Write a query in SQL to find the last name of all employees, without duplicates.
# my_cursor.execute('select distinct(emp_lname) from products.emp_details')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)



# Write a query in SQL to find the data of employees whose last name is 'Snares'
my_cursor.execute('select * from products.emp_details where emp_lname="Snares"')
result = my_cursor.fetchall()
for row in result:
    print(row)



# Write a query in SQL to display all the data of employees that work in the department 57.
# my_cursor.execute('select * from products.emp_details where emp_dept = 57')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)




con.commit()