# UPDATED ATM APPLICATION
# import sys
# import time
# class bank:
#     name = "state bank of India"
#     acc = "XXXXXXXX595"
#     def __init__(self,minimum_balance = 1000,avl_bal = 5000):
#         self.Minimum = minimum_balance
#         self.Avl = avl_bal
#
#     def deposit(self, amount):
#         self.Amount = amount
#         self.Avl += self.Amount
#         op = input("Do you want to display the available balance[Yes | No]").lower()
#         if op == "yes":
#             self.credit()
#
#     def withdraw(self, amount):
#         self.Amount = amount
#         if self.Avl - self.Amount < self.Minimum:
#             print("sorry the minimum balance should be atleast 1000 RS")
#         else:
#             self.Avl -= self.Amount
#             print("please wait")
#             time.sleep(5)
#             print("please collect your cash")
#             op1 = input("Do you want to display the available balance[Yes | No]").lower()
#             if op1 == "yes":
#                 self.debit()
#
#     def bal(self):
#         print(f"Your current account balance is {self.Avl}")
#
#     def pin(self):
#         attempts = 3
#         print(f"Hello you have {attempts} attempts to enter correct pin:")
#         while attempts > 0:
#             pc = int(input("please enter your old pin:"))
#             if pc == 4235:
#                 pc1 = int(input("please enter your new pin:"))
#                 print("your pin has been changed successfully")
#                 break
#             else:
#                 attempts -= 1
#                 if attempts > 1:
#                     print(f"sorry,Wrong pin.you have {attempts} attempts left")
#                 elif attempts == 1:
#                     print(f"sorry,Wrong pin.you have {attempts} attempt left")
#                 else:
#                     print("You dont have any attempts left")
#
#         else:
#             print("Your card is temporarly blocked for 24 Hours.please try after 24 hours. For more details please contact toll free number 1234123423.Thank you")
#             sys.exit()
#
#
#     def leave(self):
#         ch = input("Do you want to display the available balance before leaving [yes | no]").lower()
#         if ch == "yes":
#             self.bal()
#             print("Thank you for choosing our banking services.Have a great day")
#             sys.exit()
#
#         else:
#             print("Thank you for choosing our banking services.Have a great day")
#             sys.exit()
#
#     def credit(self):
#         print(f"your account {bank.acc} has been credited with INR {self.Amount} and your current account balance is {self.Avl}")
#
#     def debit(self):
#             print(f"your account {bank.acc} has been debited with INR {self.Amount} and your current account balance is {self.Avl}")
#
#
# b = bank()
# print(f"Hello welcome to {bank.name} services")
# n = input("please enter your name:")
# print(f"Hello {n}", end=" ")
# print("please insert your card\nReading card...")
# time.sleep(5)
# while True:
#     print()
#     print("Please select your operation from below options:")
#     print("1.Deposit\n2.Withdraw\n3.Balance enquiry\n4.Pin change\n5.exit")
#     print()
#     choice = int(input("please select your choice:"))
#     if choice == 1:
#         amt = int(input("Please enter the amount to deposit:"))
#         if amt <= 0:
#             print("invalid amount to deposit")
#         else:
#             b.deposit(amt)
#
#
#     elif choice == 2:
#         amt = int(input("please enter the amount to withdraw:"))
#         b.withdraw(amt)
#
#     elif choice == 3:
#         b.bal()
#
#     elif choice == 4:
#         b.pin()
#
#     elif choice == 5:
#             b.leave()
#     else:
#         print("please select a valid option")
# ----------------------------------------------------------------------------------------------------------------------
#
# import sys
# class Customer:
#     '''This bank application is developed by dgs '''
#     bankname = "STATE BANK OF INDIA"
#     print("This ATM accepts only 200 and 500 denominations for credit and debit")
#     account_no = "XXXXXXX595"
#     def __init__(self, name, balance = 500.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amt):
#         self.balance += amt
#         c.display()
#
#     def withdraw(self, amt):
#         if amt == self.balance:
#             print("The minimum balance should be 500 Rs")
#         elif amt > self.balance:
#             print("insufficient funds...can not perform this operation now")
#             sys.exit()
#         else:
#             self.balance -= amt
#             c.display()
#     def display(self):
#         print("Your current balance is:", self.balance)
#
#     def thanks(self):
#         print("Thank you for choosing our banking services:")
#
# print(Customer.__doc__)
# print("Hello, welcome to", Customer.bankname)
# name = input("please enter your name:")
# c = Customer(name)
# print(f"Hello {name} welcome to {Customer.bankname} services and your current balance is {c.balance}")
# while True:
#     print("Please select your operation")
#     print('1-Deposit \n2-Withdraw \n3-balance enquiry\n4-exit')
#     option = input("please select your choice:")
#     if option == "1":
#         amt = float(input("enter amount to deposit:"))
#         while amt % 500 != 0 or amt % 200 != 0:
#             print("please insert only 500 or 200 denominations")
#             amt = float(input("enter amount to deposit:"))
#         print(f"Your Account {Customer.account_no} is credited with Inr {amt}")
#         c.deposit(amt)
#
#     elif option == "2":
#         amt = float(input("enter amount to withdraw:"))
#         while amt % 500 != 0 or amt % 200 != 0:
#             print("please select only 500 or 200 denominations")
#             amt = float(input("enter amount to withdraw:"))
#         print(f"Your Account {Customer.account_no} is debited with Inr {amt}")
#         c.withdraw(amt)
#
#     elif option == "3":
#         c.display()
#
#     elif option == "4":
#         c.thanks()
#         sys.exit()
#
#     else:
#         print("Please select a valid option")
# ----------------------------------------------------------------------------------------------------------------------
# def fib(n):
#     a = 1
#     b = 1
#     d = {}
#     c = 1
#     while len(d) < n:
#         d[c] = a
#         res = a + b
#         a = b
#         b = res
#         c += 1
#     return d[n]
# n = int(input())
# print(f"The number present at {n}th index in fibonacci series is {fib(n)}")

# ---------------------------------------------------------------------------------------------------------------------
#  udemy coding exercise 19
# def myfunc(a):
#     d = {}
#     for i in range(0, len(a)):
#         d[i + 1] = a[i].lower()
#     for each in d:
#         if each % 2 == 0:
#             d[each] = d[each].upper()
#
#     for i in d:
#         print(d[i], end="")
# ----------------------------------------------------------------------------------------------------------------------

# WAP TO PRINT THE PALINDROME OF NUMBER IF THE NUMBER IS PRIME

# n = int(input("Enter a number:"))
# for i in range(2, n):
#         if n % i == 0:
#             x = str(n)
#             y = ""
#             z = -1
#             while z >= -len(x):
#                 y += x[z]
#                 z -= 1
#             if int(y) == n:
#                 print(f"reversed string:{y}")
#                 print(f"{n} is not a prime number but it is palindrome")
#                 break
#             else:
#                 print(f"reversed string:{y}")
#                 print(f"{n} is not a prime number as well as not a palindrome")
#                 break
# else:
#     a = str(n)
#     b = ""
#     c = -1
#     while c >= -len(a):
#         b += a[c]
#         c -= 1
#     if int(b) == n:
#         print(f"{n} is palindromic prime number")
#     else:
#         print(f"{n} is prime number but not palindrome")
# ---------------------------------------------------------------------------------------------------------------------
# x = 100
# def f1():
#     x = 200
#     print("enclose before", x)
#     def f2():
#         print(x)
#         print("local", x)
#     f2()
# print("global before", x)
# f1()
#----------------------------------------------------------------------------------------------------------------------
# WAP TO REVERSE THE NUMBERS IN THE GIVEN LIST
# l = [1, 21, 36, 48, 145, 254, 423, 665]
# l1 = []
# for each in l:
#     a = str(each)
#     b = ""
#     c = -1
#     while c >= -(len(a)):
#         b += a[c]
#         c -= 1
#     l1.append(int(b))
# print(l1, end=" ")
# ----------------------------------------------------------------------------------------------------------------------

# ROCK PAPER SCISSOR:
#
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
#             print("Game over!")
#             sys.exit()
#         else:
#             print("player1 won and the score of player 1 ", end=" ")
#             sp1 = sp1 + 1
#             print(sp1)
#             break
#     else:
#         print("player2 selected invalid option")
#         break


# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"b": 200, "c": 300, "a": 100}
# print(d1 == d2)



# ---------------------------------------------------------------------------------------------------------------------
# WAP TO PRINT THE SUM OF INDIVIDUAL ELEMENTS IN A LIST

# l = [321, 456, 23, 67, 2, 6789]
# l1 = []
# for i in l:
#     l2 = 0
#     for j in str(i):
#         l2 = l2 + (int(j))
#     l1.append(l2)
# print(l1)

# WAP TO PRINT THE PRODUCT  OF INDIVIDUAL ELEMENTS IN A LIST

# l = [321, 456, 23, 67, 2, 6789]
# l1 = []
# for i in l:
#     l2 = 1
#     for j in str(i):
#         l2 = l2 * (int(j))
#     l1.append(l2)
# print(l1)

# WAP TO PRINT THE SQUARE OF INDIVIDUAL ELEMENTS IN A LIST BY ADDING THE ELEMENTS:

# l = [321, 456, 23, 67, 2, 6789]
# l1 = []
# for i in l:
#     l2 = 0
#     for j in str(i):
#         l2 = l2 + (int(j))
#     l1.append(l2 ** 2)
# print(l1)

# WAP TO PRINT THE SQUARE OF INDIVIDUAL ELEMENTS IN A LIST BY MULTIPLYING THE ELEMENTS:

# l = [321, 456, 23, 67, 2, 6789]
# l1 = []
# for i in l:
#     l2 = 1
#     for j in str(i):
#         l2 = l2 * (int(j))
#     l1.append(l2 ** 2)
# print(l1)
# ---------------------------------------------------------------------------------------------------------------------
# WAP TO PRINT THE TABLES UPTO GIVEN RANGE :
# n = int(input("enter the first table:"))
# n1 = int(input("enter the last table:"))
# for i in range(n, n1+1):
#     if n <= n1:
#         if i == 1:
#             print("-" * 40)
#             print("printing {}st table:".format(i))
#             print("-" * 40)
#             for j in range(1, 11):
#                 print("{} * {} = {}".format(n, j, j * n))
#         elif i == 2:
#             print("-" * 40)
#             print("printing {}nd table:".format(i))
#             print("-" * 40)
#             for j in range(1, 11):
#                 print("{} * {} = {}".format(n, j, j * n))
#
#         elif i == 3:
#             print("-" * 40)
#             print("printing {} rd table:".format(i))
#             print("-" * 40)
#             for j in range(1, 11):
#                 print("{} * {} = {}".format(n, j, j * n))
#
#         else:
#             print("-" * 40)
#             print("printing {}th table:".format(i))
#             print("-" * 40)
#             for j in range(1, 11):
#                 print("{} * {} = {}".format(n, j, j * n))
#     n += 1
#     print()
# --------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter how many tables you want:"))
# if n <= 0:
#     print("{} is an invalid option".format(n))
# else:
#     l = []
#     for i in range(1, n+1):
#         n = int(input("Enter {} value:".format(i)))
#         l.append(n)
#     print("*" * 50)
#     print("The selected numbers are {}".format(l))
#     print("*" * 50)
#     for i in range(len(l)):
#         print("printing {} table".format(l[i]))
#         print("*" * 50)
#         for j in range(1, 11):
#             print("{} * {} = {}".format(l[i], j, l[i] * j))
#         print("*" * 50)



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
# func(wrap1)

#----------------------------------------------------------------------------------------------------------------------
# a=10
# b=20
# c=30
# d=40   # Here a,b,c,d are called Global Variable Names
# def   operation():
# 	a=100
# 	b=200
# 	c=300
# 	d=400   # Here a,b,c,d are called Local Variable Names
# 	res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
# 	print("sum of local var vals=",res)
# 	print("=============OR=============")
# 	res=a+b+c+d+globals().get('a')+globals().get('b')+globals().get('c')+globals().get('d')
# 	print("sum of local var vals=",res)
#
# #main program
# operation()
# print(globals())


#   WAP which will implement following

# l = [1, 232, 5545455, 909090, 1212, 8558]
# d = {}
# l1 = []
# for each in l:
#     d[len(str(each))] = each
# for each in l:
#     if str(each) == str(each)[::-1]:
#         l1.append(len(str(each)))
# print("the longest palindrome in {} is {}".format(l, d[max(l1)]))


# l = [5 > 0, 10 < 8, 20 > 100]
# print(any(l))  True
# print(all(l))  False

# from itertools import permutations
# l = permutations([1, 2, 3, 4, 5, 6])
# for i, j in enumerate(l, 1):
#     print(j, "----->", i)


import os
os.environ["PYSPARK_PYTHON"] = "pyhton"
PYSPARK_SUBMIT_ARGS ="--master local[3] pyspark-shell"

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkGetExample").getOrCreate()
data = [(1, "dgs"), (2, "sks")]
col = ("id", "name")
df = spark.createDataFrame(data, col)
df.show()