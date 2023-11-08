# # Notes written in pink binding book shri:side
# # EX:1 CREATING A CONNECTION
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          auth_plugin="mysql_native_password",2

# # )
# # cur = mydb.cursor(buffered=True)
# # print(mydb)
# # ---------------------------------------------------------------------------------------------------------------------
#
# EX:2 CREATING A CONNECTION WITH DATABASE INORDER TO CONNECT TO A SPECIFIC DATABASE WHICH IS ALREADY EXISTING

# import mysql.connector
# try:
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Raghavendra@123",
#     auth_plugin="mysql_native_password",
#     database="book_shop"
#     )
#     print(mydb)
#     print(mydb.is_connected())
# except:
#     print("database does not exists")

# #----------------------------------------------------------------------------------------------------------------------
#
# # EX:3 CREATING THE CURSOR OBJECT
# import mysql.connector

# Create the connection object
# myconn = mysql.connector.connect(
# host="localhost",
# user="root",
# passwd="Raghavendra@123",
# database="book_shop",
# auth_plugin="mysql_native_password")

# printing the connection object
# print(myconn)

# creating the cursor object
# cur = myconn.cursor()

# # ----------------------------------------------------------------------------------------------------------------------
#
# # EX:4  Getting the list of existing databases
#
#
# import mysql.connector
# mydb = mysql.connector.connect(
#          host="localhost",
#          user="root",
#          passwd="Raghavendra@123",
#          auth_plugin="mysql_native_password"
# )
# cur = mydb.cursor()
# print(list(cur))
# try:
#     query = "show databases"
#     dbs = cur.execute(query)
#     print(list(cur))
#
# except:
#     mydb.rollback()
# for x in cur:
#     print(x[0])
#
# print(list(cur))
# mydb.close()


# # ---------------------------------------------------------------------------------------------------------------------
# EX:5 Creating the new database
# import mysql.connector
# # Create the connection object
# mydb = mysql.connector.connect(
#          host="localhost",
#          user="root",
#          passwd="Raghavendra@123",
#          auth_plugin="mysql_native_password")
# # creating the cursor object
# cur = mydb.cursor()
# try:
#     # creating a new database
#     new_data_base = cur.execute("create database pythonDB")
#     # getting the list of all the databases which will now include the new database PythonDB
#     dbs = cur.execute("show databases")
#
# except mysql.connector.errors.DatabaseError as db:
#     print(db)
#
# for x in cur:
#     print(x)
# mydb.close()

# # ---------------------------------------------------------------------------------------------------------------------
# # EX:6 CREATING A TABLE IN THE DATABASE
# import mysql.connector
# #
# # # Create the connection object
# myconn = mysql.connector.connect(
#          host="localhost",
#          user="root",
#          passwd="Raghavendra@123",
#          auth_plugin="mysql_native_password",
#          database="pythonDB"
# )
# # # creating the cursor object
# cur = myconn.cursor()
# #
# try:
# #   Creating a table with name Employee having four columns i.e., name, id, salary, and department id
#     query = '''create table if not exists Employee2(
#                name varchar(20) not null,
#                id int(20) not null primary key,
#                salary float not null,
#                Dept_id int not null)'''
#     dbs = cur.execute(query)
#     cur.execute("desc employee2")
# except Exception as e:
#     print("can not connect")
#
# for each in cur:
#     print(list(each))
#
# myconn.close()


# # ---------------------------------------------------------------------------------------------------------------------
#
# # EX:7 Alter Table

# import mysql.connector
# con = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         passwd="Raghavendra@123",
#         database="pythonDB",
#         auth_plugin="mysql_native_password")
# cur = con.cursor()
# try:
#     cur.execute("alter table employee add branch_name varchar(20) not null")
#     print("one row added successfully to the table")
#     cur.execute("desc employee")
# except mysql.connector.errors.DatabaseError as db:
#       print(db)
# for each in cur:
#     print(list(each))
# con.close()
#
# # ----------------------------------------------------------------------------------------------------------------------
# # EX:8
# # Insert Operation
# # Adding a record to the table
# import mysql.connector
# # Create the connection object
# myconn = mysql.connector.connect(
#            host="localhost",
#            user="root",
#            passwd="Raghavendra@123",
#            database="PythonDB",
#            auth_plugin="mysql_native_password")
# # creating the cursor object
# cur = myconn.cursor()
# sql = "insert into employee1(name, id, salary, dept_id) values ('dgs', 1002, 5.5, 112233)"
#
# try:
#     # inserting the values into the table
#     cur.execute(sql)
#
#     # commit the transaction.commit is used to save the inserted row in the table.if the table is not commited then no changes are made to table
#     myconn.commit()
#
# except mysql.connector.errors.DatabaseError as db:
#        myconn.rollback()
#        print("changes are rollbacked")
# print(cur.rowcount, "record inserted!")
# myconn.close()

# # ----------------------------------------------------------------------------------------------------------------------
#
# # EX:9  TO INSERT MULTIPLE VALUES:
# import mysql.connector, sys
# def  insertRecord():
#     c = 0
#     while True:
#         con = mysql.connector.connect(
#               host="localhost",
#               user="root",
#               passwd="Raghavendra@123",
#               database="pythonDB",
#               auth_plugin="mysql_native_password")
#         cur = con.cursor()
#         print("-"*50)
#         name = input("Enter Employee Name:")
#         id = int(input("Enter Employee Number:"))
#         salary = float(input("Enter Employee Salary:"))
#         Dept_id = int(input("Enter the Departement id:"))
#         branch_name = input("Enter branch name:")
#         cur.execute(f"insert into employee (name, id, salary, Dept_id, branch_name)values('%s',%d,%f, %d, '%s')"
#                     % (name, id, salary, Dept_id, branch_name))
#         con.commit()
#         print("-"*50)
#         print("{} Record Inserted Successfully in Employee Table!".format(cur.rowcount))
#         print("-"*50)
#         c += 1
#         ch = input("Do u want to insert another record(yes/no):")
#         print()
#         if(ch.lower()=="no"):
#             print(f"Total number of records added to the table: {c}")
#             print("Thx for using this program")
#             sys.exit()
#         print("-"*50)
#
# #main program
# insertRecord()

#----------------------------------------------------------------------------------------------------------------------
# # READ OPERATION
# # EX:10  TO GET THE WHOLE DATA FROM THE TABLE(cursor.fetchall())
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select * from employee")
# #     result = cur.fetchall()
# #     for x in result:
# #         print(x)
# # except mysql.connector.errors.DatabaseError as db:
# #        print(db)
# #
# # mydb.close()
#
# # output:
# # ('gfd', 66, 67.0, 665, 'mkg')
# # ('dgs', 100, 5.5, 112233, 'MBA')
# # ('dgss', 1001, 5.5, 112233, 'MBA')
# # ('dgs', 1002, 5.5, 112233, 'MBA')
# # ('john', 33211, 5.5, 665544, 'mba')
# # ('abhiram', 105444, 4.4, 445566, 'mba')
# # ('rrr', 667788, 666.0, 555, 'hgt')
# # ('sitha', 5566884, 6.7, 887766, 'mba')
# # ---------------------------------------------------------------------------------------------------------------------
#
# #  EX:11 READING ONLY SPECIFIC COLUMNS
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select name,id,salary from employee")
# #     result = cur.fetchall()
# #     for each in result:
# #         print(each)
# # except mysql.connector.errors.DatabaseError as db:
# #         print(db)
# #
# # mydb.close()
# #
# # output:
# # ('gfd', 66, 67.0)
# # ('dgs', 100, 5.5)
# # ('dgss', 1001, 5.5)
# # ('dgs', 1002, 5.5)
# # ('john', 33211, 5.5)
# # ('abhiram', 105444, 4.4)
# # ('rrr', 667788, 666.0)
# # ('sitha', 5566884, 6.7)
# # ---------------------------------------------------------------------------------------------------------------------
# # EX:12 TO RETRIEVE ONLY ONE RECORD(cursor.fetchone())
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select * from employee")
# #     result = cur.fetchone()
# #     print(result)
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
# #
# # output
# #
# # ('gfd', 66, 67.0, 665, 'mkg')
# # ---------------------------------------------------------------------------------------------------------------------
# # EX:13 TO RETRIEVE ONLY GIVEN NUMBER OF RECORDS(cursor.fetchmany(n))
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select * from employee")
# #     result = cur.fetchmany(3)
# #     for x in result:
# #         print(x)
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
#
# # output
# # ('gfd', 66, 67.0, 665, 'mkg')
# # ('dgs', 100, 5.5, 112233, 'MBA')
# # ('dgss', 1001, 5.5, 112233, 'MBA')
# # ----------------------------------------------------------------------------------------------------------------------
#
# # EX:14 Formatting the result:
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select name, id, salary from Employee")
# #     result = cur.fetchall()
# #     print("Name\tid\tsalary")
# #     for row in result:
# #         print("%s\t%d\t%d" %(row[0],row[1], row[2]))
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# #
# # mydb.close()
# # --------------------------------------------------------------------------------------------------------------------
#
# # EX:15 printing the names which has d
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select name, id, salary from Employee where Name like '%d%'")
# #     result = cur.fetchall()
# #     print("Name     id     salary")
# #     for row in result:
# #         print("%s    %d    %d" %(row[0], row[1], row[2]))
# #
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
# # ----------------------------------------------------------------------------------------------------------------------
# # EX:16 printing the names with id = 10O, 1001, and 1002
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select name, id, salary from Employee where id in(100, 1001,1002)")
# #     result = cur.fetchall()
# #     print("Name     id     salary")
# #     for row in result:
# #         print("%s    %d    %d" %(row[0], row[1], row[2]))
# #
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
# # ---------------------------------------------------------------------------------------------------------------------
#
# # #EX:17 Ordering the result by name in ascending order
# #
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select * from employee order by name")
# #     result = cur.fetchall()
# #     print("Name     id     salary    Dept_id    branch_name")
# #     for row in result:
# #         print("%s    %d    %d    %d    %s" %(row[0], row[1], row[2],row[3],row[4]))
# #
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
#
# # ---------------------------------------------------------------------------------------------------------------------
#
# #EX:17 Ordering the result by id  in descending order
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("select * from employee order by id desc")
# #     result = cur.fetchall()
# #     print("Name     id     salary    Dept_id    branch_name")
# #     for row in result:
# #         print("%s    %d    %d    %d    %s" %(row[0], row[1], row[2],row[3],row[4]))
# #
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
# # ---------------------------------------------------------------------------------------------------------------------
# # # EX:18 Update Operation
# #
# import mysql.connector
# mydb = mysql.connector.connect(
#          host="localhost",
#          user="root",
#          passwd="Raghavendra@123",
#          database="pythonDB",
#          auth_plugin="mysql_native_password")
# cur = mydb.cursor()
# try:
#     cur.execute("UPDATE employee SET name = 'DGS' WHERE name = 'gangadhar'")
#     mydb.commit()
#     cur.execute("select * from employee")
#     result = cur.fetchall()
#     for x in result:
#         print(x)
# except mysql.connector.errors.DatabaseError as db:
#     print(db)
# mydb.close()
# # ----------------------------------------------------------------------------------------------------------------------
#
# # EX:19 DELETE Operation.Deleting the names who have letter d
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #          host="localhost",
# #          user="root",
# #          passwd="Raghavendra@123",
# #          database="pythonDB",
# #          auth_plugin="mysql_native_password")
# # cur = mydb.cursor()
# # try:
# #     cur.execute("DELETE FROM employee WHERE name like '%d%' ")
# #     mydb.commit()
# #     cur.execute("select * from employee") [to check whether values are deleted or not]
# #     result = cur.fetchall()
# #     for x in result:
# #         print(x)
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # mydb.close()
# # ----------------------------------------------------------------------------------------------------------------------
# # JOIN OPERATION
# # EX:20 FULL JOIN
# # import mysql.connector
# # myconn = mysql.connector.connect(host="localhost", user="root", passwd="Raghavendra@123", database="PythonDB",auth_plugin="mysql_native_password")
# # cur = myconn.cursor()
# # try:
# #     cur.execute('''select e.name, e.id,
# #                 e.salary,d.Dept_id,d.Dept_name
# #                 from departements as d join employee as e on e.Dept_id = d.Dept_id''')
# #
# #     print("Name    Id    Salary    Dept_id    Dept_name")
# #     for row in cur:
# #         print("%s    %d    %f    %d    %s" %(row[0], row[1], row[2], row[3], row[4]))
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # myconn.close()
# # ----------------------------------------------------------------------------------------------------------------------
#
# # RIGHT JOIN(Doubt)
# # EX:21
# # import mysql.connector
# # myconn = mysql.connector.connect(host="localhost", user="root", passwd="Raghavendra@123", database="PythonDB",auth_plugin="mysql_native_password")
# # cur = myconn.cursor()
# # try:
# #     cur.execute('''select e.name, e.id,
# #                 e.salary,d.Dept_id,d.Dept_name
# #                 from departements as d RIGHT join  employee as e  on d.Dept_id = e.Dept_id''')
# #
# #     print("Name    Id    Salary    Dept_id    Dept_name")
# #     for row in cur:
# #         print("%s    %d    %0.2f   %d    %s" %(row[0], row[1], row[2], row[3], row[4]))
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # myconn.close()
# # ---------------------------------------------------------------------------------------------------------------------
# # LEFT JOIN(Doubt)
# # EX:22
#
# # import mysql.connector
# # myconn = mysql.connector.connect(host="localhost", user="root", passwd="Raghavendra@123", database="PythonDB",auth_plugin="mysql_native_password")
# # cur = myconn.cursor()
# # try:
# #     cur.execute('''select e.name, e.id,
# #                 e.salary,d.Dept_id,d.Dept_name
# #                 from employee as e LEFT join departements as d on d.Dept_id = e.Dept_id''')
# #
# #     print("Name    Id    Salary    Dept_id    Dept_name")
# #     for row in cur:
# #         print("%s    %d    %0.2f   %d    %s" %(row[0], row[1], row[2], row[3], row[4]))
# #
# # except mysql.connector.errors.DatabaseError as db:
# #     print(db)
# # myconn.close()
# # # ----------------------------------------------------------------------------------------------------------------------
# #
# # # wap which will implement the following by using classes and objects
# # # Student Information System
# # #
# # # 1.add student
# # # 2.delete student
# # # 3.update student
# # # 4.view student
# # # 5. view all students
# # # 6.exit
# #
# #
# #
# # import mysql.connector, sys
# # class Student_info:
# #     table_name = "student_info"
# #     def add_student(self):
# #         con = mysql.connector.connect(host="localhost",
# #                                       user="root",
# #                                       passwd="Raghavendra@123",
# #                                       database="pythondb",
# #                                       auth_plugin="mysql_native_password")
# #         cur = con.cursor()
# #         try:
# #             sno = int(input("enter student number:"))
# #             sname = input("enter student name:")
# #             smarks = int(input("enter student marks:"))
# #             saddress = input("enter student address:")
# #             cur.execute("insert into student_info values('%s', '%s', '%s', '%s')"%(sno, sname, smarks, saddress))
# #             con.commit()
# #         except mysql.connector.errors.DatabaseError as db:
# #             print(db)
# #         print(cur.rowcount, "record inserted successfully to student_info table")
# #         con.close()
# #
# #     def delete_student(self):
# #         con = mysql.connector.connect(host="localhost",
# #                                       user="root",
# #                                       passwd="Raghavendra@123",
# #                                       database="pythondb",
# #                                       auth_plugin="mysql_native_password")
# #         cur = con.cursor()
# #         try:
# #             sno = int(input("enter student number to delete from the table:"))
# #             cur.execute("delete from {} where sno = {}".format(Student_info.table_name, sno))
# #             con.commit()
# #         except mysql.connector.errors.DatabaseError as db:
# #             print(db)
# #         print(cur.rowcount, "record deleted successfully from student_info table")
# #         con.close()
# #
# #
# #     def update_student(self):
# #         con = mysql.connector.connect(host="localhost",
# #                                       user="root",
# #                                       passwd="Raghavendra@123",
# #                                       database="pythondb",
# #                                       auth_plugin="mysql_native_password")
# #         cur = con.cursor()
# #         up = input("Enter which record you want to update from table:")
# #         up1 = input("Enter the old value / name:")
# #         up2 = input("Enter the updated value / name:")
# #         try:
# #             cur.execute("Update {} SET {} = '{}' where {} = '{}'".format(Student_info.table_name, up, up2, up, up1))
# #             con.commit()
# #         except mysql.connector.errors.DatabaseError as db:
# #             print(db)
# #         print("{} is successfully updated".format(up))
# #         con.close()
# #
# #     def view_student(self):
# #         con = mysql.connector.connect(host="localhost",
# #                                       user="root",
# #                                       passwd="Raghavendra@123",
# #                                       database="pythondb",
# #                                       auth_plugin="mysql_native_password")
# #         cur = con.cursor()
# #         vw = input("Enter any column name from the table to view the details:")
# #         vw1 = input("Enter the value/ name:")
# #         try:
# #             cur.execute("select * from {} where {} = '{}'".format(Student_info.table_name, vw, vw1))
# #             result = cur.fetchmany(1)
# #             print("SNO    SNAME   SMARKS    SADDREE")
# #             for row in result:
# #                 print(row[0], "    ", row[1], "    ", row[2], "    ", row[3])
# #         except mysql.connector.errors.DatabaseError as db:
# #             print(db)
# #         con.close()
# #
# #
# #     def view_all(self):
# #         con = mysql.connector.connect(host="localhost",
# #                                       user="root",
# #                                       passwd="Raghavendra@123",
# #                                       database="pythondb",
# #                                       auth_plugin="mysql_native_password")
# #         cur = con.cursor()
# #         try:
# #             cur.execute("select * from {}".format(Student_info.table_name))
# #             result = cur.fetchall()
# #             print("SNO    SNAME   SMARKS    SADDREE")
# #             for row in result:
# #                 print(row[0], "    ", row[1], "    ", row[2], "    ", row[3])
# #         except mysql.connector.errors.DatabaseError as db:
# #             print(db)
# #         con.close()
# # s = Student_info()
# # while True:
# #     print('''
# #     1.add student
# #     2.delete student
# #     3.update student
# #     4.view student
# #     5. view all students
# #     6.exit''')
# #     choice = int(input("please select your choice:"))
# #     if choice == 6:
# #         print("Thank you")
# #         sys.exit()
# #     if choice == 1:
# #         s.add_student()
# #     if choice == 2:
# #         s.delete_student()
# #     if choice == 3:
# #         s.update_student()
# #     if choice == 4:
# #         s.view_student()
# #     if choice == 5:
# #         s.view_all()
# #-----------------------------------------------------------------------------------------------------------------------
#
#
# import mysql.connector
# mydb = mysql.connector.connect(
#          host="localhost",
#          user="root",
#          passwd="Raghavendra@123",
#          auth_plugin="mysql_native_password",
#          database="book_shop_copy"
#
# )
# cur = mydb.cursor()
# try:
#     query = 'select * from emp'
#     exe = cur.execute(query)
#
# except:
#     print("connection not found")
# for each in cur:
#     print(each)
# cur.close()
# mydb.close()
# ----------------------------------------------------------------------------------------


import mysql.connector,csv, sys
mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="Raghavendra@123",
         database="pythonDB",
         auth_plugin="mysql_native_password")
cur = mydb.cursor()
file_loc = "C:/Users/Gangadhar Sharma/OneDrive/Desktop/linux/myfile.csv"
try:
    syntax = "select * from employee"
    cur.execute(syntax)
    res = cur.fetchall()
    col = [each[0] for each in cur.description]
    with open(file_loc, "w") as fp:
        dict_writer =

