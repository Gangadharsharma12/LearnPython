# print("\"I'm\"")
# print("\"\"learning\"\"")
# print("\"\"\"python\"\"\"")


# print(9 % 6 % 2)
# print(2 ** 3 ** 2)
# print(2 * 3 % 5)
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# print((560/ 26) // 2)


# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# sheep_count = int(input("enter any number:"))
#
#
# def make_bed():
#     print("i am very tired")
#     print("please arrange a bad for me")
#     print()
#
#
# def take_a_shower():
#     print("I am very tired")
#     print("i will go for a bath")
#     print()
#
#
# def sleep_and_dream():
#     print("i am very tired")
#     print("i love sleeping and dreaming")
#     print()
#
# def feed_sheep_dogs():
#     print("please feed the sheeps and dogs")
#
# if sheep_count >= 120:
#     make_bed()
#     take_a_shower()
#     sleep_and_dream()



# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)



# s = input()
# if s == "spathiphyllum".upper():
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif s == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {s}!")



# If tax is less than or equal to 85,528 tax is 18% of income - 556.02.
# If tax is more than 85,528, tax is 14,839.02 plus 32% of surplus above     85,528.

# income = float(input("Enter the annual income: "))
# if income <= 85228:
#     tax = (18/100) * income - 556.02
#     if tax < 0:
#         print("The tax is: 0.0 thalers")
#     else:
#         print(round(tax, 0))
# elif income > 85228:
#     tax = 14839.02 + (32/100 * (income-85228))
#     print(round(tax,0))



# year = int(input("enter the year number:"))
# if year <= 1580:
#     print("Not within the Gregorian calendar period")
# else:
#     if year % 100 == 0 and year % 400 == 0:
#         print("leap year")
#     elif year % 4 == 0 and year % 100 != 0:
#         print("leap year")
#     else:
#         print("common year")


# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# while True:
#     n = int(input("enter the user number:"))
#     if n == secret_number:
#         print("Well done, muggle! You are free now.")
#         break
#     else:
#         continue


# blocks = int(input("Enter the blocks : "))
# height = 0
# layers = 1
# while layers <= blocks:
#     height += 1
#     blocks -= layers
#     layers += 1
# print("The height of the pyramid: ", height)



# c0 = int(input())
# c = 0
# while True:
#     if c0 == 1:
#         break
#     elif c0 % 2 == 0:
#         c0 = c0 // 2
#         print(c0)
#         c += 1
#     else:
#         c0 = 3*c0 +1
#         print(c0)
#         c += 1
# print("steps =", c)



# s = input()
# s1 = ""
# for each in s:
#     if each == "0":
#         s1 += "x"
#     else:
#         s1 += each
# print(s1)


# l = [3, 7, 11, 42, 34, 49]
# h = [5, 11, 9, 42, 3, 49]
# c = 0
# for each in l:
#     if each in h:
#         c += 1
# print(c)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# l1 = ["even" if each % 2 == 0  else "odd"  for each in l]
# print(l1)

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1


# for i in range(1):
#     print("$")
# else:
#     print("$")



# num = [10, 1, 2,3]
# val = num[-3:-1:1]
# print(val)


# l = [[0, 1, 2, 3] for i in range(2)]
# print(l[2][0])

# def message(place, name = "dgs"):
#     print("hello", name)
#     print("i am from", place)
#
# x = input("enter your name:")
# y = input("enter your place:")
# message(y, x)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")


# def sum_list(*l):
#     s = 0
#     for each in l:
#         s += each
#     return s
# print(sum_list(10, 20, 30))
# print(sum_list(10))


# def is_year_leap(year):
#     for each in year:
#         if each % 4 == 0 and each % 100 != 0:
#             print("leap year")
#         elif each % 100 == 0 and each % 400 == 0:
#             print("leap year")
#         else:
#             print("normal year")
# is_year_leap([1900, 2000, 2016, 1987])


# n = int(input())
# def is_prime(n):
#     for i in range(2, n):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# is_prime(n)



# c = int(input())
# def fib_ser(n):
#     if n < 1:
#         return 1
#     if n < 3:
#         return 1
#     e1 = e2 = 1
#     s = 0
#     for i in range(3, n+1):
#         s = e1 + e2
#         e1, e2 = e2, s
#     return s
# for i in range(1, c+1):
#     print(i, "------->", fib_ser(i))

# n = int(input())
# n1 = int(input())
# l = []
# l1 = []
# l2 = []
# for i in range(1, n+1):
#     if n % i == 0:
#         l.append(i)
# for i in range(1, n1+1):
#     if n1 % i == 0:
#         l1.append(i)
# for each in l:
#     if each in l1:
#         l2.append(each)
# print(l2[-1])


# x = 50
# def func():
#     print(x)
#     y = 100
#     def inner():
#         nonlocal y
#         y += 600
#         print(y)
#         z = 200
#         def inner1():
#             nonlocal y
#             y += 600
#             print(y)
#         inner1()
#         print(z)
#     inner()
# func()

# a = 10
# b = 20
# c = 30
# d = 40
# def func():
#     a = 100
#     b = 200
#     c = 300
#     d = 400
#     res = a + b + c + d + globals()['a'] + globals()["b"] + globals().get("c") + globals().get("d")
#     return res
# print(func())


# def ft_and_inch_to_m(ft, inch=0.0):
#     return ft * 0.3048 + inch * 0.0254
#
#
# def lb_to_kg(lb):
#     return lb * 0.45359237
#
#
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None
#
#     return weight / height ** 2
#
#
# print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))


# password generator:
# import random
# print("Welcome to the password Generator!")
# letters = int(input("How Many letters would you like to have in your password:"))
# numbers = int(input("How Many numbers would you like to have in your password:"))
# symbols = int(input("How Many symbols would you like to have in your password:"))
# l1 = []
# l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
#      "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#
# n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# s = ["!", "@", "#", "$", "%", "&", "*", "^", "(", ")", "+", "?", "<", ">", "/",  "{", "}"]
# for i in range(letters):
#     l1.append(random.choice(l))
# for j in range(numbers):
#     l1.append(random.choice(n))
# for k in range(symbols):
#     l1.append(random.choice(s))
#
# random.shuffle(l1)
# x = "".join(l1)
# print(f"Your secret password is: {x}")

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
#
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#
#
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))
# def factorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     fact = 1
#     for element in range(2, n+1):
#         fact *= element
#     return fact
#
# n = int(input("enter the number:"))
# for i in range(1, n+1):
#     print(f"{i} factorial is {factorial(i)}")


# import time
# fact = 1
# i = 1
# n = int(input())
# while True:
#     if i > 0:
#         fact *= n
#         print(f"The factorial of {i} is {fact}")
#         i += 1
#         n += 1
#         time.sleep(1)



# n = int(input())
# for i in range(1, n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact = fact * j
#     print(f"the factorial of {i} is {fact}")
#-----------------------------------------------------------------------------------------------------------------------

# n = int(input("enter a range:"))
# c = 1
# fib1 = 1
# fib2 = 1
# fib = 0
# while c <= n:
#     fib = fib1+fib2
#     print(fib1, end=" ")
#     fib1 = fib2
#     fib2 = fib
#     c += 1


# n = int(input("enter a range:"))
# fib1 = 1
# fib2 = 1
# fib = 0
# while fib1 < n:
#     fib = fib1+fib2
#     print(fib1, end=" ")
#     fib1 = fib2
#     fib2 = fib


# import time
# n = 1
# fib1 = 1
# fib2 = 1
# total = 0
# while n > 0:
#     total = fib1 + fib2
#     print(f"{n} fibonacci number is {fib1}")
#     fib1, fib2 = fib2, total
#     n += 1
#     time.sleep(1)


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))


#WAP TO CHECK A NUMBER IS ARMSTRONG OR NOT
# n = int(input("enter a number:"))
# a = str(n)
# m = n
# s = 0
# while n > 0:
#           r = n % 10
#           s = s+r**len(a)
#           n = n//10
# if (m == s):
#     print("ARMSTRONG")
# else:
#     print("NA")


# n = int(input())
# for i in range(n):
#     m = i
#     a = str(i)
#     s = 0
#     while i > 0:
#         r = i % 10
#         s = s + r ** len(a)
#         i = i // 10
#     if s == m:
#         print(s)
#

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']
#
# for each in words:
#     if each in dictionary:
#         print(each, "----->", dictionary[each])
#     else:
#         print(f"{each} is not in dictionary")

# writing properly: This is called hanging indent
# dictionary = {
#               "cat": "chat",
#               "dog": "chien",
#               "horse": "cheval"
#               }
#
# for keys in sorted(dictionary):
#     print(keys, '----->', dictionary[keys])

# dictionary = {
#               "cat": "chat",
#               "dog": "chien",
#               "horse": "cheval"
#               }
# dictionary["dgs"] = "medak"
# dictionary.update({"duck": "canard"})
# print(dictionary)
# del dictionary["dgs"]
# print(dictionary)
# dictionary.popitem()
# print(dictionary)

# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)



# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
#
# for item in (d1, d2):
#     d3.update(item)
#
# print(d3)
#----------------------------------------------------------------------------------------------------------------------

# l = [1, 2, 3, [4, 5, 6]] valid
# l = [1, 2, 3, (4, 5, 6)] valid
# l = [1, 2, 3, {4, 5, 6}] valid [but we can not access l[3][0]
# l = [1, 2, 3, {1: "one", 2: "two", 3: "three"}] valid [here l[3][1] = "one", l[3][2] = "two"]


# t = (1, 2, 3, [4, 5, 6]) valid
# t = (1, 2, 3, (4, 5, 6)) valid
# t = (1, 2, 3, {4, 5, 6}) valid[but we can not access t[3][0] or t[3][1] or t[3][2]]
# t = (1, 2, 3, {1: "one", 2: "two", 3: "three"}) valid [here l[3][1] = "one", l[3][2] = "two"]


# s = {1, 2, 3, [4, 5, 6]}     TypeError: unhashable type: 'list'
# s = {1, 2, 3, (4, 5, 6)}     print(s) is valid but print(s[3]) is invalid because set is unordered.so no indexing
# s = {1, 2, 3, {4, 5, 6}}       TypeError: unhashable type: 'set'
# s =  {1, 2, 3, {1: "one", 2: "two", 3: "three"}}      TypeError: unhashable type: 'dict'


#  In dictionary the key should be hashable type.Hence list and set can not be used as keys in dictionary
#  Every element in set should be hashable
# List and set are unhashable.Hence we can not take list in set and set in set
# the values of the dict can be of any type

# HASHABLE TYPE
# INT, FLOAT, DECIMAL, COMPLEX, BOOLEAN , TUPLE

#UN HASHABLE TYPE
# LIST, SET, DICT, BYTE ARRAY

# ----------------------------------------------------------------------------------------------------------------------


# my_list = [x * x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
# print(fun(my_list))


# def fun(x):
#     if x % 2 == 0:
#         return  None
#     else:
#         return 2
# print(fun(fun(2)))

# l = [1, 2]
# for v in range(2):
#     l.insert(-1, l[v])
# print(l)



# def func(x):
#     global y
#     y = x * x
#     return y
# func(2)
# print(y)


# ---------------------------------------------------------------------------------------------------------------------



# try:
#     print("stmt - 1")
#     print(10/0)
#
# except TypeError:
#     print("VE")
# finally:
#     print("outer finally")
# print("dgs")
# ----------------------------------------------------------------------------------------------------------------------
# try:
# 	fp=open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\stud1.data")
#
# except FileNotFoundError:
# 	print("File does not exist")
#
# else:
# 	print("File Opened Successfully in Read Mode:")
# 	print("Type of fp=",type(fp))
# 	print("Is File Closed--else block:", fp.closed)
# 	print("File Mode Name=",fp.mode)
#
#
# finally:
# 	print("\nI am from finally block:")
# 	fp.close()
# 	print("Is File Closed in finally block:", fp.closed)

# ---------------------------------------------------------------------------------------------------------------------

# fp = open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\stud1.data", "w")
# print("File Created Successfully in Write Mode:")
# print("Type of fp=", type(fp))
# ----------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("stud4.data") as fp:
# 		print("File Opened Successfully in Read Mode:")
# 		print("Type of fp=", type(fp))
# 		print("Is File Closed--within with-open() as Indentation block:", fp.closed)
#
# 	print("\ni am out-of with-open() as Indentation block:")
# 	print("Is File Closed--out-of with-open() as Indentation block:", fp.closed)
#
# except FileNotFoundError:
# 	print("File does not exist:")
# -----------------------------------------------------------------------------------------------------------------------

# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\stud4.data", "a+")as fp:
# 	print("-"*50)
# 	print("File Opened in Write Mode:")
# 	print("Name of File =", fp.name)
# 	print("File Opening Mode=", fp.mode)
# 	print("Is File Writable=", fp.writable())
# 	print("Is File Readable=", fp.readable())
# 	print("-"*50)
# ----------------------------------------------------------------------------------------------------------------------


# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\kvr.data", "x")as fp:
# 		print("-"*50)
# 		print("File Opened in Write Mode:")
# 		print("Name of File =", fp.name)
# 		print("File Opening Mode=", fp.mode)
# 		print("Is File Writable=", fp.writable())
# 		print("Is File Readable=", fp.readable())   False
# 		print("-"*50)
# except FileExistsError:
# 	print("File Name alerady Exist:")

# ---------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\hyd.data", "x+")as fp:
# 		print("-"*50)
# 		print("File Opened in Write Mode:")
# 		print("Name of File =", fp.name)
# 		print("File Opening Mode=", fp.mode)
# 		print("Is File Writable=", fp.writable())
# 		print("Is File Readable=", fp.readable())       True
# 		print("-"*50)
# except FileExistsError:
# 	print("File Name alerady Exist:")

# ----------------------------------------------------------------------------------------------------------------------

# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\addr1.data", "w")as fp:
# 	fp.write("Travis El Olihpant\n")
# 	fp.write("FNO:13-14, Hill Side\n")
# 	fp.write("Numpy Foundation\n")
# 	fp.write("Nethet Lands-56\n")
# 	print("Data Written to the file")

# ---------------------------------------------------------------------------------------------------------------------
# obj = [10, 20, 30, 10, 20, 30]
# with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\addr2.data", "w")as fp:
# 	fp.writelines(str(obj))
# 	print("Data Written to the file")

# This mode is used for opening the file name in READ Mode.
# If we open the file name in 'r' mode and if the file name does not exist then we get
#     FileNotFoundError.
# "r" mode is default mode of all file opening modes.

# ---------------------------------------------------------------------------------------------------------------------
# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\addr1.data")as fp:
# 		print("Initial Position of fp before reading=", fp.tell())
# 		print(fp.read())
# 		print("Position of fp after reading=", fp.tell())
# 		print("-"*40)
# 		fp.seek(6)
# 		print("Now after Seek--Position of fp before reading=", fp.tell())
# 		print(fp.read(10))
# 		print("Position of fp after reading=", fp.tell())
#
# except FileNotFoundError:
# 	print("File does not Exist");
# ----------------------------------------------------------------------------------------------------------------------


# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abc.data", "w")as fp:
# 		fp.write("Travis El Olihpant\n")
# 		fp.write("FNO:13-14, Hill Side\n")
# 		fp.write("Numpy Foundation\n")
# 		fp.write("Nethet Lands-56\n")
# 		fp.write("dgs")
# 		print("Data Written to the file")

# except FileNotFoundError:
# 	print("File not found in specified location:")

# If we run this program we get the o/p of Travis EL oliphant details

# ----------------------------------------------------------------------------------------------------------------------
# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abc.data", "w")as fp:
# 		fp.write("dgs\n")
# 		fp.write("medak\n")
# 		fp.write("Telangana\n")
# 		fp.write("India\n")
# 		print("Data got overridden")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")

# Again if we run the program by keeping the file name same we wont get travis details and we get dgs details bcoz
# W mode overrides the previous data
#-----------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abc.data", "a")as fp:
# 		fp.write("dgs\n")
# 		fp.write("medak\n")
# 		fp.write("Telangana\n")
# 		fp.write("India\n")
# 		fp.write("shyam\n")
# 		fp.write("samhitha\n")
# 		print("Data Appended  to the file")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")

# ----------------------------------------------------------------------------------------------------------------------


# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abc.data", "r+")as fp:
# 		fp.write("dgs\n")
# 		fp.write("medak\n")
# 		fp.write("Telangana\n")
# 		fp.write("India\n")
# 		fp.write("shyam\n")
# 		fp.write("samhitha\n")
# 		print(fp.read())
# 		fp.write("prasad sharma")
# 		print(fp.readable())
# 		print(fp.writable())
# 		print("This file can perform both read and write operations")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")
# ---------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abcd.data", "w+")as fp:
# 		fp.write("dgs\n")
# 		fp.write("medak\n")
# 		fp.write("Telangana\n")
# 		fp.write("India\n")
# 		fp.write("shyam\n")
# 		fp.write("samhitha\n")
# 		print(fp.readable())
# 		print(fp.writable())
# 		print("Data written  to the file")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")

# Now opening the same file again.Now the data gets overlapped ie we wont get previous data

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abcd.data", "w+")as fp:
# 		fp.write("hello\n")
# 		fp.write("my\n")
# 		fp.write("name\n")
# 		fp.write("is\n")
# 		fp.write("Gangadhar\n")
# 		fp.write("sharma\n")
# 		fp.write("dammannagari")
# 		print(fp.read())
# 		print("Data overridden successfully")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")
# ----------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abcd.data", "a+")as fp:
# 		fp.write("\nhello\n")
# 		fp.write("my\n")
# 		fp.write("name\n")
# 		fp.write("is\n")
# 		fp.write("Gangadhar\n")
# 		fp.write("sharma\n")
# 		fp.write("dammannagari\n")
# 		fp.write("I am\n")
# 		fp.write("from\n")
# 		fp.write("medaK")
# 		print(fp.read())
# 		print("Additional Data added successfully")
#
# except FileNotFoundError:
# 	print("File not found in specified location:")

# ----------------------------------------------------------------------------------------------------------------------

# try:
# 	with open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\New folder\\abcde.data", "x")as fp:
# 		fp.write("\nhello\n")
# 		fp.write("my\n")
# 		fp.write("name\n")
# 		fp.write("is\n")
# 		fp.write("Gangadhar\n")
# 		fp.write("sharma\n")
# 		fp.write("dammannagari\n")
# 		fp.write("I am\n")
# 		fp.write("from\n")
# 		fp.write("medak")
# 		print("Additional Data added successfully")
#
# except FileExistsError:
# 	print("File found in specified location:")
#-----------------------------------------------------------------------------------------------------------------------
# import functools
# l = [0, 5, 10, 15, 20, 25, 30]
#
# l1 = list(filter(lambda x: x > 10, l))
# print(l1)
# l2 = list(map(lambda x: x ** 2, l))
# print(l2)
# l3 = functools.reduce(lambda a, b: a + b, l)
# print(l3)

# def func(n):
#     return n * n
# x = lambda a: func(a)
# print(x(5))
#----------------------------------------------------------------------------------------------------------------------
# DECORATORS:
# def outer():
#     print("outer function:")
#     def inner(n):
#         print("inner function:")
#         return  n ** 2
#     return  inner
#
# new = outer()
# print(new(5))
# ----------------------------------------------------------------------------------------------------------------------

# def f1(func):
#     print("hello i am the first function")
#     print("my name is dgs")
#     return func
#
#
# def fx(func1):
#     print("this is fx function")
#     return func1
#
# def fy():
#     print("this is fy function")
#
# n = f1(fx)
# n(fy)
# n1 =fx(fy)
# n1()



# def func1(func2):
#     print("hello this is first function")
#     print("hello my name is dgs")
#     return func2
#
# def func2(func3):
#     print("hello this is second function")
#     print("my father name is prasad sharma")
#     return func3
#
# def func3():
#     print("hello this is third function")
#     print("my mother name is vani")
#
# n = func1(func2)
# n(func3)
# n1 = func2(func3)
# n1()


# def decor(func):
#     def inner(x, y):
#         print(f"The addition od {x} and {y} is:", end="")
#         func(x, y)
#     return inner
# @decor
# def add(a, b):
#     print(a + b)
# add(10, 20)

# def decor(func):
#     def inner(a, b):
#         if b == 0:
#             print("we can not divide by zero")
#         else:
#             print(f"The division of {a} and {b} is:", end="")
#             return func(a, b)
#     return inner
#
# @decor
# def divide(x, y):
#     x, y = y, x
#     print(x / y)
#
# divide(20,10)
# -----------------------------------------------------------------------------------------------------------------------
# def beautiful(ugly):
#     def beauty():
#         print(f"hello i am printing the factorial of")
#         return ugly()
#     return beauty
#
# @beautiful
#
#
# def ugly():
#     n = int(input("enter any number:"))
#     print(n ** 2)
# ugly()
# ---------------------------------------------------------------------------------------------------------------------


# def decor2(func):
#     def inner2():
#         x = func()
#         return x * x
#     return inner2
#
#
# def decor1(func):
#     def inner1():
#         x = func()
#         return 2 * x
#     return inner1
#
# @decor2
# @decor1
# def num():
#     return 10
# num()




# def upper_d(func):
#     def inner():
#         return "first" + func() + "second1"
#     return inner
#
#
# def split_d(inner):
#     def wrap():
#         return "second" + inner() + "second2"
#     return wrap
#
# @split_d
# @upper_d
# def ordinary():
#     return "good morning"
# print(ordinary())


# a = int(input())
# b = int(input())
# c = max(a, b)
# while c <= a * b:
#     if c % a == 0 and c % b == 0:
#         break
#     else:
#         c += 1
# print(c)


# def func(func1):
#     print("This is the first function")
#     func1(wrap2)
# def wrap1(func2):
#     print("This is function 2")
#     func2(wrap3)
#
# def wrap2(func3):
#     print("this is function 3")
#     func3()
#
# def wrap3():
#     print("this is function 4")
#
#
# func(wrap1)

# 1.Index [gives the index of the first occurance of given elememt.If element not found in list we get value error]
# 2.append[ It append the given element at end of list and it takes only one argument]
# l = [1, 2, 3]
# l1 = [4, 5]
# l.append(l1)
# print(l)         [1, 2, 3, [4, 5]]

# 3. Extend:
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l2.extend(l1)
# print(l2)                [4, 5, 6, 1, 2, 3]
# print(l1)                [1, 2, 3]



# l = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# for each in l:
#     if each == 1:
#         l.remove(1)
#         print(l)
# # print(l)
import copy

# l1 = [1, [2, 3], 4]
# l2 = l1
# l3 = l1.copy()
# # l4 = copy.deepcopy(l1)
# l1.append(5)
# l1[1][1] = 999
#
# print(l1)
# print(l2)
# print(l3)


# class A:
#     def __init__(self):
#         print("hello i am parent class constructor")
#
#     def m1(self):
#         print("I am parent class m1 method")
#
#     def m2(self):
#         print("i am parent class m2 method")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#
#     def m12(self):
#         print("I am child class m12 method")
#
#     def m23(self):
#         print("i am child class m23 method")
#
#
# class C(A):
#     def __init__(self):
#         super().m1()
#
#     def m121(self):
#         print("I am grand child class m121 method")
#
#     def m231(self):
#         print("i am grand child class m231 method")
#
#
#
# c = C()
# c.m121()
#---------------------------------------------------------------------------------------------------------------------
# def changeme( mylist ):
#     mylist.append([1, 2, 3, 4])
#     print("Values inside the function: ", mylist)

# mylist = [10,20,30]
# changeme(mylist)
# print("Values outside the function: ", mylist)

# ---------------------------------------------------------------------------------------------------------------------
# def changeme( mylist ):
#     mylist = [1, 2, 3, 4]
#     print("Values inside the function: ", mylist)
#
# mylist = [10,20,30]
# changeme(mylist)
# print("Values outside the function: ", mylist)
# ----------------------------------------------------------------------------------------------------------------------

# capitalize
# center [default is space]
# case fold (converts all letters to lower case)
# count
# endswith
# Find [default is -1]
# format
# Index [same as find but if if the index not found it raises error]
# isalnum
# isalpha
# isascii
# isdecimal


