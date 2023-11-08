#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx1.py----Instance Data members
# class Student:pass
#
# #main program
# s1=Student()
# s2=Student()
# print("Content of s1 before adding the data={} and Number of values={}".format(s1.__dict__, len(s1.__dict__)))
# print("Content of s2 before adding the data={} and Number of values={}".format(s2.__dict__, len(s2.__dict__)))
# print("-"*50)
# #add Instance Data Members to s1
# s1.sno=10
# s1.name="RS"
# s1.marks=22.22
# print("Content of s1 after adding the data={} and Number of values={}".format(s1.__dict__, len(s1.__dict__)))
# #add Instance Data Members to s2
# s2.stno=20
# s2.sname="TR"
# s2.smarks=42.22
# print("Content of s2 after adding the data={} and Number of values={}".format(s2.__dict__, len(s2.__dict__)))
#
# # OUTPUT:
#
# Content of s1 before adding the data={} and Number of values=0
# Content of s2 before adding the data={} and Number of values=0
# --------------------------------------------------
# Content of s1 after adding the data={'sno': 10, 'name': 'RS', 'marks': 22.22} and Number of values=3
# Content of s2 after adding the data={'stno': 20, 'sname': 'TR', 'smarks': 42.22} and Number of values=3

# ------------------------------------------------------------------------------------------------------------------------------
#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx2.py----Instance Data members and Class Level Data Members
# class Student:
# 	crs="PYTHON" # here crs is called Class Level Data member
#
#
# #main program
# s1=Student()
# s2=Student()
# print("Content of s1 before adding=",s1.__dict__)
# print("Content of s2 before adding=",s2.__dict__)
# #Read Instance Data members such as sno,sname and marks to s1
# print("-"*50)
# print("First Student Information")
# print("-"*50)
# s1.sno=int(input("Enter Student Number:"))
# s1.sname=input("Enter Student Name:")
# s1.marks=float(input("Enter Student Marks:"))
# print("-"*50)
# print("Second Student Information")
# print("-"*50)
# s2.sno=int(input("Enter Student Number:"))
# s2.sname=input("Enter Student Name:")
# s2.marks=float(input("Enter Student Marks:"))
# print("-"*50)
# print("\nContent of s1 after adding=",s1.__dict__)
# print("Content of s2 after adding=",s2.__dict__)

# OUTPUT:

# Content of s1 before adding= {}
# Content of s2 before adding= {}
# --------------------------------------------------
# First Student Information
# --------------------------------------------------
# Enter Student Number:101
# Enter Student Name:DGS
# Enter Student Marks:100
# --------------------------------------------------
# Second Student Information
# --------------------------------------------------
# Enter Student Number:200
# Enter Student Name:KVR
# Enter Student Marks:90
# --------------------------------------------------
#
# Content of s1 after adding= {'sno': 101, 'sname': 'DGS', 'marks': 100.0}
# Content of s2 after adding= {'sno': 200, 'sname': 'KVR', 'marks': 90.0}

# ------------------------------------------------------------------------------------------------------------------------------


#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx3.py----Instance Data members and Class Level Data Members
# class Student:
# 	crs="PYTHON" # here crs is called Class Level Data member
#
# #main program
# s1=Student()
# s2=Student()
# print("Content of s1 before adding=",s1.__dict__)
# print("Content of s2 before adding=",s2.__dict__)
# #Read Instance Data members such as sno,sname and marks to s1
# print("-"*50)
# print("First Student Information")
# print("-"*50)
# s1.sno=int(input("Enter Student Number:"))
# s1.sname=input("Enter Student Name:")
# s1.marks=float(input("Enter Student Marks:"))
# print("-"*50)
# print("Second Student Information")
# print("-"*50)
# s2.sno=int(input("Enter Student Number:"))
# s2.sname=input("Enter Student Name:")
# s2.marks=float(input("Enter Student Marks:"))
#
# print("-"*50)
# print("First Student Information:")
# print("-"*50)
# print("\tStudent Number:{}".format(s1.sno))
# print("\tStudent Name:{}".format(s1.sname))
# print("\tStudent Marks:{}".format(s1.marks))
# print("\tStudent Course:{}".format(Student.crs))# accessing Class Level Data member w.r.t Class Name
# print("-"*50)
# print("Second Student Information:")
# print("-"*50)
# print("\tStudent Number:{}".format(s2.sno))
# print("\tStudent Name:{}".format(s2.sname))
# print("\tStudent Marks:{}".format(s2.marks))
# print("\tStudent Course:{}".format(Student.crs))## accessing Class Level Data member w.r.t Class Name
# print("-"*50)

# OUTPUT:

# Content of s1 before adding= {}
# Content of s2 before adding= {}
# --------------------------------------------------
# First Student Information
# --------------------------------------------------
# Enter Student Number:100
# Enter Student Name:DGS
# Enter Student Marks:56
# --------------------------------------------------
# Second Student Information
# --------------------------------------------------
# Enter Student Number:500
# Enter Student Name:KVR
# Enter Student Marks:53
# --------------------------------------------------
# First Student Information:
# --------------------------------------------------
# 	Student Number:100
# 	Student Name:DGS
# 	Student Marks:56.0
# 	Student Course:PYTHON
# --------------------------------------------------
# Second Student Information:
# --------------------------------------------------
# 	Student Number:500
# 	Student Name:KVR
# 	Student Marks:53.0
# 	Student Course:PYTHON
# --------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------
#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx4.py----Instance Data members and Class Level Data Members

# class Student:
# 	crs="PYTHON" # here crs is called Class Level Data member
#
# #main program
# s1=Student()
# s2=Student()
# print("Content of s1 before adding=",s1.__dict__)
# print("Content of s2 before adding=",s2.__dict__)
# #Read Instance Data members such as sno,sname and marks to s1
# print("-"*50)
# print("First Student Information")
# print("-"*50)
# s1.sno=int(input("Enter Student Number:"))
# s1.sname=input("Enter Student Name:")
# s1.marks=float(input("Enter Student Marks:"))
# print("-"*50)
# print("Second Student Information")
# print("-"*50)
# s2.sno=int(input("Enter Student Number:"))
# s2.sname=input("Enter Student Name:")
# s2.marks=float(input("Enter Student Marks:"))
#
# print("-"*50)
# print("First Student Information:")
# print("-"*50)
# print("\tStudent Number:{}".format(s1.sno))
# print("\tStudent Name:{}".format(s1.sname))
# print("\tStudent Marks:{}".format(s1.marks))
# print("\tStudent Course:{}".format(s1.crs)) # accessing Class Level Data member w.r.t object Name
# print("-"*50)
# print("Second Student Information:")
# print("-"*50)
# print("\tStudent Number:{}".format(s2.sno))
# print("\tStudent Name:{}".format(s2.sname))
# print("\tStudent Marks:{}".format(s2.marks))
# print("\tStudent Course:{}".format(s2.crs))# accessing Class Level Data member w.r.t object Name
# print("-"*50)
#
#
# OUTPUT:
# Content of s1 before adding= {}
# Content of s2 before adding= {}
# --------------------------------------------------
# First Student Information
# --------------------------------------------------
# Enter Student Number:100
# Enter Student Name:DGS
# Enter Student Marks:98
# --------------------------------------------------
# Second Student Information
# --------------------------------------------------
# Enter Student Number:700
# Enter Student Name:KVR
# Enter Student Marks:90
# --------------------------------------------------
# First Student Information:
# --------------------------------------------------
# 	Student Number:100
# 	Student Name:DGS
# 	Student Marks:98.0
# 	Student Course:PYTHON
# --------------------------------------------------
# Second Student Information:
# --------------------------------------------------
# 	Student Number:700
# 	Student Name:KVR
# 	Student Marks:90.0
# 	Student Course:PYTHON
# --------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------

#Program for Reading sno,sname ,marks in an object of Programmer-defined class w.r.t Instance Methods
#InstanceMethodEx1.py
# class Student:
# 	def getstuddata(self):
# 		print("-"*40)
# 		self.sno=int(input("Enter Student Number:"))
# 		self.sname=input("Enter Student Name:")
# 		self.marks=float(input("Enter Student Marks:"))
# 		print("-"*40)
# 	def dispstuddata(hyd):
# 		print("-"*40)
# 		print("\tStudent Number:{}".format(hyd.sno))
# 		print("\tStudent Name:{}".format(hyd.sname))
# 		print("\tStudent Marks:{}".format(hyd.marks))
# 		print("-"*40)
#
#
# #main program
# s1=Student()
# s2=Student()
# print("Content of s1 before reading=",s1.__dict__)
# print("Content of s2 before reading=",s2.__dict__)
# print("-"*50)
# print("Enter First Student Information:")
# s1.getstuddata()
# print("Enter Second Student Information:")
# s2.getstuddata()
# print("Details of First Student:")
# s1.dispstuddata()
# print("Details of Second Student:")
# s2.dispstuddata()
#
# # OUTPUT
#
# Content of s1 before reading= {}
# Content of s2 before reading= {}
# --------------------------------------------------
# Enter First Student Information:
# ----------------------------------------
# Enter Student Number:100
# Enter Student Name:DGS
# Enter Student Marks:39
# ----------------------------------------
# Enter Second Student Information:
# ----------------------------------------
# Enter Student Number:899
# Enter Student Name:KVR
# Enter Student Marks:66
# ----------------------------------------
# Details of First Student:
# ----------------------------------------
# 	Student Number:100
# 	Student Name:DGS
# 	Student Marks:39.0
# ----------------------------------------
# Details of Second Student:
# ----------------------------------------
# 	Student Number:899
# 	Student Name:KVR
# 	Student Marks:66.0
# ----------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------

# Program for Reading sno,sname ,marks in an object of Programmer-defined class w.r.t Instance Methods
# InstanceMethodEx2.py
# class Student:
#     crs = "PYTHON"  # Class Level Data Member
#
#     def getstuddata(self):
#         print("-" * 40)
#         self.sno = int(input("Enter Student Number:"))
#         self.sname = input("Enter Student Name:")
#         self.marks = float(input("Enter Student Marks:"))
#         print("-" * 40)
#         self.dispstuddata()  # calling Instance method from another instance method
#
#     def dispstuddata(self):
#         print("-" * 40)
#         print("\tStudent Number:{}".format(self.sno))
#         print("\tStudent Name:{}".format(self.sname))
#         print("\tStudent Marks:{}".format(self.marks))
#         print("\tStudent Course name:{}".format(self.crs))
#         print("-" * 40)
#
#
# # main program
# s1 = Student()
# s2 = Student()
# print("Content of s1 before reading=", s1.__dict__)
# print("Content of s2 before reading=", s2.__dict__)
# print("-" * 50)
# print("Enter First Student Information:")
# s1.getstuddata()
# print("Enter Second Student Information:")
# s2.getstuddata()
#
# OUTPUT:
# Content of s1 before reading= {}
# Content of s2 before reading= {}
# --------------------------------------------------
# Enter First Student Information:
# ----------------------------------------
# Enter Student Number:100
# Enter Student Name:DGS
# Enter Student Marks:44
# ----------------------------------------
# ----------------------------------------
# 	Student Number:100
# 	Student Name:DGS
# 	Student Marks:44.0
# 	Student Course name:PYTHON
# ----------------------------------------
# Enter Second Student Information:
# ----------------------------------------
# Enter Student Number:000
# Enter Student Name:KVR
# Enter Student Marks:55
# ----------------------------------------
# ----------------------------------------
# 	Student Number:0
# 	Student Name:KVR
# 	Student Marks:55.0
# 	Student Course name:PYTHON
# ----------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------

# Program for demonstrating Class Level Methods and Class Level Data members
# ClassLevelMethodEx1.py
# class Student:
#     @classmethod
#     def getcourse(cls):
#         cls.crs = "PYTHON"
#
#     @classmethod
#     def getDeveloper(cls):
#         Student.dev = "Rossum"
#
#
# # main program
# Student.getcourse()  # calling Class Level method w.r.t class name
# Student.getDeveloper()  # calling Class Level method .w.r.t classname
# s1 = Student()
# s2 = Student()
# print(s1.crs, s1.dev)
# print(s2.crs, s2.dev)
#
# # OUTPUT
#
# PYTHON Rossum
# PYTHON Rossum

# -----------------------------------------------------------------------------------------------------------------------------

# Program for demonstrating Class Level Methods and Class Level Data members
# ClassLevelMethodEx2.py
# class Student:
#     @classmethod
#     def getcourse(cls):
#         cls.crs = "PYTHON"
#
#     @classmethod
#     def getDeveloper(cls):
#         Student.dev = "Rossum"
#
#
# # main program
# s1 = Student()
# s2 = Student()
# s1.getcourse()  # calling Class Level method w.r.t object name
# s2.getDeveloper()  # calling Class Level method w.r.t object name
#
# print(s1.crs, s1.dev)
# print(s2.crs, s2.dev)
#
# OUTPUT:
#
# PYTHON Rossum
# PYTHON Rossum

# ------------------------------------------------------------------------------------------------------------------------------

# Program for demonstrating Class Level Methods and Class Level Data members
# ClassLevelMethodEx3.py
# class Student:
#     @classmethod
#     def getcourse(cls):
#         cls.crs = "PYTHON"
#         cls.getDeveloper()  # Calling Class Level Method w.r.t cls
#
#     @classmethod
#     def getDeveloper(cls):
#         Student.dev = "Rossum"
#
#
# # main program
# Student.getcourse()  # Calling Class Level Method w.r.t Class Name
# s1 = Student()
# s2 = Student()
#
# print(s1.crs, s1.dev)
# print(s2.crs, s2.dev)

# OUTPUT
# PYTHON Rossum
# PYTHON Rossum

# ------------------------------------------------------------------------------------------------------------------------------

# Program for demonstrating Class Level Methods and Class Level Data members
# ClassLevelMethodEx4.py
# class Student:
#     @classmethod
#     def getcourse(cls):
#         cls.crs = "PYTHON"
#         cls.getDeveloper("ROSSUM")  # Calling Class Level Method w.r.t cls
#
#     @classmethod
#     def getDeveloper(cls, dname):
#         Student.dev = dname
#
#     def getstudentdet(self, sno, sname, marks):
#         self.sno = sno
#         self.sname = sname
#         self.marks = marks
#
#     def dispstuddata(self):
#         self.getcourse()  # calling Class Level Method Name w.r.t self
#         print("-" * 40)
#         print("\tStudent Number:{}".format(self.sno))
#         print("\tStudent Name:{}".format(self.sname))
#         print("\tStudent Marks:{}".format(self.marks))
#         print("\tStudent Courrse Name:{}".format(self.crs))
#         print("\tCourrse Dev By:{}".format(self.dev))
#         print("-" * 40)
#
#
# # main program
# s1 = Student()
# s2 = Student()
# s1.getstudentdet(10, "RS", 11.11)
# s2.getstudentdet(20, "TR", 21.11)
# s1.dispstuddata()
# s2.dispstuddata()
# OUTPUT:
# ----------------------------------------
# 	Student Number:10
# 	Student Name:RS
# 	Student Marks:11.11
# 	Student Courrse Name:PYTHON
# 	Courrse Dev By:ROSSUM
# ----------------------------------------
# ----------------------------------------
# 	Student Number:20
# 	Student Name:TR
# 	Student Marks:21.11
# 	Student Courrse Name:PYTHON
# 	Courrse Dev By:ROSSUM
# ----------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

#StaticMethodEx1.py
# class Student:
# 	def  getstuddet(self):
# 		self.sno=int(input("\nEnter Student Number:"))
# 		self.sname=input("Enter Student Name:")
#
# class Employee:
# 	def  getempdet(self):
# 		self.eno=int(input("\nEnter Employee Number:"))
# 		self.ename=input("Enter Employee Name:")
# 		self.sal=input("Enter Employee Salary:")
#
# class Teacher:
# 	def getteacherdet(self):
# 		self.tno=int(input("\nEnter Teacher Number:"))
# 		self.ename=input("Enter Teacher Name:")
# 		self.subject=input("Enter Teacher Subject:")
#
# class Hyd:
# 	@staticmethod
# 	def  dispobjectdata(kvr,pinfo):
# 		print("-"*50)
# 		print("Information about:{}".format(pinfo))
# 		for k,v in kvr.__dict__.items():
# 			print("\t{}   {}".format(k,v))
# 		print("-"*50)
#
#
# #main program
# s=Student()
# e=Employee()
# t=Teacher()
# s.getstuddet()
# e.getempdet()
# t.getteacherdet()
# #calling Static Method w..r.t Class Name
# Hyd.dispobjectdata(s, "Student")
# Hyd.dispobjectdata(e, "Employee")
# Hyd.dispobjectdata(t, "Teacher")

# output:

# Enter Student Number:100
# Enter Student Name:ravi
#
# Enter Employee Number:200
# Enter Employee Name:raju
# Enter Employee Salary:30000
#
# Enter Teacher Number:300
# Enter Teacher Name:usha
# Enter Teacher Subject:python
# --------------------------------------------------
# Information about:Student
# 	sno   100
# 	sname   ravi
# --------------------------------------------------
# --------------------------------------------------
# Information about:Employee
# 	eno   200
# 	ename   raju
# 	sal   30000
# --------------------------------------------------
# --------------------------------------------------
# Information about:Teacher
# 	tno   300
# 	ename   usha
# 	subject   python
# --------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------

#StaticMethodEx2.py
# class Student:
# 	def  getstuddet(self):
# 		self.sno=int(input("Enter Student Number:"))
# 		self.sname=input("Enter Student Name:")
#
# class Employee:
# 	def  getempdet(self):
# 		self.eno=int(input("\nEnter Employee Number:"))
# 		self.ename=input("Enter Employee Name:")
# 		self.sal=input("Enter Employee Salary:")
#
# class Teacher:
# 	def getteacherdet(self):
# 		self.tno=int(input("\nEnter Teacher Number:"))
# 		self.ename=input("Enter Teacher Name:")
# 		self.subject=input("Enter Teacher Subject:")
#
# class Hyd:
# 	@staticmethod
# 	def  dispobjectdata(kvr,pinfo):
# 		print("-"*50)
# 		print("Information about:{}".format(pinfo))
# 		for k,v in kvr.__dict__.items():
# 			print("\t{}   {}".format(k,v))
# 		print("-"*50)
#
#
# #main program
# s=Student()
# e=Employee()
# t=Teacher()
# s.getstuddet()
# e.getempdet()
# t.getteacherdet()
# #calling Static Method w..r.t Object Name
# H=Hyd()
# H.dispobjectdata(s,"Student")
# H.dispobjectdata(e,"Employee")
# H.dispobjectdata(t,"Teacher")


# output:

# Enter Student Number:100
# Enter Student Name:ravi
#
# Enter Employee Number:200
# Enter Employee Name:raju
# Enter Employee Salary:30000
#
# Enter Teacher Number:300
# Enter Teacher Name:usha
# Enter Teacher Subject:python
# --------------------------------------------------
# Information about:Student
# 	sno   100
# 	sname   ravi
# --------------------------------------------------
# --------------------------------------------------
# Information about:Employee
# 	eno   200
# 	ename   raju
# 	sal   30000
# --------------------------------------------------
# --------------------------------------------------
# Information about:Teacher
# 	tno   300
# 	ename   usha
# 	subject   python
# --------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------

#StaticMethodEx3.py
# class Student:
# 	def  getstuddet(self):
# 		self.sno=int(input("\nEnter Student Number:"))
# 		self.sname=input("Enter Student Name:")
# 		self.dispobjectdata(self,"Student") # Calling Static Method w.r.t self
# 	@staticmethod
# 	def  dispobjectdata(kvr,pinfo):
# 		print("-"*50)
# 		print("Information about:{}".format(pinfo))
# 		for k,v in kvr.__dict__.items():
# 			print("\t{}   {}".format(k,v))
# 		print("-"*50)
# class Employee:
# 	def  getempdet(self):
# 		self.eno=int(input("\nEnter Employee Number:"))
# 		self.ename=input("Enter Employee Name:")
# 		self.sal=input("Enter Employee Salary:")
# 		Student.dispobjectdata(self,"Employee") #Calling Static Method w.r.t class name
# class Teacher:
# 	def getteacherdet(self):
# 		self.tno=int(input("\nEnter Teacher Number:"))
# 		self.ename=input("Enter Teacher Name:")
# 		self.subject=input("Enter Teacher Subject:")
# 		Student.dispobjectdata(self,"Teacher") #Calling Static Method w.r.t class name
# #main program
# s=Student()
# e=Employee()
# t=Teacher()
# s.getstuddet()
# e.getempdet()
# t.getteacherdet()

# OUTPUT:

# Enter Student Number:100
# Enter Student Name:RAVI
# --------------------------------------------------
# Information about:Student
# 	sno   100
# 	sname   RAVI
# --------------------------------------------------
#
# Enter Employee Number:200
# Enter Employee Name:RAJU
# Enter Employee Salary:30000
# --------------------------------------------------
# Information about:Employee
# 	eno   200
# 	ename   RAJU
# 	sal   30000
# --------------------------------------------------
#
# Enter Teacher Number:300
# Enter Teacher Name:KIRAN
# Enter Teacher Subject:PYTHON
# --------------------------------------------------
# Information about:Teacher
# 	tno   300
# 	ename   KIRAN
# 	subject   PYTHON
# --------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------


"""write a python program which will accept student details such as student number student name,marks in three subjects.
calculate the total marks
calculate the Percentage and give the grades.(fail/pass)

give the grade = #fail provided student secured less than 40 in any of the three subjects.
give the grade = #distinction provided student totall marks lies within 250 - 300
give the grade = #First class provided totall marks lies within 200- 249
give the grade= second class provided totall marks lies within 150- 199
give the grade= third class provided totall marks lies within 120- 149
save the students result in the database."""
# StudentOOPsDataBaseMySQL.py
# import mysql.connector
#
#
# class Student:
#     def getstuddet(self):
#         self.sno = int(input("Enter Student Number:"))
#         self.sname = input("Enter Student Name:")
#         # validation of C Marks
#         while (True):
#             self.cm = int(input("Enter Marks in C(100):"))
#             if (self.cm >= 0) and (self.cm <= 100):
#                 break
#         # validation of C++ Marks
#         while (True):
#             self.cppm = int(input("Enter Marks in C++(100):"))
#             if (self.cppm >= 0) and (self.cppm <= 100):
#                 break
#         # validation of Python Marks
#         while (True):
#             self.pym = int(input("Enter Marks in PYTHON(100):"))
#             if (self.pym >= 0) and (self.pym <= 100):
#                 break
#
#     def compute(self):
#         self.totmarks = self.cm + self.cppm + self.pym
#         self.percent = (self.totmarks / 300) * 100
#         # decide Grade
#         if (self.cm < 40) or (self.cppm < 40) or (self.pym < 40):
#             self.grade = "FAIL"
#         else:
#             if (self.totmarks >= 250) and (self.totmarks <= 300):
#                 self.grade = "DISTINCTION"
#             elif (self.totmarks >= 200) and (self.totmarks <= 249):
#                 self.grade = "FIRST"
#
#             elif (self.totmarks >= 150) and (self.totmarks <= 199):
#                 self.grade = "SECOND"
#             elif (self.totmarks >= 120) and (self.totmarks <= 149):
#                 self.grade = "THIRD"
#
#     def savestuddata(self):
#         # We must write PDBC Code
#         try:
#             con = mysql.connector.connect(host="localhost",
#                                           user="root",
#                                           passwd="root",
#                                           database="batch11am")
#             cur = con.cursor()
#             cur.execute("insert into result values(%d,'%s',%d,%d,%d,%d,%f,'%s')" % (
#             self.sno, self.sname, self.cm, self.cppm, self.pym, self.totmarks, self.percent, self.grade))
#             con.commit()
#             print("Student Record Saved Successfully in Result Table:")
#         except mysql.connector.DatabaseError as db:
#             print("Prob in DB", db)
#
#
# # main program
# s = Student()
# s.getstuddet()
# s.compute()
# s.savestuddata()
# ------------------------------------------------------------------------------------------------------------------------------




