from emp import *
import pickle
with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\dgs.ser", "wb") as f:
    while True:
        eno = int(input("Enter Employee Number:"))
        ename = input("Enter Employee name:")
        esal = float(input("Enter Employee Salary:"))
        eaddress = input("Enter Employee address:")
        e = Employee(eno, ename, esal, eaddress)
        pickle.dump(e, f)
        print("Employee object saved to file")
        option = input("Do you want to serialize one more employee object[yes|No]")
        if option.lower() == "no":
            break
    print("All Employee objects serialized")

