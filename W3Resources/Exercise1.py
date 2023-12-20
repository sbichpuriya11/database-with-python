# https://www.w3resource.com/sql-exercises/sql-retrieve-from-table.php

import mysql.connector as connection


con = connection.connect(
    host='127.0.0.1',
    user='root',
    password=''
)


if(con):
    print('Connection Successfull')

my_cursor = con.cursor()

#This is to prevent error if previors records exists in database
# my_cursor.execute('Drop database if exists w3_resource')



# first of all we have to create a database
# my_cursor.execute('Create database if not exists w3_resource')


#query to create a table w3_resource & to set the specific starting point for auto increment
# my_cursor.execute(
#     "Create table if not exists w3_resource.salesman(salesman_ID integer AUTO_INCREMENT PRIMARY KEY not null , name varchar(30),city varchar(30), commission float)auto_increment=5001")





# Inserting values to our database

# records = [('James Hoog','New York',0.15),
#            ('Nail Knite','Paris',0.13),
#            ('Pit Alex','London',0.11),
#            ('Mx Lyon','Paris',0.14),
#            ('Paul Adam','Rome',0.13),
#            ('Lauson Hen','San Jose',0.12)
#            ]
#
# query = 'insert into w3_resource.salesman(name,city,commission) values(%s,%s,%s)'
# for i in range(0,len(records)):
#     my_cursor.execute(query,records[i])
# con.commit()





# 1) Write a SQL statement to display all the information of all salesmen
# my_cursor.execute('select * from w3_resource.salesman')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# 2) Write a SQL statement to display specific columns like name and commission for all the salesman.
# my_cursor.execute('Select name,commission from w3_resource.salesman')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


#Query to create table orders
# my_cursor.execute("create table if not exists w3_resource.orders(ord_no int,primary key (ord_no), purch_amt float, ord_date date,customer_id int NOT NULL,salesman_ID int, FOREIGN KEY(salesman_ID) references salesman(salesman_ID))")
# records = [(70001,150.5,'2012-10-05',3005,5002),
#            (70009,270.65,'2012-09-10',3001,5005),
#            (70002,65.26,'2012-10-05',3002,5001),
#            (70004,110.5,'2012-08-17',3009,5003),
#            (70007,948.5,'2012-09-10',3005,5002),
#            (70005,2400.6,'2012-07-27',3007,5001),
#            (70008,5760,'2012-09-10',3002,5001),
#            (70010,1983.43,'2012-10-10',3004,5006),
#            (70003,2480.4,'2012-10-10',3009,5003),
#            (70012,250.45,'2012-06-27',3008,5002),
#            (70011,75.29,'2012-08-17',3003,5004),
#            (70013,3045.6,'2012-04-25',3002,5001)
#            ]
# query = 'INSERT INTO w3_resource.ORDERS(ord_no,purch_amt,ord_date,customer_id,salesman_id) values(%s,%s,%s,%s,%s)'
# for record in records:
#     my_cursor.execute(query,record)



# Write a query to display the columns in a specific order like order date, salesman id, order number and purchase amount from for all the orders.
# my_cursor.execute('Select * from w3_resource.orders')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)



# Write a query which will retrieve the value of salesman id of all salesmen, getting orders from the customers in orders table without any repeats.
# my_cursor.execute('Select distinct(ord_no),purch_amt,ord_date,customer_id,salesman_id from w3_resource.orders')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


# Write a SQL statement to display names and city of salesman, who belongs to the city of Paris
# my_cursor.execute('Select name,commission,city from w3_resource.salesman where city="Paris"')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)



# Query to create table customer
# my_cursor.execute('create table if not exists w3_resource.customer(customer_id int primary key not null, cust_name varchar(30), city varchar(20), grade int, salesman_ID  int, foreign key (salesman_ID) references salesman(salesman_ID)  )')


# records = [(3002,'Nick Rimando','New York',100,5001),
#            (3007,'Brad Davis','New York',200,5001),
#            (3005,'Graham Zusi','California',200,5002),
#            (3008,'Julian Green','London',300,5002),
#            (3004,'Fabian Johnson','Prais',300,5006),
#            (3009,'Geoff Cameron','Berlin',100,5003),
#            (3003,'Jozy Altidor','Moscow',200,5004),
#            (3001,'Brad Guzan','London',None,5005)
#            ]
#
# query = 'INSERT INTO w3_resource.customer(customer_id,cust_name,city,grade,salesman_ID ) values(%s,%s,%s,%s,%s)'
# for record in records:
#     my_cursor.execute(query,record)


# Write a SQL statement to display all the information for those customers with a grade of 200.
# my_cursor.execute('select * from w3_resource.customer where grade=200')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)


#  Write a SQL query to display the order number followed by order date and the purchase amount for each order which will be delivered by the salesman who is holding the ID 5001.
# my_cursor.execute('select * from w3_resource.orders where salesman_ID = 5001')
# result = my_cursor.fetchall()
# for record in result:
#     print(record)
#

con.commit()

