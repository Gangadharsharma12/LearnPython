# class Parent:
#     def m1(self):
#         print("parent class method")
#
#
# class Child(Parent):
#     def m1(self):
#         super().m1()
#         print("child class method")
#
#
# c = Child()
# c.m1()


# EX:2

# class Parent:
#     a = 50
#
#     def __init__(self):
#         print("Parent class constructor")
#
#     @staticmethod
#     def m1():
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
#         print(Parent.a)
#         self.m1()
#         self.m2()
#         self.m3()
#         super().__init__()
#
#
# c = Child()
# c.method1()



# EX:3
# class Person:
#     def __init__(self, name, age, height, weight):
#         print("constructor execution")
#         self.Name = name
#         self.Age = age
#         self.Height = height
#         self.Weight = weight
#
#     def show(self):
#         print("NAME:", self.Name)
#         print("AGE:", self.Age)
#         print("HEIGHT:", self.Height)
#         print("WEIGHT:", self.Weight)
#
#
# class Student(Person):
#     def __init__(self, name, age, height, weight, sid, saddress):
#         super().__init__(name, age, height, weight)
#         self.Sid =sid
#         self.Saddress = saddress
#
#
#     def see(self):
#         super().show()
#         print("SID:", self.Sid)
#         print("SADDRESS:", self.Saddress)
#         print()
#
#
#
#
# class Employee(Person):
#     def __init__(self, name, age, height, weight, eno, esal, eid):
#         super().__init__(name, age, height, weight)
#         self.Eno = eno
#         self.E_sal = esal
#         self.Eid = eid
#
#     def show(self):
#         super().show()
#         print("ENO:", self.Eno)
#         print("ESAL:", self.E_sal)
#         print("EID:", self.Eid)
#
#
# s = Student("Gangadhar", 24, 5.9, 65, 9550836114, "Medak")
# s.see()
# e = Employee("Sharma", 24, 5.9, 65, 7989478498, 30000, 121231)
# e.show()

# EX:4
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
#         super(E, self).m1()
#
# e = E()
# e.m1()


# ---------------------------------------------------------------------------------------------------------------------
# def change(x):
#     x[1] = x[1] + 20
#     print(x)
#
# a = [10,20,30,4]
# print(a)
# print(id(a))
# change(a)
# print(id(a))
# print(a)
# --------------------------------------------------------------------------------------------------------------------
# from random import *
# from abc import *
# class Account(ABC):
#     def accno(self):
#         print("Your account numbers is:")
#         for i in range(12):
#             print(randint(0, 9), end="")
#
#     def __init__(self, name, balance, min_bal):
#         self.Name = name
#         self.Balance = balance
#         self.Minimum = min_bal
#
#     def deposit(self, amount):
#         self.Balance += amount
#         self.ministatement()
#
#
#     def withdraw(self, amount):
#         if self.Balance - amount >= self.Minimum:
#             self.Balance -= amount
#             self.ministatement()
#
#         else:
#             print("Un sufficient amount")
#     @abstractmethod
#     def ministatement(self): pass
#
#     @abstractmethod
#     def wish(self): pass
#
# class Current(Account):
#     def __init__(self, name, balance, min_bal):
#         super().__init__(name, balance, min_bal)
#         self.Minimum = min_bal
#
#
#     def ministatement(self):
#         user_id = int(input())
#         password = input()
#         if user_id == 12345 and password == "ICICI@123":
#             print(f"Your current account balance is {self.Balance}")
#         else:
#             print("Please provide valid credentials")
#
#     def __str__(self):
#         return f"{self.Name} account balance is {self.Balance}"
#
#     def wish(self):
#         print(f"Hello my name is {self.Name}")
#
#
# class Saving(Current):
#     def __init__(self, name, balance, min_bal):
#         super().__init__(name, balance, min_bal)
#         self.Minimum = min_bal
# #
#
# s = Saving("Dgs", 5000,-1000)
# s1 = Saving("Dgs", 5000, 0)
# s.withdraw(6000)
# s1.withdraw(6000)
# s.ministatement()
# s1.ministatement()













