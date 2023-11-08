# from math import *
#
# choice = input("What do you want to calculate?")
# if choice == "n":
#     loan_principle = int(input("enter the loan principle: "))
#     monthly_payment = int(input("enter the monthly payment: "))
#     loan_intrest = float(input("enter the loan intrest:"))
#     loan_intrest = (loan_intrest / 100) / 12 * (100 / 100)
#     monthly_payment = ceil(log((monthly_payment / (monthly_payment - (loan_intrest * loan_principle))), (1 + loan_intrest)))
#     print(monthly_payment)
#     n_to_years = (monthly_payment // 12)
#     print(n_to_years)
#     n_to_months = (monthly_payment % 12)
#     print(n_to_months)
#     if n_to_years == 0:
#         if n_to_months == 1:
#             print(f"it will take {n_to_months} month to repay the loan!")
#         else:
#             print(f"it will take {n_to_months} months to repay the loan!")
#     elif n_to_years < 2:
#         string = '1 year '
#         if n_to_months == 0:
#             print(f"it will take {n_to_years} years to repay the loan!")
#         elif n_to_months == 1:
#             print(f"it will take {n_to_years} years and {n_to_months} month to repay the loan!")
#         elif n_to_months > 1:
#             print(f"it will take {n_to_years} years and {n_to_months} months to repay the loan!")
#     elif n_to_years >= 2:
#         if n_to_months == 0:
#             print(f"it will take {n_to_years} years to repay the loan!")
#         elif n_to_months == 1:
#             print(f"it will take {n_to_years} years and {n_to_months} month to repay the loan!")
#         elif n_to_months > 1:
#             print(f"it will take {n_to_years} years and {n_to_months} months to repay the loan!")
#
# if choice == "a":
#      loan_principle = int(input("enter the loan principle:"))
#      period = int(input("Enter the number of periods:"))
#      loan_intrest = float(input("enter the loan intrest:"))
#      loan_intrest = (loan_intrest / 100) / 12
#      num = loan_intrest * ((1 + loan_intrest) ** period)
#      den = ((1 + loan_intrest) ** period) - 1
#      annuity_payment =  loan_principle * num / den
#      final_annuity = (ceil(annuity_payment))
#      print(f"your monthly payment {final_annuity}!")
#
#
#
#
# if choice == "p":
#     annuity_payment = float(input("enter the annuity payment:"))
#     period = int(input("enter the number of periods:"))
#     loan_intrest = float(input("enter the loan intrest:"))
#     loan_intrest = (loan_intrest / 100) / 12
#     num = loan_intrest * ((1 + loan_intrest) ** period)
#     den = ((1 + loan_intrest) ** period) - 1
#     principal = annuity_payment / (num / den)
#     final_principle = (round(principal))
#     print(f"your loan principle = {final_principle}!")
######################################################################################################################################################


# from math import *
# loan_principle = int(input("enter the principle amount:"))
# choice = input("What do you want to calculate?")
# m = "monthly payment"
# p = "number_of_months_payment"
# if choice == "m":
#      monthly_payment = int(input("enter the amount to be paid monthly:"))
#      time_taken = ceil(loan_principle / monthly_payment)
#      if time_taken == 1:
#           print(f"It will take 1 month to repay the loan")
#      else:
#           print(f"It will take {time_taken} months to repay the loan")
#
# else:
#      if choice == "p":
#               number_of_months = int(input("enter the number of months:"))
#               time_taken_2 =  ceil(loan_principle / number_of_months)
#               last_payment = loan_principle - (number_of_months - 1) * time_taken_2
#      print(f"Your monthly payment = {time_taken_2} and the last payment = {last_payment}")

#####################################################################################################################################################


# range_ = int(input())
# list_ = []
# for _ in range(range_):
#     list_.append(int(input("enter a number:")))
# print(list_)

# n = input()
# digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
# for i in n:
#     print(digits[int(i)])



# l = ["python","hub"]
# for i in l:
#     l.append(i.upper())
# print(l)


# import argparse
# parser = argparse.ArgumentParser
# parser.add_argument


# x = int(input())
# while True:
#     x = x + 1
#     if x == 10:
#         continue
#     print(x)
#     if x == 20:
#         break


# for x in range(1,20):
#     if x == 10:
#         continue
#     print(x)







# coffee_ = int(input("Write how many cups of coffee you will need:"))
# print(f"for {coffee_} cups of coffee you need:")
# print(200 * coffee_, "ml of water")
# print(50 * coffee_, "ml of milk")
# print(15 * coffee_, "g of coffee beans")


# string = 'Mississippi'
# print(string.lstrip('ips'))
# print(string.rstrip("ips"))
# print(string.strip("ips"))

# string = 'incomprehensibilities'
# print(string.lstrip('is'))
# print(string.rstrip("is"))
# print(string.strip("is"))

# string = "civic"
# print(string.strip('vci'))


# str_ = input()
# str_ = str_.strip("*")
# str_ = str_.strip("_")
# str_ = str_.strip("~")
# str_ = str_.strip("`")
# str_ = str_.strip("''")
# print(str_)


# first_number = float(input())
# second_number = float(input())
# operations = input()
# if second_number == float(0) and operations in ('/', 'div', 'mod'):
#     print("Division by 0!")
# else:
#     if operations == "+" :
#         print(first_number + second_number)
#     if operations == "-":
#         print(first_number - second_number)
#     if operations == "*":
#         print(first_number * second_number)
#     if operations == "/":
#         print(first_number / second_number)
#     if operations == "mod":
#         print(first_number % second_number)
#     if operations == "pow":
#         print(first_number ** second_number)
#     if operations == "div":
#         print(first_number // second_number)


# age = int(input())
# if age <= 16:
#     print("The lion king")
# elif 17 <= age <= 25:
#     print("Trainspotting")
# elif 26 <= age <= 40:
#     print("Matrix")
# elif 41 <= age <= 60:
#     print("Pulp Fiction")
# else:
#     print("Breakfast at Tiffany's")



# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())
# Y = int(input())
# if A * B * C >= X * Y:
#     print("The box can not be carried")
# else:
#     print("The box can  be carried")




# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())
# Y = int(input())
# if X * Y >= A * B:
#     print("The box can be carried")
# elif X * Y >= B * C:
#     print("The box can be carried")
# elif X * Y >= C * A:
#     print("The box can be carried")
# else:
#     print("The box cannot be carried")


# index_ = float(input())
# if index_ < 2:
#     print("Analytic")
# elif  index_ == 2:
#     print("Synthetic")
# elif 2 < index_ <= 3:
#     print("Synthetic")
# else:
#     print("Polysynthetic")




# entry_1 = float(input())
# entry_2 = float(input())
# if entry_1 == 0 and entry_2 == 0:
#     print("It's the origin!")
# elif entry_1 == 0 or entry_2 == 0:
#     print("One of the coordinates is equal to zero!")
# elif entry_1 > 0 and entry_2 > 0:
#     print("I")
# elif entry_1 < 0 and entry_2 > 0:
#     print("II")
# elif entry_1 < 0 and entry_2 < 0:
#     print("III")
# elif entry_1 > 0 and entry_2 < 0:
#     print("IV")


# army = int(input())
# if army < 1:
#     print("no army")
# elif 1 <= army <= 9:
#     print("few")
# elif 10 <= army <= 49:
#     print("pack")
# elif 50 <= army <= 499:
#     print("horde")
# elif 500 <= army <= 999:
#     print("swarm")
# else:
#     print("legion")




# money = int(input())
# chicken = 23
# Goat = 678
# Pig = 1296
# Cow = 3848
# Sheep = 6769
# if money < chicken:
#     print('None')
# if chicken <= money < Goat :
#     number = money // chicken
#     if number > 1:
#         print(number, 'chickens')
#     else:
#         print(number, 'chicken')
# elif Goat <= money < Pig:
#     number = money // Goat
#     if number > 1:
#         print(number, 'goats')
#     else:
#         print(number, 'goat')
# elif Pig <= money < Cow:
#     number = money // Pig
#     if number > 1:
#         print(number, 'pigs')
#     else:
#         print(number, 'pig')
# elif Cow <= money < Sheep:
#     number = money // Cow
#     if number > 1:
#         print(number, 'cows')
#     else:
#         print(number, 'cow')
# elif money >= Sheep:
#     number = money // Sheep
#     print(number, 'sheep')



# year = int(input())
# century = 400
# if year % 4 == 0 and year % 100 != 0:
#     print("Leap")
# elif year % century == 0:
#     print("Leap")
# else:
#     print("Ordinary")


# entry = int(input())
# entry_1 = int(input())
# entry_2 = int(input())
# angle_of_triangle = 180
# if entry + entry_1 + entry_2 == angle_of_triangle:
#     print("The triangle is valid!")
# else:
#     print("The triangle is not valid!")



# print('One')
# print()
# print("""Two
#
# Three""")
# print("")
# print("Four")
#
# input_str = input()
# print(list(input_str))


# l = (1, 2, 3, 4, 5)
# l = list(l)
# print(l)

# fruits = ["apple", "pear", "orange", "mango", "peach"]
#
# print(fruits[0])
# print(fruits[-5])
# print(fruits[4-2])



# Save the input in this variable
# ticket = input()
#
# # Add up the digits for each half
# half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
#
# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")


# event_0 = int(input())
# event_1 = int(input())
# event_2 = int(input())
# event_3 = int(input())
# event_4 = int(input())
# event_5 = int(input())
# hour_sec = 3600
# min_sec = 60
# one_sec = 1
# a = event_0 * hour_sec
# b = event_1 * min_sec
# c = event_2 * one_sec
# d = event_3 * hour_sec
# e = event_4 * min_sec
# f = event_5 * one_sec
# g = d + e + f
# h = g - (a + b + c)
# print(h)



# duration_ = int(input())
# food_cost = int(input())
# flight_cost = int(input())
# hotel_cost = int(input())
# food_cost = food_cost * duration_
# flight_cost = flight_cost + flight_cost
# hotel_cost = (duration_ - 1) * hotel_cost
# total_ = food_cost + flight_cost + hotel_cost
# print(total_)


# choice = int(input())
# a = choice // 100
# b = choice % 10
# c = choice // 10
# d = c % 10
# print(a + b + d)

# choice = int(input())
# a = choice % 10
# b = choice // 10
# print( a * b)

# N = int(input())
# K = int(input())
# print(K % N)
# print(K // N)


# first_number = input()
# second_number = input()
# print(int(first_number) + int(second_number))


# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)


# N = int(input())
# i = 1
# while i < N:
#     if i % 2 == 0:
#               print(i)
#     i = i+1


# N = int(input())
# sum = 0
# for i in range(1, N + 1):
#     sum = sum + i
# print(sum)



# i = 1
# while i <= 20:
#     print(i ** 2)
#     i = i + 1


# sum_ = 0
# i = 0
# while True:
#     number = int(input())
#     if number == 55:
#         break
#     sum_  += number
#     i = i + 1
# print(i)
# print(sum_)
# print(round(sum_ / i))
# ---------------------------------------------------------------------------------------------------------------------

# UDEMY MATH MODULE

# import math
# value = 5.35
# print(math.floor(value))    5



# import math
# value = 6.35
# print(math.ceil(value))      7


# import math
# print(round(math.pi, 2))    3.14

# import random
# random.seed(43)
# print(random.randint(0,100))


# import random
# my_list = range(0, 20)
# print(random.choices(population=my_list, k=10))
# print(random.sample(population=my_list, k=10))
#
#
# l = [1,2,3,4,5,6,7,8]
# random.shuffle(l)
# print(l)
#
#
# print(random.uniform(a=10, b=20))




