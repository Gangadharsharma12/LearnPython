# # class Student:
# #     '''this class is developed by dgs'''
# # print(Student.__doc__)
# # help(Student)
#
#
# # class Sandeep:
# #
# #
# #     def __init__(self):
# #         self.name = 'DGS'
# #         self.age = 25
# #        #print(f'{self.name} is of {self.age} years')
# #
# #
# # s1 = Sandeep()
# # s2 = Sandeep()
# # s1.name = 'Shyam'
# # print(s1.name)
# # print(s2.name)
#
#
#
#
# class Student:
#     def __init__(self):
#         self.name = "gangadhar"
#         self.rollno = "19R01E0014"
#         self.marks = 200
#
#     def talk(self):
#         print("hello my name is", self.name)
#         print("hello my roll no is",self.rollno)
#         print("hello my marks are", self.marks)
#
# stu = Student()
# print(stu.name)
# print(stu.rollno)
# print(stu.marks)
# stu.talk()


# class Student:
#     '''this class is developed by dgs'''
#     def __init__(self,name, rollno, marks):
#         print("constructor execution is started")
#         self.peru = name
#         self.kramasankhya = rollno
#         self.markulu = marks
#     def talk(self):
#         print("Hello my name is", self.peru)
#         print("Hello my roll no is", self.kramasankhya)
#         print("Hello my marks are", self.markulu)
#
# print(Student.__doc__)
# s = Student("sunny", 101, 90)
# s1 = Student("Bunny", 102, 95)
# s2 = Student("chinny", 103, 100)
# s2.talk()
# print("student1:", s.peru, s.kramasankhya, s.markulu)
# print("student2:", s1.peru, s1.kramasankhya, s1.markulu)
# print("student3:", s2.peru, s2.kramasankhya, s2.markulu)


# class Test:
#     def __init__(self):
#         print("this is a constructor")
#
#     def speek(self):
#         print("this is a method")
#         print(20 * 30)
#
# t = Test()
# t.speek()


# class Student:
#     def __init__(self, na, rno,marks):
#         self.name = na
#         self.rollno = rno
#
#
# s = Student("sunny", 101, 90)
# s1 = Student("dgs",  100, 95)
# print(s.name, s.rollno)
# print(s1.name)


# class Test:
#     def m1(self,x):
#         print("method execution....") # default constructor is provided by pvm
#         print(x)
#
#
# t = Test()
# t.m1(20)


# class Test:
#     def __init__(self):
#         print(f"constructor execution....{id(self)}")
#
# t = Test()
# t.__init__()
# t.__init__()


# class Test:
#     def __init__(self):
#         print("no arg constructor")
#
#     def __init__(self,x):
#         print("one arg constructor")
#
# t = Test(19)


# class Test:
#     def __init__(self, name):
#         self.name = name
#         print("my name is", name)
#
# class Demo:
#     def __init__(self, name):
#         self.name = name
#         print("my name is", name)
#
# t = Test("sunny")
# d = Demo("sachin")
# t.__init__("bunny")
# d.__init__("dravid")


# def test():
#     print("This is a Test function")
# class Test:
#     def Test(self):
#         print("class name is same as method name")
#
#
# test()
# t = Test()
# t.Test()


# class Test:
#     def Test(self):
#         print('This is a method')
#     def Test(self):
#         print('This is also a method ')
#     def Test(self):
#         print('Normal Method')
#
# obj = Test()
# obj.Test()


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def get_bonus(self,name):
#         print("my name is",name)
#         return name
# e = Employee("dgs", 24,10000)
# print(e.get_bonus("sks"))


# word = input()
# n = -1
# for each in  word:
#     if each != word[n]:
#         print("false")
#         break
#     else:
#         print("true")
#         n1 -= 1
#         break


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello, I am {self.name}!")
#
#
# user = Person(input())
# user.greet()


# class Student:
#     principal = "Durga"
#     director = "nagoor babu"
#
#     @classmethod
#     def getclginfo(cls):
#         print("principal name:", cls.principal)
#         print("director name:",cls.director)
#
#     @staticmethod
#     def getaverage(a, b, c):
#         return (a + b + c) / 3
#
# Student.getclginfo()
# print("The avarage is",Student. getaverage(10, 20, 30))


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#
#     def m1(self):
#         self.c = 30
#
#
# t1 = Test()
# t1.m1()
# t2 = Test()
# t2.d = 40
# print(t1.__dict__)
# print(t2.__dict__)


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         print(self.a)
#         print(self.b)
#     def m1(self):
#         print(self.a)
#         print(self.b)
#
# t1 = Test()
# t1.m1()
# print(t1.a)
# print(t1.b)


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
# print(t1.__dict__)
# t1.m1()
# print(t1.__dict__)
# del t1.b, t1.c, t1.d
# print(t1.__dict__)



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



# class Test:
#     def __init__(self):
#         self.a = 10
#
#     def m1(self):
#         self.a = 20
#         self.b = 30
#
# t1 = Test()
# t1.m1()
# t1.a = 40
# t1.c = 50
# print(t1.__dict__)


# -----------------------------------------------------------------------------------------------------------------------


# class Test:
#     a = 10
# print(Test.a)


# class Test:
#     a = 10
#     def __init__(self):
#         Test.b = 20
#     def m1(self):
#         Test.c = 30
# t1 = Test()
# t1.m1()
# print(Test.__dict__)


# class Test:
#     '''this is dgs'''
#     a = 10
#     def __init__(self):
#         Test.b = 20
#     def m1(self):
#         Test.c = 30
#     @classmethod
#     def m2(cls):
#         cls.d1 = 40
#         Test.d2 = 400
#     @staticmethod
#     def m3():
#         Test.e = 50
# print(Test.__doc__)
# print(Test.__dict__)
# t = Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# Test.m2()
# print(Test.__dict__)
# Test.m3()
# print(Test.__dict__)
# Test.f = 60
# print(Test.__dict__)


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
#         print(cls.a)
#         print(Test.a)
#     @staticmethod
#     def m3():
#         print(Test.a)
#
#
# t1 = Test()
# t1.m1()
# Test.m2()
# Test.m3()
# print(t1.a)
# print(Test.a)


# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20
# t1 = Test()
# t2 = Test()
# print("t1:", t1.x, t2.y)  10  20
# print("t2:",t2.x, t2.y)   10  20
# t1.x = 888
# t1.y = 999
# print("t1:", t1.x, t1.y)888  999
# print("t2:",t2.x, t2.y) 10   20


# class Test:
#     x = 10
#     def __init__(self):
#         self.x = 100
#         self.y = 20
# t1 = Test()
# t2 = Test()
# print("t1:", t1.x, t2.y)100 20
# print("t2:",t2.x, t2.y)100  20
# Test.x = 888
# print("t1:", t1.x, t1.y)100  20
# print("t2:",t2.x, t2.y)100   20


# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20
# t1 = Test()
# t2 = Test()
# print("t1:", t1.x, t2.y) 10  20
# print("t2:",t2.x, t2.y)  10  20
# Test.x = 888
# t1.y = 999
# print("t1:", t1.x, t1.y) 888  999
# print("t2:",t2.x, t2.y)  888  20


# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20
#
#     def m1(self):
#         self.x = 888
#         self.y = 999
# t1 = Test()
# t2 = Test()
# t1.m1()
# print("t1:", t1.x, t1.y)  888  999
# print("t2:",t2.x, t2.y)   10   20


# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20
#     @classmethod
#     def m1(cls):
#         cls.x = 888
#         cls.y = 999
# t1 = Test()
# t2 = Test()
# t1.m1()
# print("t1:", t1.x, t1.y)  888  20
# print("t2:",t2.x, t2.y)   888  20
# print("Test:",Test.x, Test.y)888  999


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
#         while amt % 500  and amt % 200 != 0:
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

# -----------------------------------------------------------------------------------------------------------------------


# Types of methods:

# Instance method:

# class Student:
#     def __init__(self, x,y):
#         self.naam = x
#         self.markulu = y
#
#     def display(self):
#         print("hello my name is:",self.naam)
#         print("hello my marks are:",self.markulu)
#
#     def grade(self):
#         if self.markulu >= 90:
#             print("you got first grade")
#         elif self.markulu >= 80:
#             print("You got second grade")
#         elif self.markulu >= 70:
#             print("You got third grade")
#         else:
#             print("you are failed....sorry")
#
# x = input("enter your name:")
# y = int(input("enter your marks to find your grade:"))
# s = Student(x, y)
# s.display()
# s.grade()


# class Student:
#     def __init__(self, x,y):
#         self.naam = x
#         self.markulu = y
#
#     def display(self):
#         print("hello my name is:",self.naam)
#         print("hello my marks are:",self.markulu)
#         self.grade()
#
#     def grade(self):
#         if self.markulu >= 90:
#             print("you got first grade")
#         elif self.markulu >= 80:
#             print("You got second grade")
#         elif self.markulu >= 70:
#             print("You got third grade")
#         else:
#             print("you are failed....sorry")
# times = int(input("enter the number of students:"))
# for i in range(times):
#     x = input("enter your name:")
#     y = int(input("enter your marks to find your grade:"))
#     s = Student(x, y)
#     s.display()
#     print()


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





# class Animal:
#     legs = 4
#     @classmethod
#     def walk(cls, name):
#         print(f"{name} walks with {cls.legs} legs")
# Animal.walk("Lion")


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
# name = input()
# Student.display(name)

# ----------------------------------------------------------------------------------------------------------------------

# class Student:
#     @staticmethod
#     def test(a, b):
#         return (a + b) / 2
#
# print(Student.test(10, 20))



# class Test:
#     @staticmethod
#     def sum(a, b):
#         return a + b
#
#     @staticmethod
#     def subtract(a, b):
#         return a - b
#
#     @staticmethod
#     def product(a, b):
#         return a * b
#
# print(Test.sum(10, 20))
# print(Test.subtract(20, 10))
# print(Test.product(10, 20))

# --------------------------------------------------------------------------------------------------------------------

# passing one class variables and methods in another class:

# ex:1
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


# ex:2


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

# e = Employee(9999, "dgs", 32000)
# Customer.show(e)



# ex:3

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


# my own example:
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


# ex:4

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
# Coffe.m1(t, d)


# ---------------------------------------------------------------------------------------------------------------------
# 84  INNER CLASSES(with out existing one type of object their is no chance of existing another object)

# EX:1

# class Outer:
#     def __init__(self):
#         print("Outer class execution")
#
#     class Inner1:
#         def __init__(self):
#             print("Inner1 class execution")
#
#         def m1(self):
#             print("Inner1 class method.")
#
#     class Inner2:
#
#         def __init__(self):
#             print("Inner2 class execution")
#
#         def m2(self):
#             print("Inner2 class method.")
#
#
# o = Outer()
# i1 = o.Inner1()
# i1.m1()
# i1 = o.Inner2()
# i1.m2()



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
# o = Outer()
# i = o.Inner()
# i1 = i.InnerInner()
# i1.m1()

# ---------------------------------------------------------------------------------------------------------------------
# 85 Inner class demo programs

# EX:2
#
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
# human = Human()
# head = human.Head()
# head.talk()
# brain = head.Brain()
# brain.think()



# EX:1


# class Human:
#     def __init__(self, name):
#         print("Human object execution")
#         self.name = name
#         self.head = self.Head()
#
#     def info(self):
#         print("Hello i am", self.name)
#         print("I am full busy with")
#         self.head.talk()
#         self.head.brain.think()
#
#
#     class Head:
#         def __init__(self):
#             print("Head object execution")
#             self. brain = self.Brain()
#
#         def talk(self):
#             print("Talking....")
#
#         class Brain:
#             def __init__(self):
#                 print("Brain object execution")
#                 self.lungs = self.Lungs()
#
#             def think(self):
#                 print("Thinking....")
#
#             class Lungs:
#                 def __init__(self):
#                     print("Lungs object execution....")
#
#
# human = Human("Gangadhar")
# human.info()



# EX:3

# class Person:
#     def __init__(self):
#         print("Person object creation...")
#         self.dob = self.Dob(dd,mm,yyyy)
#         # dob = person.Dob(2, 10, 1997)
#         self.dob.show()
#         # dob.show()
#
#
#     class Dob:
#         def __init__(self,dd,mm,yyyy):
#             print("Dob object creation...")
#             self.DD = dd
#             self.MM = mm
#             self.YYYY = yyyy
#
#         def show(self):
#             print(f"Hello...my DOB iS {self.DD}/{self.MM}/{self.YYYY}")
#
#
# dd = int(input())
# mm = int(input())
# yyyy = int(input())
# person = Person()







# class Person:
#     def __init__(self):
#         print("Person object creation...")
#         self.dob = self.Dob(dd, mm, yyyy)
#         self.dob.show()
#
#     class Dob:
#         def __init__(self,dd, mm, yyyy):
#             print("Class object creation...")
#             self.DD = dd
#             self.MM = mm
#             self.YYYY = yyyy
#
#         def show(self):
#             print(f"Hello,i born on {self.DD}/{self.MM}/{self.YYYY}")
#
# dd = input()
# mm = input()
# yyyy = input()
# person = Person()



# ---------------------------------------------------------------------------------------------------------------------

# 86 EX:1

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
# 87

# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

# DESTRUCTOR
# EX:1
# import time
# class Test:
#     def __init__(self):
#         print("Initializing activity")
#
#     def __del__(self):
#         print("clean up process")
#
# t = Test()
# time.sleep(10)
# print("The end")
# t1 = Test()
# t2 = Test()
# print("END")


# EX:2

import time
# class Test:
#     def __init__(self):
#         print("constructor executed successfully")
#
#     def __del__(self):
#         print("destructor executed successfully")


# t = Test()
# t1 = t
# t2 = t1
# del t
# time.sleep(10)
# print("object not yet destroyed after deleting t")
# del t1
# time.sleep(10)
# print("object not yet destroyed after deleting t1")
# print("object not yet destroyed after deleting t2")
# del t2



# import sys
# class Test:
#     pass
# t = Test()
# t1 = t
# t2 = t1
# del t1
# del t2
# print(sys.getrefcount(t))

# n = int(input())
# total = 1
# while n > 0:
#     num = n % 10
#     total *= num
#     n = n // 10
# print(total)


