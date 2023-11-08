# EX:1
# import time
# def countdown(n):
#     print("countdown started")
#     while n >= 0:
#         yield n
#         n -= 1
# values = countdown(10)
# for each in values:
#     print(each)
#     time.sleep(1)

# EX:2
# import time
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# g = fib()
# for x in g:
#     print(x)
#     time.sleep(1)


# EX:3
# def natural(n):
#     x = 1
#     while x <= n:
#         yield x
#         x += 1
# values = natural(101)
# for each in values:
#     print(each, end = " ")


# EX:4
# import time
# def infinity():
#     x = 0
#     while True:
#         yield x
#         x += 1
#
# i = infinity()
# for each in i:
#     print(each)
#     time.sleep(1)


import time

#
# class Test:
#     def __init__(self, name):
#         self.name = name
#
# class Stu(Test):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks
#
#     def m1(self):
#         print(f"Hello my name is {self.name} and my marks are {self.marks}")
#
# s = Stu("Gangadhar", 100)
# s.m1()

# file_name = input("Enter file name:")
# f = open(f"C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\{file_name}", "w")
# while True:
#     s = input("enter the data")
#     f.write(s+"\n")
#     choice = input("do you want extra line[yes/no]")
#     if choice.lower() == "no":
#         break


# import pyodbc
#
# # Define your connection parameters
# # server = 'localhost'  # Replace with your server name
# # database = 'master'  # Replace with your database name
# # username = 'LAPTOP-7357NLN3\Gangadhar sharma'  # Replace with your SQL Server username
# # password = 'Raghavendra@123'  # Replace with your SQL Server password
#
# # Create a connection string
# connection = pyodbc.connect('Driver={SQL Server};' 'server=LAPTOP-7357NLN3\MSSQLSERVER01;'
#                           'Database=dgdb''Trusted_connection=yes;')
#
# def read(connection):
#     cursor = connection.cursor()
#     print("Read")
#     cursor.execute('SELECT * FROM Table_1')
#     for row in cursor:
#         print(row)
#     connection.commit()
#
# def write(connection):
#     cursor = connection.cursor()
#     print("write")
#     Firstname = input("enter first name:")
#     Lastname = input("enter last name:")
#     cursor.execute("insert into Table_1(fname,lname) values(?,?),", (Firstname,Lastname))
#     read(connection)
#     connection.commit()
#
# write(connection)


import pyodbc
import csv

# Define your connection parameters
server = 'LAPTOP-7357NLN3\MSSQLSERVER01'  # Replace with your SQL Server server name or IP address
database = 'dgdb'  # Replace with the name of your database


query = "select * from table_1"
csv_file_name = "C:/Users/Gangadhar Sharma/OneDrive/Desktop/python/new4.csv"
try:
    connection = pyodbc.connect(
                 f"SERVER = {server},"
                 f"DATABASE = {database}")

    cursor = connection.cursor()
    cursor.execute(query)
    fieldnames = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.Dictwriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows({fieldnames[i]: row[i] for i in range(len(fieldnames))} for row in rows)

    print(f'Data has been written to {csv_file_name}')

except pyodbc.Error as err:
    print(f"Error: {err}")
