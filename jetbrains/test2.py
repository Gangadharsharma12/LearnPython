# import random
# import sys
# player1 = random.choice(["paper", "scissor", "paper"]).lower()
# i = ["rock", "paper", "scissor", "end"]
# sp1 = 0
# sp2 = 0
# while True:
#     player2 = input("Select your choice:").lower()
#     print("player1 selected", player1)
#     while player2.lower() in i:
#         if player1 == "rock" and player2 == "paper":
#             print("Player2 won and the score of player 2 is ", end="")
#             sp2 = sp2 + 1
#             print(sp2)
#             break
#         elif player1 == "paper" and player2 == "scissor":
#             print("Player2 won and the score of player 2 is ", end="")
#             sp2 = sp2 + 1
#             print(sp2)
#             break
#         elif player1 == "scissor" and player2 == "rock":
#             print("Player2 won and the score of player 2 is ", end="")
#             sp2 = sp2 + 1
#             print(sp2)
#             break
#         elif player1 == player2:
#             print("round tied")
#             break
#         elif player2 == "end":
#             print("score of player1:", sp1)
#             print("score of player2:", sp2)
#             if sp1 > sp2:
#                 print("congratulations! player1 won the match")
#             elif sp1 == sp2:
#                 print("GAME TIE! NO RESULT")
#             else:
#                 print("congratulations! player2 won the match")
#             print("Game over")
#             sys.exit()
#         else:
#             print("player1 won and the score of player 1 ", end=" ")
#             sp1 = sp1 + 1
#             print(sp1)
#             break
#     else:
#         print("player2 selected invalid option")
#         break
#----------------------------------------------------------------------------------------------------------------------
# CREATING A CONSTRUCTOR:

# class Employee:
#
#
# def __init__(self, name, id):
#     self.id = id
#     self.name = name
#
#
# def display(self):
#     print("ID: %d \nName: %s" % (self.id, self.name))


# emp1 = Employee("John", 101)
# emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

# emp1.display()

# accessing display() method to print employee 2 information
# emp2.display()

# ---------------------------------------------------------------------------------------------------------------------

# Python Non-Parameterized Constructor(having only self)


# class Student:
#     # Constructor - non parameterized
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name):
#         print("Hello",name)
# student = Student()
# student.show("John")
# =====================================================================================================================

# Python Parameterized Constructor(more than self)

# class Student:
#     # Constructor - parameterized
#     def __init__(self, name):
#         print("This is parametrized constructor")
#         self.name = name
#     def show(self):
#         print("Hello",self.name)
# student = Student("John")
# student.show()
# ---------------------------------------------------------------------------------------------------------------------

# Python Default Constructor

# class Student:
#     roll_num = 101
#     name = "Joseph"
#
#     def display(self):
#         print(self.roll_num, self.name)
#
#
# st = Student()
# st.display()
# ---------------------------------------------------------------------------------------------------------------------

# More than One Constructor in Single class

# class Student:
#     def __init__(self):
#         print("The First Constructor")
#
#     def __init__(self):
#         print("The second contructor")
#
#
# st = Student()

# ---------------------------------------------------------------------------------------------------------------------


# CREATING AN INSTANCE VARIABLE:

# class Test:
#     def __init__(self, name, rollno):
#         self.Name = name
#         self.Rollno = rollno
#
#     def demo(self, marks, age):
#         self.Marks = int(marks)
#         self.Age = int(age)
#
# t = Test("Gangadhar", "19R01E0014")
# t.demo(10, 24)
# t.id = 11223344
# t.phno = 9550836114
# print(t.phno)
# print(t.id)
#-----------------------------------------------------------------------------------------------------------------------

# ACCESSING THE INSTANCE VARIABLES:

# class Test:
#     def __init__(self, name, rollno):
#         self.Name = name
#         self.Rollno = rollno
#         print(f"Hello my name is {self.Name}")
#         print(f"Hello my roll no is {self.Rollno}")
#
#     def demo(self, marks, age):
#         self.Marks = marks
#         print(f"Hello my marks are {self.Marks}")
#         self.Age = age
#         print(f"Hello my age is {self.Age}")
#
# t = Test("Gangadhar", "19R01E0014")
# t.demo(10, 24)
# t.id = 11223344
# t.phno = 9550836114
# print(t.id)
# print(t.phno)

#-----------------------------------------------------------------------------------------------------------------------

# Deleting the instance variables:

# class Test:
#     def __init__(self, name, rollno):
#         self.Name = name
#         self.Rollno = rollno
#         del self.Name
#         print(self.Name)    We get error because we deleted the variable error
#
#
#     def demo(self, marks, age):
#         self.Marks = int(marks)
#         self.Age = int(age)
#         del self.Age
#         print(f"Hello my age is {self.Age}")        We get error because we deleted the variable age
#
# t = Test("Gangadhar", "19R01E0014")
# t.demo(10, 24)
# t.id = 11223344
# t.phno = 9550836114
# del t.phno
# print(t.id)
# print(t.phno)                 We get error because we deleted the variable phno

# --------------------------------------------------------------------------------------------------------------------
# Counting the number of objects of a class
# class Student:
#     count = 0
#     def __init__(self):
#         Student.count += 1
# s1 = Student()
# s2 = Student()
# s3 = Student()
# print("The number of objects created are :", Student.count)


# ---------------------------------------------------------------------------------------------------------------------

# changing the values in one object will not effect the valuese in other object

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
# t1 = Test()
# t2 = Test()
# t1.a = 888
# t1.b = 999
# print(t1.__dict__)
# print(t2.__dict__)

# --------------------------------------------------------------------------------------------------------------------
#The instance variables which are deleted from one object,will not be deleted from other objects


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40
#
#     def m1(self):
#         del self.a
#
# t1 = Test()
# t2 = Test()
# print(t1.__dict__)       {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# t1.m1()
# print(t1.__dict__)      Here we wont get "a" value because we deleted "a" in m1 method
# del t1.b, t1.c, t1.d   here we are deleting all variables in t1 method
# print(t1.__dict__)     here we get empty dict because everything was deleted in t1
# print(t2.__dict__)     But here in t2 we get all variables because we only deleted variables in t1 object




# class Test:
#     def __init__(self):
#         self.a = 10
#
#     def m1(self):
#         self.a = 20
#         self.b = 30
#
# t1 = Test()
# Test.m1(t1)
# t1.a = 40
# t1.c = 50
# print(t1.__dict__)                           {'a': 40, 'b': 30, 'c': 50}
#--------------------------------------------------------------------------------------------------------------------
# 79  The complete story of static variable:

# EX:1 In general we can access static variable by using class name:

# class Test:
#     a = 10
# print(Test.a)

# EX:2 we can declare static variable with in the class directly and inside constructor or instance method we can declare by using class name

# class Test:
#      a = 10
#      def __init__(self):
#         Test.b = 20
#      def m1(self):
#         Test.c = 30
#
# t1 = Test()
# t1.m1()
# print(Test.__dict__)

# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x000001F629B58AF0>, 'm1': <function Test.m1 at 0x000001F629B589D0>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30}

# Ex:3 we can also declare inside class method by using cls or class name as cls and class name are pointing to same object
# We can declare the static variable inside static method by using class name
# We can declare the static variable outside of class by using class name
# class Test:
#     '''this is dgs'''
#     a = 10                declaring static variable directly
#     def __init__(self):
#         Test.b = 20       declaring inside constructor
#     def m1(self):
#         Test.c = 30       declaring inside instance method
#     @classmethod
#     def m2(cls):
#         cls.d1 = 40       declaring inside class method by using cls
#         Test.d2 = 400     declaring inside class method by using class name
#     @staticmethod
#     def m3():
#         Test.e = 50      declaring inside static method by using class name

# print(Test.__doc__)    here documentation will be displayed
# print(Test.__dict__)   here only "a" will be displayed which is declared directly( we can use print(Test.a) to get value of a
# t = Test()             here constructor is executed
# print(Test.__dict__)   here "a" and "b" are displayed
# t.m1()                 calling m1 method
# print(Test.__dict__)   here "a","b","c" are displayed
# Test.m2()              calling m2 method(class method)
# print(Test.__dict__)   here "a","b","c","d1","d2" are displayed
# Test.m3()              calling m3 method(static method)
# print(Test.__dict__)   here "a","b","c","d1","d2","e"  are displayed
# Test.f = 60            creating static variable outside of class by using class name
# print(Test.__dict__)   here "a","b","c","d1","d2","f" are displayed
# ---------------------------------------------------------------------------------------------------------------------

# EX:4 we can access static variable inside constructor and instance method by class name or self
# inside class method we can access static variable by using cls or class name
# inside static method we can access static variable by using  only class name
# outside of class we can access static variable by using object reference(only when static and instance not having same variable name) or class name
# Highly recommended to use class name for good programmming practice

# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m1(self):
#         print(Test.a)
#         print(self.a)
#     @classmethod
#     def m2(cls):
#         print(cls.a, "cls")
#         print(Test.a, "cls")
#     @staticmethod
#     def m3():
#         print(Test.a)
#
#
# t1 = Test()
# t1.m1()
# Test.m2()
# Test.m3()
# Test.m4 = 100
# print(Test.m4)
# print(t1.a)
# print(Test.a)


# EX:5 Modifying or updating the value of static variable:
# If static and instance variable has the same name then pvm will always give preference to instance variable
# If the variable is not available in instance then it will look for static variable.
# We can only modify static variable by using class name or cls variable
#  if we try to modify with self or reference variable it will not be effected in class level data
# class Test:
#     x = 10
#     def m1(self):
#         self.y = 20
#         self.x = 200
# t1 = Test()                             creating t1 object
# t2 = Test()                             creating t2 object
# t1.m1()                                 calling m1 method with t1
# print("t1:", t1.x, t1.y)                t1 object is created and x, y are assigned in t1 object(200, 20)
# t2.m1()                                 calling m1 method with t2
# print("t2:", t2.x, t2.y)                t2 object is created and x, y are assigned in t2 object(200, 20)
# t1.x = 888                              changing x value in t1 to 888 which is replaced by 200
# t1.y = 999                              changing y value in t1 to 999 which is replaced by 20
# print("t1:", t1.x, t1.y)                888   999
# print("t2:", t2.x, t2.y)                t2 values remain same (200, 20)
# Test.x = 100                            changing static variable to 100 by using class name.If we use obj ref then again instance variable will change
# print(Test.x)                           100 will be printed

#-----------------------------------------------------------------------------------------------------------------------

# 80
# How to delete static variables:
# anywhere: del Class name.variable name
# with in the class method: del cls.variable name
# Example is written in notes


# Local variables

# we can declare local variables inside a method directly.
# local variables are created at the time of method execution and destroyed once the method execution completed
# Local variables can not be accessed from the outside of the method and the scope is limited upto to that method only
# We need not to delete the local variables explicitly.
# ---------------------------------------------------------------------------------------------------------------------

# Bank mini application

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
#         while amt % 500 != 0:
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

# 81   GETTER AND SETTER METHODS

# class Student:
#     def setname(self, name):
#         self.name = name
#
#     def getname(self):
#         return self.name
#
#     def setmarks(self, marks):
#         self.marks = marks
#
#     def getmarks(self):
#         return self.marks
#
#
# n = int(input("enter the number of students:"))
# for i in range(n):
#     s = Student()
#     name = input("enter the student name:")
#     s.setname(name)
#     marks = int(input("enter the marks:"))
#     s.setmarks(marks)
#     print("hello", s.getname())
#     print("Your marks are:", s.getmarks())
#     print()

# -------------------------------------------------------------------------------------------------------------------
# CLASS METHOD:
# If we are not using any instance variable any we are using only static variables
# we may use static variables
# @class method is mandatory
# cls is always first argument
# cls is reference to current class object.By using cls we can aceess class level variables

# EX:1
# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print(f"{name} walks with {Animal.legs} legs")
# Animal.walk("Lion")

# -------------------------------------------------------------------------------------------------------------------
# EX:2

# class Student:
#
#     college_name = "CMR INSTITUTE OF TECHNOLOGY"
#     departement = "MBA"
#
#     @classmethod
#     def display(cls, x):
#         print(f"hello my name is {x} and i am from {cls.college_name}.")
#         print(f"i am from {cls.departement} marketing.")
#
# Student.display("Gangadhar")

#--------------------------------------------------------------------------------------------------------------------
# EX:3  WAP TO KNOW THAT HOW MANY OBJECTS GOT CREATED
# class Test:
#     count = 0
#     def __init__(self):
#         Test.count += 1
#     @classmethod
#     def display(cls):
#         print(f"The total number of objects are {Test.count}")
#
# t = Test()
# t1 = Test()
# t2 = Test()
# t3 = Test()
# t5 = Test()
# Test.display()

#----------------------------------------------------------------------------------------------------------------------

# 83  Passing members of one class to another class.Here members means variables and methods

# EX:1

# class Employee:
#
#     def __init__(self, eno, en_ame, esa_l):
#         self.e_no = eno
#         self.e_name = en_ame
#         self.e_sal = esa_l
#
#     def show(self):
#         print("employee number:", self.e_no)
#         print("employee name:", self.e_name)
#         print("employee sal:", self.e_sal)
#
#
# class Test:
#     def new_name(emp):
#         emp.e_name = "Arunachala shiva"
#         emp.e_sal += 20000
#         emp.e_no = 1234
#         emp.show()
#
#
# emp_ = Employee(8888, "DGS", 40000)
# Test.new_name(emp_)

# -------------------------------------------------------------------------------------------------------------------

# EX:2
# class Demo:
#     def __init__(self,name, town,state, country):
#         self.Name = name
#         self.Town = town
#         self.State = state
#         self.Country = country
#
#     def show(self):
#         print(f"Hello my name is {self.Name}")
#         print(f"Hello my town is {self.Town}")
#         print(f"Hello my state is {self.State}")
#         print(f"Hello my country is {self.Country}")
#
#
# class Another:
#     def change(self):
#         self.Town = "Medak"
#         self.State = "Telangana"
#         self.Country = "India"
#         self.show()
#
# d = Demo("Dgs", "m", "t", "I")
# Another.change(d)

#--------------------------------------------------------------------------------------------------------------------
# EX:3

# class Employee():
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#
#
# class Student:
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#
#
# class Customer:
#     def show(cus):
#         print(cus.eno)
#         print(cus.ename)
#         print(cus.esal)
#
# e = Student(9999, "dgs", 32000)
# e1 = Employee(8888, "sks", 45000)
# Customer.show(e)
# Customer.show(e1)

# ------------------------------------------------------------------------------------------------------------------
# EX:4

# class Employee:
#     def __init__(self,ename):
#         self.ename = ename
#
#
# class Student:
#     def __init__(self, sid):
#         self.sid = sid
#
#
# class Demo:
#     def m1(x):
#         print(type(x))
#         print(x.ename)
#
#     def m2(y):
#         print(type(y))
#         print(y.sid)
#
# e = Employee("DGS")
# Demo.m1(e)
# s = Student(100)
# Demo.m2(s)
# -------------------------------------------------------------------------------------------------------------------
# EX:5

# class Student:
#     def __init__(self, sname):
#         self.sname = sname
#
#     def m1(self):
#         print(self.sname)
#
# class Test:
#     def m2(x):
#         x.m1()
#
# s = Student("Hello world!")
# Test.m2(s)
# ------------------------------------------------------------------------------------------------------------------

# class Test:
#     def __init__(self, ename, eaddress, esal):
#         self.ename = ename
#         self.eaddress = eaddress
#         self.esal = esal
#
#     def show(self):
#         print(self.ename)
#         print(self.eaddress)
#         print(self.esal)
#
# class Demo:
#     def __init__(self, state, pincode):
#         self.state = state
#         self.pincode = pincode
#     def m1(x):
#         t.show()
#
#
# class Employee:
#     def m2(y):
#         print(y.state)
#         print(y.pincode)
#
#
# t = Test("dgs", "medak", 40000)
# d = Demo("ts", 502110)
# Demo.m1(t)
# Employee.m2(d)
# -------------------------------------------------------------------------------------------------------------------
# EX:6  WE CAN HAVE SAME METHOD AND ITS ARGUMENTS DEFINED IN MULTIPLE CLASSES

# class Test:
#     @staticmethod
#     def method_1(self):
#         print("method-1 of Test class")
#
# class Demo:
#     @staticmethod
#     def method_1(self):
#         print("Method 1 of Demo class")
#
# Test.method_1(10)
# Demo.method_1(100)

# -------------------------------------------------------------------------------------------------------------------
# EX:7 WE CAN ALSO PASS TWO CLASSES VARIABLES IN THE THIRD CLASS SIMULTANEOUSLY

# class Test:
#     def m1(x):
#         print("Test class")
#
# class Demo:
#     def m1(x):
#         print("Demo method")
#
# class Coffe:
#     def m1(a, b):
#         a.m1()
#         b.m1()
#
#
# t = Test()
# d = Demo()
# Coffe.m1(d, t)
#----------------------------------------------------------------------------------------------------------------------

#84 INNER CLASSES

# class Outer:     creating outer class
#     def __init__(self):    outer class constructor
#         print("Outer class execution")
#
#     class Inner1:   creating inner class
#         def __init__(self):   creating inner class constructor
#             print("Inner1 class execution")
#
#         def m1(self):   inner class m1 method
#             print("Inner1 class method.")
#
#     class Inner2:   creating Inner2 class
#
#         def __init__(self):  Inner2 class constructor
#             print("Inner2 class execution")
#
#         def m2(self):   Inner2 class m2 method
#             print("Inner2 class method.")


# o = Outer()   creating object for outer class
# i = o.Inner1()   calling inner1 class with outer class(syntax is inner class ref var = outer class ref var.inner class name)
# i.m1()  calling inner class m1 method
# i1 = o.Inner2()   calling inner2 class by creating i1 as ref var
# i1.m2()             calling inner2 class m2 method

#--------------------------------------------------------------------------------------------------------------------
# EX:2
# class Outer:
#     def __init__(self):
#         print("Outer class object creation")
#
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation")
#
#         class InnerInner:
#             def __init__(self):
#                 print("InnerInner class object creation")
#
#             def m1(self):
#                 print("InnerInner class m1 method")
#
#
# o = Outer()    ref var for outer class
# i = o.Inner()  creating ref var for Inner class by passing i as ref var
# i1 = i.InnerInner()  creating ref var for InnerInner class by using Inner class ref var
# i1.m1()   calling  InnerInner class m1 method

#----------------------------------------------------------------------------------------------------------------------

# 85


# class Human:
#     class Head:
#         def talk(self):
#             print("Talking.....")
#
#         class Brain:
#             def think(self):
#                 print("Thinking....")
#
#
# human = Human()            obj created for Human class
# head = human.Head()        obj created for Head class.Here "head" is the ref var to Head class
# head.talk()                calling talk method which is in Head class
# brain = head.Brain()       creating ref var for Brain class.Here Head class is the outer class for Brain class. Hence we used Head class ref var
# brain.think()              calling think method in Brain class.

# --------------------------------------------------------------------------------------------------------------------
# class University:
#     def __init__(self,name,branch):
#         print("University object creation")
#         self.name = name
#         self.branch = branch
#
#     def display(self):
#         self.x = self.Dept()
#         self.x.m1()
#         self.x.method1()
#
#
#     class Dept:
#             def m1(self):
#                 print("Deapartement object creation")
#             def method1(self):
#                 print("Deapartement class method1")
#                 self.x = self.Branch()
#                 self.x.m1()
#
#             class Branch:
#                     def m1(self):
#                         print("Branch class m1 method")
#
#
# u = University("dgs", "b.sc")
# u.display()

# ----------------------------------------------------------------------------------------------------------------------
# class Human:
#     def __init__(self, name):
#         print("Human object execution")
#         self.name = name
#         self.a = self.Head()
#         self.a.talk()
#
#     class Head:
#         def __init__(self):
#             print("Head object execution")
#             self. b = self.Brain()
#             self.b.think()
#
#
#         def talk(self):
#             print("Talking....")
#
#         class Brain:
#             def __init__(self):
#                 print("Brain object execution")
#                 self.c = self.Lungs()
#
#             def think(self):
#                 print("Thinking....")
#                 self.c.kidney()
#
#             class Lungs:
#                 def __init__(self):
#                     print("Lungs object execution....")
#                     self.d = self.Information()
#                     self.d.info()
#                     print("hello")
#
#
#                 def kidney(self):
#                     print("Please drink more water")
#
#                 class Information:
#                     def info(self):
#                         print("I am full busy with")
#
# human = Human("Gangadhar")




# class School:
#     def __init__(self, name, standard):
#         self.name = name
#         self.standard = standard
#         self.display()
#         self.inter = self.Inter()
#         self.inter.m1("Adarsha junior college", "twelve")
#
#
#
#     def display(self):
#         print("my school name is:", self.name)
#         print("I studied upto:", self.standard)
#
#
#     class Inter:
#         def m1(self, name, standard):
#             self.clgname = name
#             self.standard = standard
#             print("i studied inter at:", self.clgname)
#             print("I studied upto", self.standard)
#             self.degree = self.Degree("Aurora degree college", "Bsc")
#
#
#         class Degree:
#             def __init__(self, name, standard):
#                 self.mba = self.Mba()
#                 self.name = name
#                 self.standard = standard
#                 print("my degree college name is:", self.name)
#                 print("i studied", self.standard)
#                 self.mba.method1("CMRIT", "MBA")
#
#             class Mba:
#                 def method1(self, name, standard):
#                     self.name = name
#                     self.standard = standard
#                     print("I studied mba at", self.name)
#                     print(f"I studied {self.standard} at {self.name}")
#
#
# scl = School("siddartha", "tenth class")

# -------------------------------------------------------------------------------------------------------------------
# class Geeksforgeeks:             [In this code we called methods from outside as well as inside]
#
#     def __init__(self):
#         self.inner = self.Inner()
#         self.show()
#         print()
#         self.inner.show()
#
#
#     def show(self):
#         print('This is an outer class')
#
#     class Inner:
#
#         def __init__(self):
#             self.innerclassofinner = self.Innerclassofinner()
#
#
#         def show(self):
#             print('This is the inner class')
#             print()
#             self.innerclassofinner.show()
#             print()
#
#         class Innerclassofinner:
#
#             def show(self):
#                 print('This is an inner class of inner class')
#
# outer = Geeksforgeeks()
# outer.show()
# print()
#
# gfg1 = outer.inner
# gfg1.show()
# print()
#
#
# gfg2 = outer.inner.innerclassofinner
# gfg2.show()
#  -------------------------------------------------------------------------------------------------------------------

# AREA OF CIRCLE IS PI.r2
# AREA OF SQUARE IS A = a2
# AREA OF TRIANGLE IS 1/2 * b * h
# AREA OF RECTANGLE IS A = length * width
# AREA OF TRAPEZUM = (a + b / 2) * h
#  AREA OF RHOMBUS = 1/2 * D1 * D2


# import math
# class Circle:
#     def __init__(self, a1):
#         self.a1 = a1
#         print(f"The area of circle is {math.pi * self.a1}")
#         self.square = self.Square(10)
#
#
#     class Square:
#         def __init__(self, a):
#             self.a = a
#             print(f"The area of square is {self.a ** 2}")
#             self.triangle = self.Triangle()
#             self.triangle.method1(10, 20)
#
#         class Triangle:
#             def method1(self, a, b):
#                 self.a = a
#                 self.b = b
#                 print(f"The area of Triangle with breadth 10 and height 20 is {0.5 * self.a * self.b}")
#                 self.rectangle = self.Rectangle(10, 20)
#
#             class Rectangle:
#                 def __init__(self, l, w):
#                     self.l = l
#                     self.w = w
#                     print(f"The area of rectangle with length 10 and breath 20 is {self.l * self.w}")
#                     self.trapezium = self.Trapezium(10, 20, 30)
#                 class Trapezium:
#                     def __init__(self, a, b, h):
#                         self.a = a
#                         self.b = b
#                         self.h = h
#                         print(f"The area of trapezium is {(self.a + self.b) / 2 * self.h}")
#                         self.rhombus = self.Rhombus()
#                         self.rhombus.method2(20, 40)
#
#                     class Rhombus:
#                         def method2(self, a, b):
#                             self.a = a
#                             self.b = b
#                             print(f"The area of rhombus is {0.5 * self.a * self.b}")
#
#
# circle = Circle(10)

# ---------------------------------------------------------------------------------------------------------------------

# 86  NESTED METHODS:
# Method inside method is allowed in python
#with in the method if some functionality is repeatedly required then we use method inside method
#python book and street light example

# class Test:
#     def m1(self):
#         pass
#
#         def calc(a, b):
#             print("The addition is:", a + b)
#             print("The difference is:", a - b)
#             print("The product is", a * b)
#             print("The division is", a / b)
#             print("The floor division is", a // b)
#             print("The modulus is", a % b)
#             print()
#         calc(10, 20)
#         calc(50, 60)
#         calc(90, 10)
#
#
# t = Test()
# t.m1()
# ---------------------------------------------------------------------------------------------------------------------
# 90  oops part 2(INHERITANCE)
# All the memebers of the parent class(constructor,functions,variables) are by default available to the child class
# We need not to define the members of parent class again in child class explicitly
# Syntax: class Child class name(parent class name)
# The biggest advantage is code reusability and code extendability

# EX:1
# class Parent:                            Declaring parent class
#     def m1(self):                        creating parent class m1 method
#         print("Parent class m1 method")

# class Child(Parent):    inheritating the members of parent class to  child class
#     def m2(self):       creating m1 method in child class
#         print("Child class m2 method")

# c = Child()          creating an object for child class
# c.m1()               calling parent class m1 method
# c.m2()               calling child class m2 method

# ---------------------------------------------------------------------------------------------------------------------
# EX:2
# When parent class and child class having same methods then only Child class method is executed
# class Parent:
#     def m1(self):
#         print("Parent class m1 method")
#
# class Child(Parent):
#     def m1(self):
#         print("Child class m1 method")
#
# c = Child()
# c.m1()
# -------------------------------------------------------------------------------------------------------------------
# EX:3  When we create a reference variable to child class but child class does not have any constructor then parent class constructor will be executed automatically
#  But preference is always given to the child class constructor first
#  If both child and parent classes are having constructors then parent class constructor will be ignored by pvm


# class Parent:
#     def __init__(self):
#         print("Parent class constructor")
#
#
# class Child(Parent):
#     pass

# c = Child()  Here automatically parent class constructor is executed because child class has no constructor

# -------------------------------------------------------------------------------------------------------------------
# EX:4  Full fledged example to show parent class members are  by default available to child class
# We can access parent class instance variable by using  only child class ref var
# We can access parent class instance method by using  only child class ref var
# We can access parent class static variable by using child class ref var, class name of child, class name of parent
# We can access parent class (class method) by using child class ref var, class name of child, class name of parent
# We can access parent class (static method) by using child class ref var, class name of child, class name of parent


# class Parent:
#     a = 10
#
#     def __init__(self):
#         print("Parent class constructor method")
#         self.b = 20
#
#     def m1(self):
#         print("parent class instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("parent class static method")
#
#
# class Child(Parent):
#     pass

# c = Child()        Parent class constructor is executed
# # print(c.a)       printing parent class static method
# # print(c.b)       printing parent class instance variable
# c.m1()             Printing Parent class instance method
# Parent.m2()        Printing Parent class (class method)
# Parent.m3()        Printing Parent class (static method)
# ------------------------------------------------------------------------------------------------------------------
# super(): From child class if we want to access parents class instance method we use super
# Because when child class is having constructor then parent class constructor is not executed

# EX:1
# class Parent:
#     def __init__(self):
#         self.a = 888
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.b = 999
#
# c = Child()
# print(c.b)
# print(c.a)
#--------------------------------------------------------------------------------------------------------------------

# EX:2

# class Person:
#     def __init__(self, name, age):    parent class constructor
#         self.Name = name              parent class instance variable
#         self. Age = age               parent class instance variable
#
#     def eatdrink(self):               parent class instance method
#         print("Eat rice and drink water...")
#
# class Employee(Person):
#     def __init__(self, ename, eage, eno, esal):     child class constructor
#         super().__init__(ename,eage)                calling parent class constructor to execute.Here arguments need not be same but they should be same in number
#         self.Eno = eno                              child class instance variable
#         self.Esal = esal                            child class instance variable
#
#     def work(self):                                 child class instance method
#         print("practising Python")
#
#     def getdetails(self):                          child class instance method
#         print("Employee name",self.Name)
#         print("Employee age", self.Age)
#         print("Employee number", self.Eno)
#         print("Employee salary", self.Esal)
#
# e = Employee("Gangadhar", 24, 242425, 30000)    obj creation for child class by passing 4 arguments.Automatically child class constructor is executed
# e.eatdrink()                                    calling parent class instance method by using obj ref of child class
# e.work()                                        calling child class instance method (work)
# e.getdetails()                                  calling child class instance method(getdetails)

# -------------------------------------------------------------------------------------------------------------------

# My own example:
# class Parent:
#     def m1(self,ename,eage):
#         self.Ename = ename
#         self.Eage = eage
#
#
# class Child(Parent):
#     def m1(self, ename, eage, esal, eid, eaddress):
#         super().m1(ename, eage)
#         self.Esal = esal
#         self.Eid = eid
#         self.Eaddress = eaddress
#
#     def display(self):
#         print(f"Hello my name is {self.Ename}")
#         print(f"Hello my age is {self.Eage}")
#         print(f"Hello my salary is {self.Esal}")
#         print(f"Hello my id  is {self.Eid}")
#         print(f"Hello my address is {self.Eaddress}")
#
# c = Child()
# c.m1("Gangadhar", 24, 200000,121234, "Medak")
# c.display()
# -----------------------------------------------------------------------------------------------------------------------
# 92  TYPES OF INHERITANCE:

# Single inheritance(one parent having one child)

# class Parent:
#     def m1(self):
#         print("Parent class m1 method")
#
#
# class Child(Parent):
#     def m2(self):
#         print("child class m2 method")
#
#
# c = Child()
# c.m1()
# c.m2()


# EX:2
# class Student:
#     def __init__(self, firstname, lastname):
#         self.fisrstname = firstname
#         self.lastname = lastname
#     def studentname(self):
#         return f"{self.fisrstname} {self.lastname}"
#
# class Employee(Student):
#     def __init__(self, firstname, lastname, role):
#         self.role = role
#         super().__init__(firstname, lastname)
#         print(super().studentname())
#     def work(self):
#         return f"{super().studentname()} works as {self.role}"
#
# obj = Employee("Gangadhar", "sharma", "python developer")
# # print(obj.studentname())
# print(obj.work())

#----------------------------------------------------------------------------------------------------------------------
# 2 Multi level inheriatance( Grandfather - Father - Grandson)(Dhirubai - mukesh- Akash)
# Grandson can access the methods in both Grandfather class and Father class
#
# class Parent:
#     def m1(self):
#         print("Parent class m1 method")
#
# class Child(Parent):
#     def m2(self):
#         print("child class m2 method")
#
# class Subchild(Child):
#     def m3(self):
#         print("subchild class m3 method")
#
# s = Subchild()
# s.m1()
# s.m2()
# s.m3()
# ---------------------------------------------------------------------------------------------------------------------

# EX:2

# class Person:
#     def __init__(self, firstname, lastname):
#         self.fisrstname = firstname
#         self.lastname = lastname
#     def personname(self):
#         return f"{self.fisrstname} {self.lastname}"
#
# class Student(Person):
#     def __init__(self, firstname, lastname, Id):
#         self.Id = Id
#         super().__init__(firstname, lastname)
#
#     def studentId(self):
#         return f"student Id: {self.Id}"
#
#
# class Employee(Student):
#     def __init__(self, firstname, lastname, Id, role):
#         self.role = role
#         super(). __init__(firstname, lastname, Id)
#
#     def work(self):
#         return f"{self.personname()} works as {self.role} with Id {self.Id}"
#
# obj = Employee("Gangadhar", "sharma", 12335, "python developer")
# print(obj.personname())
# print(obj.studentId())
# print(obj.work())


# ----------------------------------------------------------------------------------------------------------------------
# 3.Hierachical Inheritance(One parent having many childs)
# Dhirubai ambani has 2 sons...his property is given to his sons...he can access his property in any of his son class
# but mukesh ambani can not access anil ambani property and vice versa

# class Parent:
#     def m1(self):
#         print("Parent class m1 method")
#
#
# class Child(Parent):
#     def m2(self):
#         print("child class m2 method")
#
# class Subchild(Parent):
#     def m3(self):
#         print("subchild class m3 method")

# c = Child()
# c.m1()
# c.m2()
# c.m3()           AttributeError: 'Child' object has no attribute 'm3'(anil is trying to access mukesh ambani property)
# s = Subchild()
# s.m1()
# s.m3()
# s.m2()            AttributeError: 'Subchild' object has no attribute 'm2'(mukesh is trying to access anil property)

# ---------------------------------------------------------------------------------------------------------------------

# ex:2

# class Person:
#     def __init__(self, firstname, lastname):
#         self.fisrstname = firstname
#         self.lastname = lastname
#     def personname(self):
#         return f"{self.fisrstname} {self.lastname}"
# class Student(Person):
#     def __init__(self, firstname, lastname,Id):
#         super().__init__(firstname, lastname)
#         self.Id = Id
#     def studentId(self):
#         return f"Student Id:{self.Id} with name {self.personname()}"
#
# class Employee(Person):
#     def __init__(self, firstname, lastname, role):
#         self.role = role
#         super().__init__(firstname, lastname)
#     def work(self):
#         return f"{self.personname()} works as {self.role}"
#
# obj = Student("Gangadhar", "sharma", 12345)
# print(obj.studentId())
# obj = Employee("Gangadhar", "sharma", "python developer")
# print(obj.work())

# ---------------------------------------------------------------------------------------------------------------------
# 4.Multiple inheritance

# Multiple parent classes to single child class
# when we pass more than one parent class in child class pvm will always follow the order in which we declared
# First preference is given to the class in which we are declaring multiple parents.If the method found here it wont go further
# if that class is not having that method then pvm will follow the order
# if it does not contain in any of the classes we get attribute error

# class Parent1:
#     def m1(self):
#         print("parent1 class method")
#
#
# class Parent2:
#     def m2(self):
#         print("Parent2 class method")
#
#
# class Parent3(Parent1, Parent2):
#     def m3(self):
#         print("Parent3 class method")
#
# p = Parent3()
# p.m1()
# p.m2()
# p.m3()
# ------------------------------------------------------------------------------------------------------------------
# ex:2
# What if two classes having same method:
# Note: When we created an object and if we have a constructor then constructor will be executed first followed by the
# class in which we declared parents and followed by the order
#
# class Parent:
#     def m1(self):
#         print("parent1 class method")
#
#
# class Parent2:
#     def m2(self):
#         print("Parent2 class method")
#
#     def dgs(self):
#         print("dgs")
#
#
# class Parent3:
#     def __init__(self):
#         print("Parent3 class constructor execution")
#
#
#
# class Child(Parent3, Parent, Parent2):
#     def m3(self):
#         print("Child class method")
#
#
# c = Child()
# c.m1()
# c.m2()
#-----------------------------------------------------------------------------------------------------------------------
# EX:3

# class Person:
#     def __init__(self, firstname, lastname):
#         self.fisrstname = firstname
#         self.lastname = lastname
#     def personname(self):
#         return f"{self.fisrstname} {self.lastname}"
#
# class Student:
#     def __init__(self, Id):
#         self.Id = Id
#     def studentId(self):
#         return f"Student Id:{self.Id}"
#
# class Employee(Person, Student):
#     def __init__(self, firstname, lastname, Id, role):
#         self.role = role
#         Person.__init__(self, firstname, lastname)
#         Student.__init__(self, Id)
#
#     def work(self):
#         return f"{self.personname()} works as {self.role} with Id {self.Id}"
#
# obj = Employee("Gangadhar", "sharma", "12345", "python developer")
# print(obj.personname())
# print(obj.studentId())
# print(obj.work())
# ------------------------------------------------------------------------------------------------------------------
# 5. Hybrid inheritance:(written in pink binding notes shri:side)
# combination of all above 4 methods

# Every class in python is the child class of object class..if our class is not child of any class then it is the child
# class of object class

# class A:pass
# class B(A) : pass
# class C(A) : pass
# class D(B, C) : pass
# print(D.mro())
# --------------------------------------------------------------------------------------------------------------------
# EX:2

# class X:
#     def m1(self):
#         print("x class m1 method")
#
#
# class Y:
#     def m1(self):
#         print("Y class m1 method")
#
#
# class Z:
#     def m1(self):
#         print("Z class m1 method")
#
#
# class A(Y, Z):
#     def m1(self):
#         print("A class M1 method")
#
#
# class B(Y, Z):
#     def m1(self):
#         print("B method m1 method")
#
#
# class M(A,B):
#     def m1(self):
#         print("M class m1 method")
#
# m = M()
# m.m1()
# print(X.mro())
# print(Y.mro())
# print(Z.mro())
# print(A.mro())
# print(B.mro())
# print(M.mro())

# ---------------------------------------------------------------------------------------------------------------------

# 95 COMPLETE STORY OF SUPER():
# EX:1  If parent class have child class have different methods then we can call methods of parent class in child class
#       by using self
# class Parent:
#     def m1(self):
#         print("parent class method")
#
#
# class Child(Parent):
#     def m2(self):
        # self.m1()              m1 method by default available to child also..so to access m1 in child class we use self.m1()
        # print("child class method")


# c = Child()
# c.m2()
# ------------------------------------------------------------------------------------------------------------------

# EX:2 [If parent and child having same method we can not call by using self because self.m1() refers to child class m1()
# Hence recursion takes place. So here we can use super]

# [If parent class and child class contains a member with the same name then to call that method explicitly in child class
# we use super]

# super() is a built in function which is used for calling parent class constructor,methods,variables,explictily in child class


# class Parent:
#     def m1(self):
#         print("parent class method")
#
#
# class Child(Parent):
#     def m1(self):
#         Parent.m1(self)                               CALLING PARENT CLASS m1 method  (we can call by 2 ways)
#         super().m1()                                  CALLING PARENT CLASS m1 method
#         print("child class method")
#
#
# c = Child()

#c.m1()

# ------------------------------------------------------------------------------------------------------------------
# EX:3

# class Parent:
#     a = 50
#
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class m1 method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")
#
#     def method1(self):
#         print(super().a)  /   print(Parent.a)
#         super().m1()      /   self.m1()
#         super().m2()      /   self.m2()
#         super().m3()      /   self.m3()
#         super().__init__() /    Parent.__init__(self)
#
#
# c = Child()
# c.method1()

# --------------------------------------------------------------------------------------------------------------------
# EXAMPLE TO SHOW TWO CHILD CLASSES HAVING DIFFERENT PARENTS

# class Parent:
#     a = 50
#
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class m1 method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
#
# class Parent2:
#     a = 100
#     def __init__(self):
#         print("Parent2 class constructor")
#
#     def m1(self):
#         print("Parent2 class m1 method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent2 class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent2 class static method")
#
#
#
#
# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")
#
#     def method1(self):
#         print(super().a)
#         super().m1()
#         super().m2()
#         super().m3()
#         super().__init__()
#
#
#
# class Child1(Parent2):
#     def __init__(self):
#         print("Child class constructor")
#
#     def method1(self):
#         print(super().a)
#         super().m1()
#         super().m2()
#         super().m3()
#         super().__init__()
#
# class Child(Parent):
#     def __init__(self):
#         print("Child class constructor")
#
#     def method1(self):
#         print(super().a)
#         super().m1()
#         super().m2()
#         super().m3()
#         super().__init__()
#
#
# c1 = Child()
# c1.method1()
# print()
# c = Child1()
# c.method1()
#--------------------------------------------------------------------------------------------------------------------

# EX:4


# class Person:
#     def __init__(self, name, age, height):
#         print("Constructor execution")
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def display(self):
#         print("NAME:", self.name)
#         print("AGE:", self.age)
#         print("HEIGHT:", self.height)
#
#
# class Student(Person):
#     def __init__(self, name, age, height, weight, sid, saddress):
#         super().__init__(name, age, height)
#         self.weight = weight
#         self.sid = sid
#         self.saddress = saddress
#
#     def show(self):
#         super().display()
#         print("WEIGHT:", self.weight)
#         print("SID:", self.sid)
#         print("SADDRESS:", self.saddress)
#         print()
#
#
# class Employee(Person):
#     def __init__(self, name, age, height, weight, esal, eid):
#         super().__init__(name, age, height)
#         self.weight = weight
#         self.esal = esal
#         self.eid = eid
#
#
#     def see(self):
#         super().display()
#         print("WEIGHT:", self.weight)
#         print("ESAL:", self.esal)
#         print("EID:", self.eid)
#
#
# s = Student("Gangadhar", 24, 5.9, 65, 9550836114, "Medak")
# s.show()
# e = Employee("Sharma", 24, 5.9, 65, 30000, 121235)
# e.see()
# ------------------------------------------------------------------------------------------------------------------

# 96
# [If we have multilevel inheritance and if we use super()..then pvm will check that method in immediate parent class
# ie the class which we mentioned in parent class place]

# if that method is not having that method then pvm will look for the parent class of respective method

# HOW TO CALL PARTICULAR SUPER CLASS:

# class name.methodname(current ref variable)   (B.m1(self))
# In the above example if we use B.m1(self) in class E...pvm will directly move to class B



# class A:
#     def m1(self):
#         print("A class m1 method")
#
#
# class B(A):
#     def m1(self):
#         print("B class m1 method")
#
#
# class C(B):
#     def m2(self):
#         print("C class m1 method")
#
#
# class D(C):
#     def m1(self):
#         print("D class m1 method")
#
#
# class E(D):
#     def m1(self):
#         B.m1(self)       directly calling B class m1()...if B class dont have m1 it will go for the parent class of B
#
# e = E()
# e.m1()
#-----------------------------------------------------------------------------------------------------------------------
# VARIOUS POSSIBILITIES
# [By using super() in child class constructor we can invoke parent class constructor, parent class ainstance method
# parent class class method and parent class static method]
# class P:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class Instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
# class C(P):
#     def __init__(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#
# c = C()
# ----------------------------------------------------------------------------------------------------------------------
# 2.[By using super() in child class Instance method  we can invoke parent class constructor, parent class instance method
# parent class class method and parent class static method]

#[Here we get "Parent class constructor" two times because child class in not having constructor. so automatically
# parent class constructor will be executed and again we are calling parent class constructor by using super()]

# class P:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class Instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
# class C(P):
#     def method1(self):
#         super().__init__()
#         super().m1()
#         super().m2()
#         super().m3()
#
# c = C()
# c.method1()

# ----------------------------------------------------------------------------------------------------------------------
#3. [From child class we can not call parent class constructor and instance variable because they both
# are releated to objects]

# [But we can call parent class class method and static method because they both are no way releated to objects
# we can call them directly by using class name without creating ref variable]

# Here parent class constructor is executed because child class is not having constructor

# class P:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class Instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
# class C(P):
#     @classmethod
#     def method1(cls):
#         super().m2()
#         super().m3()
#
# c = C()
# c.method1()

# -----------------------------------------------------------------------------------------------------------------

# 4. From child class static method we can not use super() directly

# class P:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("Parent class Instance method")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method")
#
#
# class C(P):
#     @staticmethod
#     def method1(cls):
#         super().m2()
#         super().m3()
#
# c = C()
# c.method1()
# --------------------------------------------------------------------------------------------------------------------
# import sys
# while True:
#     pizza_size = input("please enter the size of pizza you want S/M/L/Q:").upper()
#     bill = 0
#     if pizza_size == "S" or "M" or "L" or "Q":
#         if pizza_size == "S":
#             bill = 100
#             print(f"The size of small pizza is {bill}")
#         elif pizza_size == "M":
#             bill = 200
#             print(f"The cost of Medium pizza is RS {bill}")
#
#         elif pizza_size == "L":
#                 bill = 300
#                 print(f"The cost of Large pizza is RS {bill}")
#
#         else:
#             if pizza_size == "Q":
#                 print("Thank you for using our service. Kindly share your valuable feedback")
#                 sys.exit()
#     extra_pepper = input("Do you want to add extra pepper[YES/NO]:").lower()
#     if extra_pepper == "yes" and pizza_size == "S":
#         bill += 20
#     elif extra_pepper == "yes" and (pizza_size == "M" or pizza_size == "L"):
#         bill += 30
#
#     extra_cheese = input("Do you want to add extra cheese[YES/NO]:").lower()
#     if extra_cheese == "yes":
#         bill += 20
#
#     else:
#         if pizza_size != "S" or "M" or "L" or "Q":
#             print("Invalid size choosen")
#             option = input("Do you want to enter the size again[YES/NO]:").lower()
#             if option == "no":
#                 break
#
# print(f"Your total bill is RS {bill}")



# import pywhatkit as kit
# kit.sendwhatmsg("+917989478498", "hello", 15, 6)


# x = int(input("please enter the last number:"))
# y = int(input("enter the last value:"))
# for i in range(1, x+1):
#     if i == 1:
#         print(f"printing {i}st table:")
#         print("----------------------------------------")
#     elif i == 2:
#         print(f"printing {i}nd table:")
#         print("----------------------------------------")
#     elif i == 3:
#         print(f"printing {i}rd table:")
#         print("----------------------------------------")
#     else:
#         print(f"printing {i}th table:")
#         print("----------------------------------------")
#     for j in range(1, y+1):
#         print(f"{i} * {j} = {i*j}")
#     print("----------------------------------------")


# n = int(input("enter the starting range:"))
# n1 = int(input("enter the ending range:"))
# l = []
# for i in range(n, n1+1):
#     flag = 0
#     for j in range(1, i):
#         if i % j == 0:
#             flag += j
#     if flag == i:
#         l.append(i)
# print(f"The perfect numbers from {n} to {n1} are:")
# for each in l:
#     print(l)
#     break



# n = int(input())
# for i in range(1, n+1):
#     x = 1
#     for j in range(1, i+1):
#         x = x*j
#     print("The factorial of {} is {}".format(j, x))
#


# s = input()
# x = -1
# print("forward direction:", end="")
# for each in s:
#     print(each, end="")
# print("\nback ward direction:", end=" ")
# for i in s:
#     if x < -len(s):
#         break
#     else:
#         print(s[x], end="")
#     x = x - 1

# s = input()
# s1 = ""
# s2 = -1
# for each in s:
#     if s2 < -len(s):
#         break
#     else:
#         if each == s[s2]:
#             s1 += each
#         s2 -= 1
# if s == s1:
#     print("palindrome")
# else:
#     print("np")



# n = int(input("Enter the number:"))
# for i in range(n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             print(f"{i} is not a prime number")
#             break
#     else:
#             print(f"{i} is a prime number")


# n=int(input("enter the range:"))
# for i in range(n):
#     m=i
#     s=0
#     a=str(i)
#     while i>0:
#         r=i%10
#         s=s+r**len(a)
#         i=i//10
#     if (m==s):
#         print(m)


# n=int(input("enter a number:"))
# a=str(n)
# m=n
# s=0
# while n>0:
#           r=n%10
#           s=s+r**len(a)
#           n=n//10
# if (m==s):
#     print("ARMSTRONG")
# else:
#     print("NA")




# class Student:
#     def __init__(self, sname):
#         self.sname = sname
#
#     def m1(self):
#         print(self.sname)
#
# class Test:
#     def m2(x):
#         x.m1()
#
# s = Student("Hello world!")
# Test.m2(s)



# s = "hyderabad"
# s1 = ""
# for each in s:
#     if s.index(each) == 0 or s.index(each) == 3:
#         s1 += each.upper()
#     else:
#         s1 += each.lower()
# print(s1)

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     @property
#     def msg(self):
#         return self.name + " got grade " + self.grade
#
#     @property
#     def msg2(self):
#         print("hello this is message2")
#
# s1 = Student("nia", "B")
# s1.grade = "A"
# print("name:", s1.name)
# print("grade:", s1.grade)
# s1.msg2
# print(s1.msg)


import os
os.environ["PYSPARK_PYTHON"] = "python"
from pyspark import SparkContext
sc = SparkContext("local", "Collect app")
words = sc.parallelize(
    ["java",
     "python",
     "pyspark"]
)

coll = words.collect()
print(f"elements in rdd------>{coll}")