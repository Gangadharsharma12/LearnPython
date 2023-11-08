# # program for serializing multiple employee objects to a file
# # In the above code we wrote all the operations at same place
# # Now we are creating 3 different python files.First file is used to create objects
# # sender.py is responsible to create and save employee objects to a file(from emp.py import *)
# # Receiver.py is responsible to de seralize all employee objects(that is reading)
# # class Employee:
# #     def __init__(self, eno, ename, esal, eaddr):
# #         self.eno = eno
# #         self.ename = ename
# #         self.esal = esal
# #         self.eaddr = eaddr
# #
# #     def display(self):
# #         print(f"ENO: {self.eno}, ENAME: {self.ename}, ESAL: {self.esal}, EADDR: {self.eaddr}")
#------------------------------------------------------------------------------------------------------------------------------

# 153

import json
employee = {"name": "gangadhar", "age": 25, "salary": 10000.0, "ismarried": False, "having gf": None}
# serialization from python object to json_string.
json_string = json.dumps(employee, indent=4, sort_keys=True)
print(json_string)
# serialization from python dict object to json and write that json to a file
with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\emp.json", "w") as fp:
    json.dump(employee, fp, indent=4)

emp_dict = json.loads(json_string)
print(emp_dict.get("ismarried"))

