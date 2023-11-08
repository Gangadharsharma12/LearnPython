# 97
# class Book:
#     def __init__(self, pages, author):
#         self.author = author
#         self.pages = pages
#
#     def __add__(self, other):
#         total = self.author + other.author
#         t = self.pages + other.pages
#         return total, t
#
#
# b1 = Book(200, "Gangadhar")
# b2 = Book(200, "sharma")
# print(b1 + b2)
# print(b2 + b1)
#
 -----------------------------------------------------------------------------------------------------------------------
# # 98 EX:1

# class Student:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __gt__(self, other):
#         if self.marks == other.marks:
#             result = self.name > other.name
#             return result
#
#         else:
#             result = self.marks > other.marks
#             return result
#
#
# s1 = Student("Durga", 100)
# s2 = Student("Apple", 200)
# s3 = Student("Ravi", 100)
# print(s1 < s3)
# print(s1 < s3)


# EX:2

# class Employee:
#     def __init__(self, name, salary):
#         self.Name = name
#         self.Salary = salary
#
#
#
# class Timesheet:
#     def __init__(self, name, days):
#         self.Name = name
#         self.Days = days
#
#     def __gt__(self, other):
#         result = self.Name > other.Name
#         return result
#
#
# e = Employee("DGS", 1000)
# t = Timesheet("TRS", 50)
# print(t < e)


# __str__()

# class Student:
#     def __init__(self, name, marks):
#         self.Name = name
#         self.Marks = marks
#
#     def __str__(self):
#         return f"Hello my name is {self.Name} and my marks are {self.Marks}"
#
#
# class Employee:
#     def __init__(self, name, sal):
#         self.Name = name
#         self.Sal = sal
#
#     def __str__(self):
#         return f"Hello my name is {self.Name} and my salary is {self.Sal}. Thank you"
#
#
#
#
# s1 = Student("DGS", 100)
# s2 = Student("TRS", 150)
# E1 = Employee("Dgs", 30000)
# E2 = Employee("TRS", 40000)
#
# print(s1)
# print(s2)
# print(E1)
# print(E2)

# ---------------------------------------------------------------------------------------------------------------------

# 99


# class Student:
#     def __init__(self, marks):
#         print("constructor execution")
#         self.Marks = marks
#
#     def __add__(self, other):
#         print("Add magic method execution")
#         n = self.Marks + other.Marks
#         n1 = Student(n)
#         return n1
#
#     def __str__(self):
#         print("Str magic method execution")
#         return str(self.Marks)
#
#
# s1 = Student(100)
# s2 = Student(200)
# s3 = Student(500)
# s4 = Student(600)
# print(s1 + s2)
# print(s1 + s2 + s3)
# print(s1 + s2 + s3 + s4)


# class Test:
#     def __init__(self, *args):
#         print("Variable number1")
#
#
#     def __init__(self, *args):
#         print("Variable number2")
#
#     def __init__(self, *args):
#         print("Variable number3")
#
#     def __init__(self, *args):
#         print("Variable number4")
#
# t = Test()
# t1 = Test(10)
# t2 = Test(10, 20)
# t3 = Test(10, 20, 30, 40,50)

#-----------------------------------------------------------------------------------------------------------------------
# 101 EX:1
# class Parent:
#     def property(self):
#         print("Property is required")
#
#     def car(self, bike):
#         print("Maruthi 800")
#
#
# class Child(Parent):
#     def car(self):
#         super().car(self)
#         print("TATA NEXON")
#
# c = Child()
# c.property()
# c.car()
# -----------------------------------------------------------------------------------------------------------------------
#                                       OOPS PART 4
# 102
# EX:1
# from abc import abstractmethod
# class Car:
#     @abstractmethod
#     def getnoofwheels(self):
#         pass


# EX:2

# from abc import abstractmethod,ABC
# class Car(ABC):
#     @abstractmethod
#     def getnoofwheels(self):
#         pass


# EX:3

# from abc import abstractmethod,ABC
# class Vehicle(ABC):
#     @abstractmethod
#     def getnoofwheels(self):
#         pass
#
# class Bus(Vehicle):
#     def getnoofwheels(self):
#         return 6
#
# class Bike(Vehicle):
#     def getnoofwheels(self):
#         return 2
#
#
# b = Bus()
# print(b.getnoofwheels())
#
# b = Bike()
# print(b.getnoofwheels())



# EX:4
# from abc import abstractmethod, ABC
# class Parent(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#
#     @abstractmethod
#     def m3(self):
#         pass
#
#
# class Child(Parent):
#     def m2(self):
#         print("Hello")
#
#     def m3(self):
#         print("World")
#
#     def m1(self):
#         print("Namastee")
#
#
# c = Child()
# c.m1()
# c.m2()
# c.m3()



# EX:5
# from abc import abstractmethod, ABC
# class Parent(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#
#     @abstractmethod
#     def m3(self):
#         pass
#
#
# class Child(Parent):
#     def m2(self):
#         print("Hello")
#
#     def m1(self):
#         print("Hai")
#
#     def m3(self):
#         print("namastee")
#
#
# class Child_2(Child):
#     def m2(self):
#         print("Dgs")
#
#     def m1(self):
#         print("Trs")
#
#     def m3(self):
#         print("TSK")
#
# c = Child()
# c.m1()
# c.m2()
# c.m3()
# c = Child_2()
# c.m1()
# c.m2()
# c.m3()




# EX:6
# from abc import abstractmethod, ABC
# class Parent(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#
#     @abstractmethod
#     def m3(self):
#         pass
#
# class C1(Parent):
#     @abstractmethod
#     def m4(self):
#         pass
#     def m5(self):
#         pass
#     def m6(self):
#         pass
#
#
# class C2(C1):
#     def m1(self):
#         print("Hello")
#
#     def m2(self):
#         print("Hai")
#
#     def m3(self):
#         print("How are you")
#
#     def m4(self):
#         print("I am fine")
#
#     def m5(self):
#         print("nice")
#
#     def m6(self):
#         print("Thank you..bye")
#
#
# c = C2()
# c.m1()
# c.m2()
# c.m3()
# c.m4()
# c.m5()
# c.m6()
#----------------------------------------------------------------------------------------------------------------------
# 102
# EX:1
# from abc import *
# class Getstudent(ABC):
#     @abstractmethod
#     def getstumarks(self):
#         pass
#     @abstractmethod
#     def getstuname(self):
#         pass
#
# class Test(Getstudent):
#     def getstumarks(self):
#         return "Student marks are 100"
#
#     def getstuname(self):
#         return "student name is Gangadhar"
#
#
# t = Test()
# print(t.getstumarks())
# print(t.getstuname())


# EX:2


# from abc import *
# class Getstudent(ABC):
#     @abstractmethod
#     def m1(self): pass
#     @abstractmethod
#     def m2(self): pass
#     @abstractmethod
#     def m3(self): pass
#
# class Abs(Getstudent):
#     def m1(self):
#         print("M1 method")
#
#     def m2(self):
#         print("M2 method")
#
# class Concrete(Abs):
#     def m3(self):
#         print("M3 method")
#
#     def m4(self):
#         print("M4 add on method")
#
# c = Concrete()
# c.m1()
# c.m2()
# c.m3()
# c.m4()

#----------------------------------------------------------------------------------------------------------------------
# 106
# EX:1
# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance
#         print(self.Getbal())
#
#     def Getbal(self):
#         a = int(input("Please enter your user id:"))
#         b = input("Please enter your password:")
#         if a == 12345 and b == "ICICI@123":
#             return  "your current account balance is", self.__balance
#         else:
#             return "Please provide valid credentials"
#
# b = Bank(60000)

#----------------------------------------------------------------------------------------------------------------------
# 110 Bank application- Mini project

# import sys
# class Customer:
#     '''This bank application is developed by dgs '''
#     bankname = "STATE BANK OF INDIA"
#     def __init__(self, name, balance = 0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amt):
#         self.balance += amt
#
#     def withdraw(self, amt):
#         if amt == self.balance:
#             self.balance -= amt
#         elif amt > self.balance:
#             print("insufficient funds...can not perform this operation now")
#             sys.exit()
#         else:
#             self.balance -= amt
#     def display(self):
#         print("Your current balance is:", self.balance)
#
# print(Customer.__doc__)
# print("Hello, welcome to", Customer.bankname)
# name = input("please enter your name:")
# c = Customer(name)
# while True:
#     print('d-Deposit \nw-Withdraw \nb-balance enquiry\ne-exit')
#     option = input("please select your choice:")
#     if option.lower() == "d":
#         amt = float(input("enter amount to deposit:"))
#         while amt % 500 != 0:
#             print("please insert only 500 denominations")
#             amt = float(input("enter amount to deposit:"))
#         c.deposit(amt)
#
#     elif option.lower() == "w":
#         amt = float(input("enter amount to withdraw:"))
#         while amt % 500 and amt % 200 != 0:
#             print("please select only 500 denominations")
#             amt = float(input("enter amount to deposit:"))
#         c.withdraw(amt)
#
#     elif option.lower() == "b":
#         c.display()
#
#     elif option.lower() == "e":
#         print("Thank you for choosing our banking services")
#         sys.exit()
#
#     else:
#         print("Please select a valid option")
# ---------------------------------------------------------------------------------------------------------------------

