
# def sum(a, b):
#     total = a + b
#     return total
# total = sum(10,20)
# print(total)



# import random
# player_1 = input("select rock, paper or scissor:").lower()
# player_2 = random.choice(("rock", "paper", "scissor")).lower()
# print("player_2 selected:",player_2)
# option = "rock","paper","scissor"
# while player_1 in option:
#     if player_1 == "rock" and player_2 == "paper":
#         print("Player_2 won")
#         break
#     elif player_1 == "paper" and player_2 == "scissor":
#         print("Player_2 won")
#         break
#     elif player_1 == "scissor" and player_2 == "rock":
#         print("player_2 won")
#         break
#     elif player_1 == player_2:
#         print("game tie")
#         break
#     else:
#         print("you won")
#         break
# else:
#     print("please enter correct option")

# def f1(x):
#     print(x ** 2 + 1)
#
#
# def f2(x):
#     print(1 / x ** 2)
#
#
# def f3(x):
#     print(x ** 2 - 1)
#
#
# def f(x):
#     if x <= 0:
#         f1(x)
#     elif 0 < x < 1:
#         f2(x)
#     else:
#         f3(x)
#
# x = float(input("Please enter something:"))
# f(x)
#
#
#
#
# def f1(x):
#     return (x ** 2) + 1
#
#
# def f2(x):
#     return 1 / (x ** 2)
#
#
# def f3(x):
#     return x ** 2 - 1
#
#
# def f(x):
#     if x <= 0:
#         return f1(x)
#     if 0 < x < 1:
#         return f2(x)
#     return f3(x)




# print('''The coffee machine has:
# 400 ml of water
# 540 ml of milk
# 120 g of coffee beans
# 9 disposable cups
# $550 of money
# ''')
# water = 400
# milk = 540
# coffee_beans = 120
# disposable_cups = 9
# money= 550
#
# action = input("enter desired action:")
# if action == "buy":
#     choice = input("What do you want to buy:")
#     if choice == "espresso":
#         water = water - 250
#         coffee_beans = coffee_beans - 16
#         money = money + 4
#         disposable_cups = disposable_cups - 1
#         print(f'''
# The coffee machine has:
# {water} ml of water
# {milk} ml of milk
# {coffee_beans} g of coffee beans
# {disposable_cups} disposable cups
# ${money} of money
# ''')
#     elif choice == "latte":
#         water = water - 350
#         milk = milk - 75
#         coffee_beans = coffee_beans - 20
#         money = money + 7
#         disposable_cups = disposable_cups - 1
#         print(f'''
# The coffee machine has:
# {water} ml of water
# {milk} ml of milk
# {coffee_beans} g of coffee beans
# {disposable_cups} disposable cups
# ${money} of money
# ''')
#     else:
#         choice == "cappuccino"
#         water -= 200
#         milk -= 100
#         coffee_beans -= 12
#         disposable_cups -= 1
#         money += 6
#         print(f'''
# The coffee machine has:
# {water} ml of water
# {milk} ml of milk
# {coffee_beans} g of coffee beans
# {disposable_cups} disposable cups
# ${money} of money
# ''')
#
# elif action == "fill":
#     water_added = int(input("Write how many ml of water you want to add:"))
#     milk_added = int(input("Write how many ml of milk you want to add:"))
#     coffee_beans_added = int(input("Write how many grams of coffee beans you want to add:"))
#     disposable_cups_added = int(input("Write how many disposable cups you want to add:"))
#     print(f'''
# The coffee machine has:
# {water + water_added} ml of water
# {milk + milk_added} ml of water
# {coffee_beans + coffee_beans_added} g of coffee beans
# {disposable_cups + disposable_cups_added} disposable cups
# ${money} of money
# ''')
#
# else:
#     if action == "take":
#         money_given = money
#         money_given = money - money_given
#
#         print(f"I gave you ${money_given}")
#         print(f'''
# The coffee machine has:
# {water} ml of water
# {milk} ml of water
# {coffee_beans} g of coffee beans
# {disposable_cups} disposable cups
# ${money_given} of money
# ''')




# n = int(input())
# if n <= 1:
#     print("This number is not prime")
# else:
#     x = 2
#     while x * x <= n:
#         if n % x == 0:
#             print("This number is not prime")
#             break
#         x += 1
#     else:
#         print("This number is prime")


# my_list = range(0,50)
# for el  in my_list:
#     if el >= 40:
#
#     else:
#         print(el)



# limit = 25
# numbers = []
# while len(numbers) < 5:
#     for i in range(limit):
#         if i % 3 != 0:
#             continue
#         else:
#             numbers.append(i)
#
# print(len(numbers))




# str = input()
# rev_str = str[::-1]
# if str == rev_str:
#     print("Palindrome")
# else:
#     print("Not palindrome")



# word = input()
# print('Palindrome' if word == word[::-1] else 'Not palindrome')


# text = input()
# vowel_ = ["a","e","i","o","u"]
# for each in text:
#     if each.isalpha():
#         if each in vowel_:
#             print("vowel")
#         else:
#             print("consonant")
#     else:
#         break





# scores = input().split()
# score = 0
# lives = 3
# for each in scores:
#     if each == "C":
#         score += 1
#     else:
#         lives -= 1
#         if lives == 0:
#             print("Game over")
#             break
# if lives > 0:
#     print("You won")
# print(score)



# class Angel:
#     color = "white"
#     feature = "wings"
#     home = "Heaven"
#     print(color)
#     print(feature)
#     print(home)
#
# class Demon:
#     color = "red"
#     feature = "horns"
#     home = "Hell"
#     print(color, feature, home)
#     print(color)
#     print(feature)
#     print((home))


# print('d-Deposit \nw-Withdraw \nb-balance enquiry \ne-exit')


# class Student:
#     def __init__(kelf, name):
#         kelf.name = name
#     def display(pelf):
#         print("hello",pelf.name)
#
# s = Student("dgs")
# s.display()


# class Ship:
#
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#     # the old sail method that you need to rewrite
#     def sail(self):
#         self.country = input()
#         print(f"The {self.name} has sailed for {self.country}!")
#
#
#
# black_pearl = Ship("Black Pearl", 800)
# black_pearl.sail()






# n_num = [1, 2, 3, 4, 5]
# n = len(n_num)
# n_num.sort()
#
# if n % 2 == 0:
#     median1 = n_num[n // 2]
#     median2 = n_num[n // 2 - 1]
#     median = (median1 + median2) / 2
# else:
#     median = n_num[n // 2]
# print("Median is: " + str(median))



# def mean(n):
#     value = sum(n) / len(n)
#     print("mean:", round(value, 2))
#     median(n)
#
#
# def median(n):
#     l = len(n)
#     n.sort()
#     if l % 2 == 0:
#         median1 = n[l // 2]
#         median2 = n[l // 2 - 1]
#         med = (median1 + median2) / 2
#
#     else:
#         med = l[n // 2]
#     print("median:" + str(med))
#     mode(n)
#
# def mode(n):
#     n.sort()
#     l = []
#     i = 0
#     while i < len(n):
#         l.append(n.count(n[i]))
#         i += 1
#     d1 = dict(zip(n, l))
#     d2 = {k for (k, v) in d1.items() if v == max(l)}
#     print("mode:" + str(d2))
#
# n = [2, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8]
# mean(n)


# l = -1 -2 -3 -4 -5
# l1 = []
# for i in l:
#     l1.append(i)
# print(max(l))


# d = {"MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3, "THURSDAY": 4, "FRIDAY": 5,"SATURDAY": 6, "SUNDAY": 0}
# choice = input()
# n = int(input())
# target_day = d[choice]
# target_day = target_day % 7
# new_day = target_day
# if new_day == 0:
#     print("sunday")
# elif new_day == 1:
#     print("monday")
# elif new_day == 2:
#     print("tuesday")
# elif new_day == 3:
#     print("wednesday")
# elif new_day == 4:
#     print("thursday")
# elif new_day == 5:
#     print("friday")
# else:
#     print("saturday")
#

# ---------------------------------------------------------------------------------------------------------------------

