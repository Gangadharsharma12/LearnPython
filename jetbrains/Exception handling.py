# EX:1
# print("hello")
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print(20 / 5)
# print("hi")


# EX:2   CONTROL FLOW IN TRY EXCEPT.once we get error in try block pvm will go to except block but it wont comeback to
# try block again
# try:
#     print("Hello")
#     print(10 / 0)
#     print("dgs")
# except ZeroDivisionError:
#     print(100 / 50)
# print("hai")
#

# EX:3  How to print Exception Information
# try:
#     print(10 / 0)
# except ZeroDivisionError as i:
#     print(i)

# EX:4
# try:
#     print(10 / 0)
# except ZeroDivisionError as i:
#     print("Exception raised:", i.__class__.__name__)
#     print("Exception raised:", type(i).__name__)
#     print("Description of exception:", i)


# try:
#     print(float("hello"))
# except BaseException as i:
#
#     print("Exception raised:", i.__class__.__name__)
#     print("Exception raised:", type(i).__name__)
#     print("Description of exception:", i)


# EX:5 try with multiple except blocks
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
#
# except ZeroDivisionError:
#     print("Zero division error raised")
#
# except ValueError:
#     print("Value error raised")
#
# except BaseException as e:
#     print("Base exception raised", e)

#-----------------------------------------------------------------------------------------------------------------------

# eg:6 single except block that can handle multiple exceptions when the handling code is same
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
# except (BaseException, ZeroDivisionError, ValueError) as e:
#     print("EXCEPTION RAISED:", e)



# eg:7 default except block

# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
# except:
#     print("exeception raised", e.__class__.__name__)




# 121 -------------------------------------------------------------------------------------------------------------------
# eg:1 FINALLY BLOCK(N0 EXCEPTION)

# try:
#     print("TRY")
# except:
#     print("EXCEPT")
# finally  :
#     print("FINALLY")





# EX:2 EXCEPTION RAISED BUT NOT HANDLED
# try:
#     x = int(input())
#     y = int(input())
#     print(x / y)
#
# except ValueError:
#     print("Value error")
#
# finally:
#     print("close db connection")


# EX:3 EXCEPTION RAISED BUT HANDLED
# try:
#     x = input()
#     y = int(input())
#     print(x / y)
#
# except ValueError:
#     print("value error")
#
# finally:
#     print("finally")


# EX:4 RETURN VS FINALLY
# def f1():
#     try:
#         print ("hello")
#         print (h)
#         return "hai"
#     except:
#         print("Value error")
#         return  "trs"
#
#     finally:
#         print("finally")
#         return  "dgs"
# print(f1())


# EX:5
# def f1():
#     try:
#         return 666
#     except:
#         return 777
#     finally:
#         return 888
#
# print(f1())



# EX:6 HOW TO AVOID EXECUTING FINALLY BLOCK
# import os
# def m1():
#     try:
#         print("Hello")
#         os._exit(0)
#     except:
#         print("except")
#
#     finally:
#         print("finally")
#
# m1()

# EX:7
#  -----------------------------------------------------------------------------------------------------------------------
# 122
# try:
#     print("outer try block")
#     try:
#         print("Inner try block")
#         print(10 / 0)
#     except ZeroDivisionError:
#         print("zero division error")
#     finally:
#         print("inner finally block")
# except ValueError:
#     print("zero division error")
# finally:
#     print("Outer finally block")



# try:
#     print("outer try block statement 1")
#     print("outer try block statement 2")
#     print("outer try block statement 3")
#     try:
#         print("inner try block statement 4")
#         print(10 / "three")
#         print("outer try block statement 6")
#     except TypeError:
#         print(10 / 2)
#     finally:
#         print("Inner block statement 8")
#     print(10 / "four")
# except TypeError:
#     print(10 / 2)
# finally:
#     print(10 / 2)
# print(20 / 0)
# #----------------------------------------------------------------------------------------------------------------------
# 123 ELSE BLOCK WITH TRY EXCEPT FINALLY

# EX:1 IF TRY HAS NO EXCEPTION THEN ELSE WILL BE EXEXUTED
# try:
#     print("try")
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")
#

# EX:2 IF TRY HAS EXCEPTION THEN ELSE WILL NOT EXECUTE

# try:
#     print("try")
#     print(10 / 0)
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")
# ----------------------------------------------------------------------------------------------------------------------
# PRE DEFINED EXCEPTIONS:
# Syntax:
#  class classname(predefined exception class name):
#  def __init__(self,arg):
#  self.msg=arg

# EX:
# class TooYoungException(Exception):
#     def __init__(self, arg):
#         self.msg = arg
# TooYoungException is our class name which is the child class of Exception
# We can raise exception by using raise keyword as follows
# raise TooYoungException("message")


# class TooYoungException(Exception):
#     def __init__(self, arg):
#         self.msg = arg
#
#
# class TooOldException(Exception):
#     def __init__(self, arg):
#         self.msg = arg
#
#
# age = int(input("Enter Age:"))
# if age > 60:
#     raise TooYoungException("Plz wait some more time you will get best match soon!!!")
# elif age < 18:
#     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
# else:
#     print("You will get match details soon by email!!!")
# ---------------------------------------------------------------------------------------------------------------------
#    FILE HANDLING:


# f = open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abc.txt", "w")
# l= {"sunny \n": 100, "bunny \n": 101}
# f.writelines(l)
# f.close()
# print(f.closed)
# print(type(f))


# create an empty file and add data to the program
# fname = input("enter a file name:")
# f = open("C:\\Users\\Gangadhar Sharma\\"+fname, "w")
# while True:
#     data = input("enter the data to write:")
#     f.write(data + "\n")
#     option = input("do you want to add some data:[Y/N]")
#     if option.lower() == "no":
#         break
#     elif option.lower() == "yes":
#         continue
#     else:
#         print("please enter valid option")
# print("Your provided data added to file successfully")
# f.close()
# print(f.closed)


# EXAMPLE TO SHOW HOW TO ADD STUDENT DATA WITH SEPERATE FILE NAMES AT A TIME AND WITHOUT OVER RIDING
# while True:
#     name = input("Enter student name:")
#     f = open(f"C:\\New folder\\{name.lower()}.txt", "w")
#     m1 = input("Enter python marks:")
#     m2 = input("Enter Java marks:")
#     m3 = input("Enter C marks:")
#     m4 = input("Enter oracle marks:")
#     f.write("*" * 50 + "\n")
#     f.write(f"Student name:{name} \n")
#     f.write("*" * 50 + "\n")
#     f.write(f"python marks are: {m1} \n")
#     f.write(f"Java marks are: {m2} \n")
#     f.write(f"C marks are: {m3} \n")
#     f.write(f"oracle marks are: {m4} \n")
#     f.write("All the data updated to the file successfully")
#     choice = input("do you want to add the details of another student:[yes/no]")
#     if choice.lower() == "no":
#         break
#     elif choice.lower() == "yes":
#         continue
#     else:
#         print("please enter valid choice")
# f.close()


# ---------------------------------------------------------------------------------------------------------------------
# HOW TO READ THE DATA FROM THE FILE
# EX:1
# f = open("C:\\New folder\\dgs.txt","r")
# print(f.read())

# EX:2  to read n characters
# f = open("C:\\New folder\\trs.txt","r")
# print(f.read(11))


# EX:3 TO READ ONE LINE
# f = open("C:\\New folder\\trs.txt")
# print(f.readline(),end = "")
# print(f.readline())

# to read all lines

# f = open("C:\\New folder\\bjp.txt")
# while True:
#     line = f.readline()
#     if line != "\n":
#         if line != "":
#             print(line, end = "")
#         else:
#             break
# f.close()
# OR
# EX:4
# import time
# f = open("C:\\New folder\\bjp.txt")
# l = f.readlines()
# for each in l:
#     print(each, end="")
#     time.sleep(1)


# EX:5 WAP TO READ THE FILE FROM FILE AND WRITE TO ANOTHER FILE

# f1 = open("C:\\New folder\\dgs.txt")
# f2 = open("C:\\New folder\\trs.txt", "w")
# f3 = f1.read()
# f2.write(f3)
# f1.close()
# f2.close()


# writelines()
# ------------------------------------------------------------------------------------------------------------------
# =>Syntax:    filepointerobj.writelines(Iterable-object)
# =>This Function is used for writing any type of Iterable Object to the file in the form of str
# =>Examples:  refer   FileWriteEx2.py

# obj = {10, 20, 30, 10, 20, 30}
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\course era\\abc.txt", "w") as fp:
# 	fp.writelines(str(obj))
# 	print("Data Written to the file")

#----------------------------------------------------------------------------------------------------------------------
# 127 closing the file automatically by using with statement
# with open("C:\\New folder\\abc.txt", "w") as f:
#         f.write("Dammannagari \n")
#         f.write("Gangadhar \n")
#         f.write("sharma \n")
#         print(f.closed)
# print(f.closed)

# tell():

# with open("C:\\New folder\\abc.txt", "r") as f:
#     print(f.tell())
#     print(f.read(3))
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     f.write("MEDAK1 \n")
#     f.write("Telangana2 \n")
#     print(f.tell() )


# seek():
# with open("C:\\New folder\\abc.txt") as f:
    # f.seek(15)   MOVE THE CURSOR TO 15TH INDEX
    # print(f.tell())  15
    # print(f.read(5))  PQRST
    # f.seek(0)  MOVE THE CURSOR TO ZERO POSITION
    # print(f.tell())  0
    # print(f.read(10))  ABCDEFGHIJ


#  changing the data in the file by using seek method
# with open("C:\\New folder\\abc.txt", "r+") as file:
#     data = (file.read())
#     print("Data before changing")
#     print("$" * 40)
#     print(data)
#     file.seek(10)
#     print("Data after changing")
#     file.write(" sandeep!!!")


# CHECKING WHETHER THE REQUESTED FILE IS EXISTS OR NOT?
# import os
# file_name = input("please enter file name:")
# if os.path.isfile(file_name):
#     print(f"{file_name} is available")
# else:
#     print(f"{file_name} is not available")



# CHECKING WHETHER THE REQUESTED FILE IS EXISTS OR NOT? IF IT EXISTS PRINT ITS CONTENT TO THE CONSOLE

# import os
# file_name = input("please enter file name:")
# if os.path.isfile(file_name):
#     print(f"{file_name} is available")
#     print("Its content is:")
#     print("@" * 45)
#     with open (file_name) as f:
#         print(f.read())
# else:
#     print(f"{file_name} is not available")
# print(f.closed)

#----------------------------------------------------------------------------------------------------------------------
# 128

# f1 = open("C:\\New folder\\ghost.mp3", "rb")
# f2 = open("C:\\New folder\\ghostvikram.mp3", "wb")
# data = f1.read()
# f2.write(data)
# print("New image is available with the name:ghostvikram")



# Handling csv files:

# import csv
# with open("C:\\New folder\\emp.csv", "w", newline="") as f:
#     w = csv.writer(f)
#     w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])
#     while True:
#         eno = input("Enter employee number:")
#         ename = input("Enter employee name:")
#         esal = input("Enter employee salary:")
#         eaddr = input("Enter employee address:")
#         w.writerow([eno, ename, esal, eaddr])
#         print("Employee record inserted successfully")
#         choice = input("Do you want to add one more record?[yes|no]")
#         if choice in["NO","no","No","nO","N","n"]:
#             break
# print("All the data inserted successfully")


# Reading the data from csv file

# import csv
# with open("C:\\New folder\\emp.csv", "r") as f:
#     r = csv.reader(f)
#     data = list(r)
#     for row in data:
#         for col in row:
#             print(col,"\t",end=" ")
#         print()



# ZIPPING AND UNZIPPING OF FILES:

# from zipfile import *
# f = ZipFile("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\files.zip", "w", ZIP_DEFLATED)
# f1 = ("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\files.zip\\abcd1.txt")
# # f.write("C:\\New folder\\abcd1.txt")
# f.write("C:\\New folder\\abcd2.txt")
# f.write("C:\\New folder\\abcd3.txt")
# f.close()
# print("zip file created succesfully with name: files.zip")


# UNZIPPING OF FILES ie PRINING THE DATA TO THE CONSOLE:


# from zipfile import *
# f = ZipFile("C:\\New folder\\files.zip\\New folderfiles.zip", "r")
# names = f.namelist()
# for name in names:
#     print("File name:", name)
#     print("The content of the file:")
#     f1 = open(name, "r")
#     print(f1.read())
#     f1.close()
#     print()

#----------------------------------------------------------------------------------------------------------------------
# 129
# TO know current working directory
# import os
# c = os.getcwd()
# print(c)


# To Create a Sub Directory in the Current Working Directory:
# import os
# os.mkdir("python1")
# print("Sub directory created")


# TO CREATE A SUB SUB DIRECTORY
# import os
# os.mkdir("python1/python2")
# print("Sub sub directory created")


#To create multiple directories ie dir1 in that dir2 in that dir3 in that dir4
# import os
# os.makedirs("dir1/dir2/dir3/dir4")
# print("multiple directories created")



# TO REMOVE A DIRECTORY
# import os
# os.rmdir("dir1/dir2/dir3/dir4")    only last directory is removed
# print("dir4 removed")



# To remove complete path of directories
# import os
# os.removedirs("dir1/dir2/dir3")
# print("All directories removed")



# To rename a directory
# import os
# os.rename("dir1", "dgs")
# print("Rename is done successfully")

# To know the contents of directory
# import os
# l = os.listdir("dgs")
# print(l)
# print(len(l))


# To know the complete path of contents by using walk()

# import os
# x = os.walk("dgs")
# for a, b, c in x:
#     print("current directory path", a)
#     print("Directory", b)
#     print("Files", c)
#     print()


# to open calculator
# import os
# os.system("calc")
# ---------------------------------------------------------------------------------------------------------------------

# 141  ALiasing ( creating a duplicate ref variable for the same object)

# l1 = [10, 20, 30, 40]
# l2 = l1
# l2[3] = 100
# print(l1)



# def manager(a,b):
#     print(f"hello i am the manager of {a} and my name is {b}")
#
#     def cashier(a, b):
#         print(f"hello i am the cashier of {a} and my name is {b}")
#
#
#         def clerk(a, b):
#             print(f"hello i am the cashier of {a} and my name is {b}")
#         clerk(a="bjp", b="SBI")
#     cashier(b="trs", a="SBI")
#
#
# manager(a="SBI", b="dgs")

# for n in range(1, 21):
#     flag = True
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} is not a prime number")
#             flag = False
#             break
#     else:
#         if flag == True:
#             if n == 1:
#                 print(f"{n} is neither prime nor composite")
#             else:
#                 print(f"{n} is a prime number")



# password = input("enter your password:")
# count = 3
# while password != "12345":
#     count -= 1
#     if count == 0:
#         print("maximum chances exceeded.please try after 24 hours")
#         break
#     else:
#         if count == 1:
#             print(f"please enter valid password.You still have {count} chance")
#             password = input("enter your password:")
#         else:
#             print(f"please enter valid password.You still have {count} chances")
#             password = input("enter your password:")
#
# else:
#     print("valid user")


# def myfunc(e):
#     return e["year"]
# cars = [
#     {"car": "ford", "year": 2006},
#     {"car": "Maruthi", "year": 2000},
#     {"car": "BMW", "Year": 2019},
#     {"car": "vw", "year": 2011}
# ]
# cars.sort(key=myfunc)
# print(cars)




# def myFunc(e):
#   return e['year']
#
# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]
#
# cars.sort(key=myFunc)
# print(cars)


# f = open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\abcd1.txt", "w")
# f.write("dammannagari \n")
# f.write("prasad \n")
# f.write("sharma \n")
# f.close()
# import zipfile
# from zipfile import *
# comp_file = ZipFile("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\comp_file.zip", "w")
# comp_file.write("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\abcd.txt", compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\abcd1.txt", compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()



# import csv
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.csv", "w", newline="") as f:
#     w = csv.writer(f)
#     w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])
#     while True:
#         eno = input("Enter employee number:")
#         ename = input("Enter employee name:")
#         esal = input("Enter employee salary:")
#         eaddr = input("Enter employee address:")
#         w.writerow([eno, ename, esal, eaddr])
#         print("Employee record inserted successfully")
#         choice = input("Do you want to add one more record?[yes|no]")
#         if choice in["NO","no","No","nO","N","n"]:
#             break
# print("All the data inserted successfully")





# import csv
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.csv") as f:
#     r = csv.reader(f)
#     data = list(r)
#     for row in data:
#         for col in row:
#             print(col, "\t", end=" ")
#         print()

# import smtplib
# smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
# smtp_object.ehlo()
# smtp_object.starttls()



# a=int(input("Enter Value of a:"))
# b=int(input("Enter Value of b:"))
# print("-"*50)
# print("Arithemtic Operators")
# print("*" * 50)
# print("\n\tsum({},{})={}".format(a, b, a+b))
# print("\n\tsub({},{})={}".format(a, b, a-b))
# print("\n\tmul({},{})={}".format(a, b, a*b))
# print("\n\tDiv({},{})={}".format(a, b, a/b))
# print("\n\tFloor Div({},{})={}".format(a, b, a//b))
# print("\n\tMod({},{})={}".format(a, b, a%b))
# print("\n\tExp({},{})={}".format(a, b, a**b))
# print("#"*50)

# d = {}
# d["fruit_name"] = ["apple", "mango", "grapes", "orange"]
# print(d["fruit_name"][1])


# class Human:
#     def __init__(self):
#         self.name = input("enter your name:")
#         self.age = int(input("enter your age:"))
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#
# h = Human()
# h.display()


# class Parent:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def display(self):
#         print(self.Name)
#         print(self.Age)
#
# class Child(Parent):
#     def __init__(self, name, age, gender, address):
#         super().__init__(name, age)
#         self.Gender = gender
#         self.Address = address
#
#     def show(self):
#         super().display()
#         print(self.Gender)
#         print(self.Age)
#
# c = Child("DGS", 24, "MALE", "MEDAK")
# Child.show(c)



# import sys
# print("="*50)
# print("\tArithemetic Operations")
# print("="*50)
# print("\t1.Addition:")
# print("\t2.Substraction:")
# print("\t3.Multiplication:")
# print("\t4.Division:")
# print("\t5.Modulo Div:")
# print("\t6.Exponentiation:")
# print("\t7.Exit:")
# print("="*50)
# while True:
# 	ch = int(input("Enter Ur Choice:"))
# 	if (ch == 1):
# 		a = float(input("Enter First Value for Addition:"))
# 		b = float(input("Enter Second Value for Addition:"))
# 		print("\tsum({},{})={}".format(a, b, a + b))
# 	elif (ch == 2):
# 		a = float(input("Enter First Value for Substraction:"))
# 		b = float(input("Enter Second Value for Substraction:"))
# 		print("\tsub({},{})={}".format(a, b, a - b))
# 	elif (ch == 3):
# 		a = float(input("Enter First Value for Multiplication:"))
# 		b = float(input("Enter Second Value for Multiplication:"))
# 		print("\tMul({},{})={}".format(a, b, a * b))
# 	elif (ch == 4):
# 		a = float(input("Enter First Value for Division:"))
# 		b = float(input("Enter Second Value for Division:"))
# 		print("\tDivision({},{})={}".format(a, b, a / b))
# 		print("\tFloor Division({},{})={}".format(a, b, a // b))
# 	elif (ch == 5):
# 		a = float(input("Enter First Value for Modulo Div:"))
# 		b = float(input("Enter Second Value for Modulo Div:"))
# 		print("\tModulo Div({},{})={}".format(a, b, a % b))
# 	elif (ch == 6):
# 		a = float(input("Enter Base:"))
# 		b = float(input("Enter Power:"))
# 		print("\tpow({},{})={}".format(a, b, a ** b))
# 	elif (ch == 7):
# 		print("Thx for using Program")
# 		exit()
# 	else:
# 		print("{} is invalid Choice, try again:".format(ch))

# To print sum of natural numbers:
# n = int(input("Enter a positive number:"))
# c = 0
# for i in range(1, n+1):
#     c = c+i
# print(c)
#
#
# n = int(input("Enter a positive number:"))
# c = 0
# for i in range(1, n+1):
#     c = c+(i ** 2)
# print(c)
#
#
# n = int(input("Enter a positive number:"))
# c = 0
# for i in range(1, n+1):
#     c = c+(i ** 3)
# print(c)


# n = int(input("Enter a positive number:"))
# s = 0
# while n > 0:
#     s = s + n
#     n = n - 1
# print(s)


# n = int(input("Enter a positive number:"))
# s = 0
# while n > 0:
#     s = s + n ** 2
#     n = n - 1
# print(s)


# n = int(input("Enter a positive number:"))
# s = 0
# while n > 0:
#     s = s + n ** 3
#     n = n - 1
# print(s)


# n = int(input("Enter a number:"))
# s = 0
# for i in range(1, (n // 2) + 1):
#     if n % i == 0:
#         s += i
# if n == s:
#     print("\tperfect number")
# else:
#     print("\tnot a perfect number")



# wap to calculate factorial of a given number
# n = int(input("enter a number"))
# s = 1
# for i in range(1, n + 1):
#     s = s * i
# print(s)


# n = int(input("enter a number:"))
# n1 = n
# s = 1
# if n < 0:
#     print("Factorial does not exist for negative numbers")
# elif n == 0:
#     print("Factorial of zero is one")
# else:
#     while n > 0:
#         s = s * n
#         n = n - 1
#     print("Factorial of {} is {}".format(n1, s))


# s = "MALAYALAM"
# s1 = ""
# s2 = -1
# for each in s:
#     if each == s[s2]:
#         s1 = s1 + each
#         s2 = s2 - 1
# print(s1)



# l = [321, 456, 23, 67, 2, 6789]
# l1 = []
# for i in l:
#     l2 = 0
#     for j in str(i):
#         l2 = l2 + (int(j))
#     l1.append(l2)
# print(l1)

