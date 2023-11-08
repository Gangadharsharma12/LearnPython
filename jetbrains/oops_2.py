# Inheritence
# EX:1 (90)

# class Parent:
#     def m1(self):
#         print("m1 method")
#
#
# class Child(Parent):
#     def m2(self):
#         print("m2 method")
#
#
# c = Child()
# c.m1()
# c.m2()



# EX:2

# class Parent:
#     a = 10
#
#     def __init__(self):
#         print("Parent class constructor method")
#         self.b = 20
#
#     def m1(self, c):
#         print("parent class instance method")
#         self.c = 30
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
#
#
# c = Child()
# print(c.a)
# print(c.b)
# Parent.m2()
# Child.m3()





# EX:3
# class Person:
#     def __init__(self, name, age):
#         self.Name = name
#         self. Age = age
#
#     def eatdrink(self):
#         print("Eat rice and drink water...")
#
# class Employee(Person):
#     def __init__(self, ename, eage, eno, esal):
#         Person.__init__(self, ename, eage)
#         self.Eno = eno
#         self.Esal = esal
#
#     def work(self):
#         print("practising Python")
#
#     def getdetails(self):
#         print("Employee name", self.Name)
#         print("Employee age", self.Age)
#         print("Employee number", self.Eno)
#         print("Employee salary", self.Esal)
#
# e = Employee("Gangadhar", 24, 242425, 30000)
# e.eatdrink()
# e.work()
# e.getdetails()

# ----------------------------------------------------------------------------------------------------------------------
# 91
# COMPOSITION AND AGGREGATION
# COMPOSITION EX:1
#
# class University:
#     def __init__(self):
#         self.dept = self.Departement()
#         print("hello")
#
#     class Departement:
#         print("Departement class executed")
#
#
# u = University()


#----------------------------------------------------------------------------------------------------------------------
# 92 S.I

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


# EX:2 MLI

# class Parent:
#     def m1(self):
#         print("Parent class m1 method")


# class Child(Parent):
#     def m2(self):
#         print("child class m2 method")
#
# class Subchild(Child):
#     def m3(self):
#         print("subchild class m3 method")

# s = Subchild()
# s.m1()
# s.m2()
# s.m3()



#EX :3 HI

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
#
# c = Child()
# c.m1()
# c.m2()
# c = Subchild()
# c.m1()
# c.m3()



# EX:4 Multiple Inheritance:

# class Parent:
#     def m1(self):
#         print("parent1 class method")
#
#
# class Parent2:
#     def m2(self):
#         print("Parent2 class method")
#
#
# class Child(Parent, Parent2):
#     def m3(self):
#         print("Child class method")
#
# c = Child()
# c.m1()
# c.m2()
# c.m3()

# EXAMPLE FOR 2 CLASSES HAVING SAME METHOD

# class Parent:
#     def m1(self):
#         print("parent1 class method")
#
#
# class Parent2:
#     def m1(self):
#         print("Parent2 class method")
#
# class Parent3:
#     def __init__(self):
#         print("Parent3 class constructor execution")
#
#
# class Child(Parent3, Parent, Parent2):
#     def m3(self):
#         print("Child class method")
#
#
# c = Child()
# c.m1()
# c.m3()
# ----------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------



