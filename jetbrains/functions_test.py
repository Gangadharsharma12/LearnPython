# def sum_():
#     number_one, number_two = input('Enter two numbers to add with space as seperator:').split()
#     return int(number_one) + int(number_two)
# def multiplication_(a, b):
#     prod = a * b
#     return prod
#
#
# #addition = sum_()
#
#
# result = multiplication_(int(input('Enter a number to multiply:')), sum_())
# print(result)


#
# def sum_(a, b):
#     print(a + b)
#
#
# def subtraction(a, b):
#     print(a - b)
#
#
# def multiplication(a, b):
#     print(a * b)
#
#
# input_ = input().split()
# number_one = int(input_[0])
# number_two = int(input_[1])
# operator_ = input_[2]
# if operator_ == '+':
#     sum_(number_one, number_two)
# elif operator_ == '-':
#     subtraction(number_one, number_two)
# elif operator_ == '*':
#     multiplication(number_one, number_two)
#

# input_ = input().split()
# number_one = int(input_[0])
# number_two = int(input_[1])
# operator_ = input_[2]
# if operator_ == '+':
#     print(number_one + number_two)
# elif operator_ == '-':
#     print(number_one - number_two)
# elif operator_ == '*':
#     print(number_one * number_two)



# print(max("gloomy", "grew", "green"))
# print(min("gloomy", "grey", "green"))
# print(max("gloomy", "grey", "green"))

#
# name = input()
# print("Hello, world! Hello",name)
# Hello, world! Hello, John
# Hello, world! Hello John
# Hello, world! Hello John


# from math import copysign
# x = float(input())
# y = float(input())
# print(copysign(x, y))

# from math import copysign
# x, y = map(float, input().split(' '))
# print(copysign(x,y))
# print(type(x))


# income_ = int(input())
# if income_ <= 15527:
#     percent_ = 0
#     calculated_tax = 0
# elif 15528 <= income_ <= 42707:
#     percent_ = 15
#     calculated_tax = round((percent_ / 100) * income_)
# elif 42708 <= income_ <= 132406:
#     percent_ = 25
#     calculated_tax = round((percent_ / 100) * income_)
# else:
#     if income_ >= 132407:
#         percent_ =  28
#         calculated_tax = round((percent_ / 100) * income_)
# print(f"The tax for {income_} is {percent_}%. That is {calculated_tax} dollars!")
#


# string = "red yellow fox bite orange goose beeeeeeeeeeep"
# vowels = 'aeiou'
# l =[]
# for each in string:
#     if each in vowels:
#         l.append(each)
# print(len(l))


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


# l = []
# sum = 0
# option = int(input())
# option_2 = int(input())
# for i in range(option,option_2 + 1):
#     if i % 3 == 0:
#         l.append(i)
#         sum = sum + i
# print(sum / len(l))


# for x in range(1, 4):
#     for y in range(-3, 0):
#         print(x * y)



# sum_ = 0
# while True:
#     number = int(input())
#     if number == 55:
#         break
#     sum_  += number
#     i = i + 1
# print(i)
# print(sum_)
# print(round(sum_ / i))


# n = int(input())
# total = 0
# for i in range(n):
#     x= int(input())
#     total += x
# print(float(total / n))


# text = input()
# for s in text:
#     if s.isupper():
#         text = text.replace(s, "_" + s.lower())
#
# print(text)



# n = int(input())
# l = []
# for i in range(n):
#     x = int(input())
#     if x % 7 == 0:
#         print(x ** 2)

# b = 30
# def fun(a, b = b):
#     return a + b
# print(fun(1))


# water = int(input("Write how many ml of water the coffee machine has:"))
# milk = int(input("Write how many ml of milk the coffee machine has:"))
# coffee_bean = int(input("Write how many grams of coffee beans the coffee machine has:"))
# coffee = int(input("Write how many cups of coffee you will need:"))
# number_of_coffee = 0
# l = []
#
#
# def final_output(water_,milk_, coffee_beans, coffee_ ):
#     string = ''
#     if water_ < 200 or milk_ < 50 or coffee_beans < 15:
#         number_of_coffees = 0
#     else:
#         by_water = water_ // 200
#         l.append(by_water)
#         by_milk = milk_ // 50
#         l.append(by_milk)
#         by_beans = coffee_beans // 15
#         l.append(by_beans)
#         number_of_coffees = min(l)
#     if coffee_ == number_of_coffees:
#         string = "Yes, I can make that amount of coffee"
#     elif coffee_ < number_of_coffees:
#         string = f"Yes, I can make that amount of coffee (and even {number_of_coffees - coffee_} more than that)"
#     else:
#         string = f"No, I can make only {number_of_coffees} cups of coffee"
#     return string
#
#
# print(final_output(water,milk,coffee_bean,coffee))






# water_ = int(input("Write how many ml of water the coffee machine has:"))
# milk_ = int(input("Write how many ml of milk the coffee machine has:"))
# coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
# coffee_ = int(input("Write how many cups of coffee you will need:"))
# number_of_coffee = 0
# l = []
# if water_ < 200 or milk_ < 50 or coffee_beans < 15:
#     number_of_coffee = 0
# else:
#     by_water = water_ // 200
#     l.append(by_water)
#     by_milk = milk_ // 50
#     l.append(by_milk)
#     by_beans = coffee_beans // 15
#     l.append(by_beans)
#     number_of_coffee = min(l)
# if coffee_ == number_of_coffee:
#     print("Yes, I can make that amount of coffee")
# elif coffee_ < number_of_coffee:
#     print(f"Yes, I can make that amount of coffee (and even {number_of_coffee - coffee_} more than that)")
# else:
#     print(f"No, I can make only {number_of_coffee} cups of coffee")



# import random
# n_guesses = 0
# while n_guesses < 5:
#     number = random.randint(1, 5)
#     print(number)
#     guess = int(input())
#     if guess == number:
#         print('Yes!')
#     else:
#         print('No!')
#     n_guesses += 1



# while True:
#     choice = input().split()
#     l1 = []
#     l2 = []
#     if choice != "MEOW":
#         l1.append(choice[0])
#         l2.append([choice[1]])
#     else:
#         break
#     print(max(l2))


# x = input()
# if x == x[::-1]:
#     print("true")
# else:
#     print("false")

# class Solution:
#
#
#     def isPalindrome(self, x):
#         value = 0
#         num = x
#         while num > 0:
#             a = num % 10
#             value = (value * 10) + a
#             num //= 10
#
#         if value == x:
#             print("true")
#         else:
#             print("false")
#
# x = int(input())
# s = Solution()
# s.isPalindrome(x)







# x = int(input())
# rev_n = 0
# while x > 0:
#     v = x % 10
#     rev_n = (rev_n * 10) + v
#     x = x // 10
# print(rev_n)


