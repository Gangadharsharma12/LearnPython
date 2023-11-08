# 51
# def sunday():
#     final()
#
# def monday():
#     final()
#
# def tuesday():
#     final()
#
# def wednesday():
#     final()
#
# def thursday():
#     final()
#
# def friday():
#     final()
#
# def saturday():
#     final()
#
# def final():
#     print(f"the temperature for {days} is {daily_temp[count]}")
#
# count = 0
# daily_temp = [68.7, 68.8, 67.4, 69.9, 70, 71.2, 72]
# days = input("please select any day from SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY")
# if days.lower() == "sunday":
#     sunday()
#
# elif days.lower() == "monday":
#     count += 1
#     monday()
#
# elif days.lower() == "tuesday":
#     count += 2
#     tuesday()
#
# elif days.lower() == "wednesday":
#     count += 3
#     wednesday()
#
# elif days.lower() == "thursday":
#     count += 4
#     thursday()
#
# elif days.lower() == "friday":
#     count += 5
#     friday()
#
# elif days.lower() == "saturday":
#     count += 6
#     saturday()
#
# else:
#     print("invalid input")
# ----------------------------------------------------------------------------------------------------------------------

# WAP TO FIND THE GIVEN WORDS ARE ANAGRAM OR NOT

# s1 = "EARTH".lower()
# s2 = "HEART".lower()
# s3 = sorted(s1)
# s4 = sorted(s2)
# flag = True
# if len(s3) == len(s4):
#     for i in range(len(s3)):
#         if s3[i] == s4[i]:
#             flag = True
#         else:
#             flag = False
#     print(flag)
#
#     if flag == True:
#         print("Anagram")
#     else:
#         print("Not anagram")
# else:
#     print("Not an anagram")
#     flag = False
#     print(flag)
# ----------------------------------------------------------------------------------------------------------------------

# WAP TO PRINT FACTORIAL OF A GIVEN NUMBER CONTINUOUSLY
# import time
# n = 1
# fact = 1
# i = 1
# while n > 0:
#     fact = fact * i
#     print(f"The factorial of {n} is {fact}")
#     n += 1
#     i += 1
#     time.sleep(1.0)
# ---------------------------------------------------------------------------------------------------------------------

# WAP TO PRINT THE FACTORIAL OF NUMBERS TO THE GIVEN RANGE

# import time
# n = int(input("Enter the number:"))
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     print(f"The factorial of {i} is {fact}")
#     i += 1
#     time.sleep(1.0)
# ---------------------------------------------------------------------------------------------------------------------

# WAP TO FIND THE PRIME NUMBERS TO THE GIVEN RANGE:

# n = int(input("Enter the number:"))
# for i in range(n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             print(f"{i} is not a prime number")
#             break
#     else:
#             print(f"{i} is a prime number")


# count = int(input("enter the count:"))
# l = []
# for i in range(2, count+1):
#     if i >= count:
#         break
#     else:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
# print(l)

# ---------------------------------------------------------------------------------------------------------------------

# WAP TO PRINT THE GIVEN NUMBER IS PRIME OR NOT:
# n = int(input("Enter any number:"))
# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is a prime number")
# --------------------------------------------------------------------------------------------------------------------

# l12 = (1, 2, 1, 4, 1, 2, 4, 3, 2, 2)
# d = {}
# for each in l12:
#     d[each] = l12.count(each)
# l = list(d.values())
# l1 = list(d.keys())
# l2 = [k for k, v in d.items() if v == max(l1)]
# print(f"The maximum repeated number in {l12} is {str(l2)} and it repeated {max(l)} times")


# n = int(input())
# n1 = n
# t = 0
# while n > 0:
#     r = n % 10
#     t = t + r ** len(str(n1))
#     n = n // 10
# if n1 == t:
#     print("armstrong")
# else:
#     print("not armstrong")


# WAP TO FIND THE GIVEN WORDS ARE ANAGRAM OR NOT

# s1 = "EARTH".lower()
# s2 = "HEART".lower()
# s3 = sorted(s1)
# s4 = sorted(s2)
# flag = True
# if len(s3) == len(s4):
#     for i in range(len(s3)):
#         if s3[i] == s4[i]:
#             flag = True
#         else:
#             flag = False
#     print(flag)
#
#     if flag == True:
#         print("Anagram")
#     else:
#         print("Not anagram")
# else:
#     print("Not an anagram")
#     flag = False
#     print(flag)

# --------------------------------------------------------------------------------------------------------------------


# a = 3
# b = 4
# print(a, b)
# a = a // b
# b = a ^ b
# a = a ^ b
# print(a, b)
# ---------------------------------------------------------------------------------------------------------------------
# LCM:
# a = int(input())
# b = int(input())
# c = max(a, b)
# while c <= a * b:
#     if c % a == 0 and c % b == 0:
#         break
#     else:
#         c += 1
# print(c)

# GCD:

# a = int(input())
# b = int(input())
# c = min(a, b)
# for i in range(1, c+1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print(gcd)

# def solve(a, b):
#    return b if a == 0 else solve(b % a, a)
# print(solve(20, 50))


# import time
# a = 2
# b = 1
# while True:
#     c = max(a, b)
#     if c <= a * b:
#         if c % a == 0 and c % b == 0:
#             print(f"the lcm of {a} and {b} is {c}")
#         else:
#             print(f"the lcm of {a} and {b} is {a * b}")
#         b += 1
#         time.sleep(1)

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



class Test:
    def __init__(self, ename, eaddress, esal):
        self.ename = ename
        self.eaddress = eaddress
        self.esal = esal

    def show(self):
        print(self.ename)
        print(self.eaddress)
        print(self.esal)

class Demo:
    def __init__(self, state, pincode):
        self.state = state
        self.pincode = pincode
    def m1(x):
        t.show()


class Employee:
    def m2(y):
        print(y.state)
        print(y.pincode)


t = Test("dgs", "medak", 40000)
d = Demo("ts", 502110)
Demo.m1(t)
Employee.m2(d)
