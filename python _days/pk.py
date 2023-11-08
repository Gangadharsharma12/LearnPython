# ex:1
# import pickle
# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.eaddr = eaddr
#
#     def display(self):
#         print(f"ENO: {self.eno}, ENAME: {self.ename}, ESAL: {self.esal}, EADDR: {self.eaddr}")
#
#
# e = Employee(100, "Durga", 1000, "Hyderabad")
#
# # We want to save this object to a file and we want to read that object from the file:
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.ser", "wb") as fp:
#     pickle.dump(e, fp)
#     print("object serlization completed")
#
#
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.ser", "rb") as f:
#     obj = pickle.load(f)
#     print("object deserlization completed")
#     print("printing employee information")
#     obj.display()
# This data is comming from emp.sar file
# -----------------------------------------------------------------------------------------------------------------------------
# ex:2

import pickle,sys
with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.data", "ab") as fp:
	while(True):
		print("-"*50)
		#read emp values from key board
		eno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		sal=float(input("Enter Emp Salary:"))
		#place emp values in Iterable Object--list
		l1=list() #empty list
		l1.append(eno)
		l1.append(ename)
		l1.append(sal)
		#Save list object data into file
		pickle.dump(l1,fp)
		print("-"*50)
		print("\tEmplyee Record Saved Successfully in File:")
		print("-"*50)
		ch=input("Do u want to insert another record(yes/no):")
		if(ch.lower()=="no"):
			print("Thx for  using  this program")
			sys.exit()


