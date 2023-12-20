import mysql.connector as connection
con = connection.connect(username='root',password='',host='localhost')
if con:
    print('Connection Successful')

my_cursor = con.cursor()


# Write a query to display all customers with a grade above 100
# my_cursor.execute('select * from w3_resource.customer where grade>100')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a query statement to display all customers in New York who have a grade value above 100.
# my_cursor.execute('select * from w3_resource.customer where city="New York" and grade>100')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL statement to display all customers, who are either belongs to the city New York or had a grade above 100.
# my_cursor.execute('select * from w3_resource.customer where city="New York" or  grade>100')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL statement to display all the customers, who are either belongs to the city New York or not had a grade above 100.
# my_cursor.execute('select * from w3_resource.customer where city="New York" or not grade >100')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to display those customers who are neither belongs to the city New York nor grade value is more than 100.
# my_cursor.execute('select * from w3_resource.customer where not city="New York" and not grade >100')
# my_cursor.execute('select * from w3_resource.customer where not (city="New York" or grade >100)')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL statement to display either those orders which are not issued on date 2012-09-10 and issued by the salesman
# whose ID is 5005 and below or those orders which purchase amount is 1000.00 and below.
# my_cursor.execute('select * from w3_resource.orders where not ((ord_date="2012-09-10" and  salesman_ID>5005) or purch_amt>=    1000)')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL statement to display salesman_id, name, city and commission who gets the commission within the range more than 0.10% and less than 0.12%
# my_cursor.execute('select * from w3_resource.salesman where commission between 0.10 and 0.11')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL query to display all orders where purchase amount less than 200 or exclude those orders which order date is on or greater than 10th Feb,2012 and customer id is below 3009.
# my_cursor.execute('select * from w3_resource.orders where purch_amt<200 or not (ord_date>="10-Feb-2012" and customer_id<3009)')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# Write a SQL statement to exclude the rows which satisfy 1) order dates are 2012-08-17 and purchase amount is below 1000 2) customer id is greater than 3005 and purchase amount is below 1000.
# my_cursor.execute('select * from w3_resource.orders where not ((ord_date="2012-08-17" or  customer_id>3005) and purch_amt<1000)')
# result = my_cursor.fetchall()
# for row in result:
#     print(row)




# Write a SQL query to display order number, purchase amount, achieved, the unachieved percentage for those order which exceeds the 50% of the target value of 6000.
my_cursor.execute('select ord_no,purch_amt, (100*purch_amt/6000) as "Achieved", (100*(6000-purch_amt)/6000) as "Unachieved" from w3_resource.orders where (100*purch_amt/6000>50)')
result = my_cursor.fetchall()
for row in result:
    print(row)
