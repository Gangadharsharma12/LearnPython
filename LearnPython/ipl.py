# x=input("please select your favourite IPL team from below and i will provide the captain name")
#
# choice=input("please select your team:")
#
# a="sun risers hyderabad"
# b="punjab kings"
# c="chennai super kings"
# d="delhi capitals"
# e="royal challaengers bengalore"
# f="gujarath titans"
# g="lucknow super gaints"
# h="mumbai indians"
# i="rajastan royals"
# j="kolkatta knight riders"
#
# m="kane williamson"
# n="mayak agarwal"
# o="ravindra jadeja"
# p="rishab pant"
# q="faf duplesis"
# r="hardhik pandya"
# s="KL Rahul"
# t="rohith sharma"
# u="sanju samson"
# v="shreyas iyyar"
#
# if choice=="a":
#     print("your fav IPL team is {} and its captain is {}".format(a,m))
#
# if choice=="b":
#     print("your fav IPL team is {} and its captain is {}".format(b,n))
#
# if choice=="c":
#     print("your fav IPL team is {} and its captain is {}".format(c,o))
#
# if choice=="d":
#     print("your fav IPL team is {} and its captain is {}".format(d,p))
#
# if choice == "e":
#     print("your fav IPL team is {} and its captain is {}".format(e,q))
#
# if choice=="f":
#     print("your fav IPL team is {} and its captain is {}".format(f,r))
#
# if choice=="g":
#     print("your fav IPL team is {} and its captain is {}".format(g,s))
#
#
# if choice=="h":
#     print("your fav IPL team is {} and its captain is {}".format(h,t))
#
# if choice=="i":
#     print("your fav IPL team is {} and its captain is {}".format(i,u))
#
# if choice=="j":
#     print("your fav IPL team is {} and its captain is {}".format(j,v))




#
# # def wish(msg,name="guest"):
# #     print("Hello",name,msg)
# # # wish("good morning")
# # # wish("good morning",name="Gangadhar")
# # wish(msg="Gangadhar",name="good morning")  # Hello good morning Gangadhar
# # wish("ravi","good morning") # Hello good morning ravi
# # wish("good morning","ravi")  # Hello ravi good morning
# # #wish(p1,p2)
# # #wish("abc","dgs")     # Hello dgs abc
# # #wish(name="good morning")  # Hello good morning
#
#
#
# # def price(item,price):
# #     print("The price of the",item,"is:",price)
# # price(20,"sugar")          # The price of the 20 is:sugar
# # price("",50000)                # error
# # price("one plus",50000)    # The price of the one plus is :50000
# # price(50000,item="one plus")    # The price of the 50000 is :one plus
#
# # def swap(a,b):
# #     a,b=b,a
# #     print(a)
# #     print(b)
# # swap(10,20)
# # swap(100,200)
#
#
# #if 5 > 2:print("Five is greater than two!")
#
#
#
# # rainbow = "red, orange, yellow, green, blue, indigo, violet"
# # warm_colors = "red, yellow, orange"
# # my_color = "orange"
# #
# # if my_color in rainbow:
# #     print("Wow, your color is in the rainbow!")
# #     if my_color in warm_colors:
# #         print("Oh, by the way, it's a warm color.")
#
#
# # sound = "music"
# # n_people = int(input())
# # if sound == "music" and n_people > 10:
# #     print("We are at the party!")
#
#
#
# # number = int(input())
# # word = input()
# # if number == 0:
# #     word = word + "s"
# # if number > 1:
# #     word = word + "s"
# # print(number, word)
#
#
# # pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# # apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# # ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# # chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# # omelette = "egg, milk, bacon, tomato, salt, pepper"
# # choice = input()
# # if choice in pasta:
# #     print("pasta time!")
# # if choice in apple_pie:
# #     print("apple pie time!")
# # if choice in ratatouille:
# #     print("ratatouille time!")
# # if choice in chocolate_cake:
# #     print("chocolate cake time!")
# # if choice in omelette:
# #     print("omelette time!")
#
#
#
# number = 0
# while True:
#     while number < 5:
#         print(number)
#         number += 1
#     print('Now, the number is equal to 5')
#     break




# choice = int(input())
# print(choice)
# print(str(choice))


# def func():
#     x = 1
#
#     def inner():
#         x = 2
#         print("func_inner:", x)
#     inner()
#     print("func_outer:", x)

#
# def nonlocal_func():
#     x = 1
#
#     def inner():
#         nonlocal x
#         x = 2
#         print("nonlocal_func_inner:", x)
#     inner()
#     print("nonlocal_func_outer:", x)
#
#
# func()  # inner: 2
#         # outer: 1
#
# nonlocal_func()  # inner: 2
#                  # outer: 2
#
#
#
#
# x = 10 #global
#
#
# def enclosed():
#     x = 20
#     print(x)
#     def minor_local():
#         print('DGS')
#     def local():
#         x = 9
#         print(x)
#     minor_local()
#     local()
#
#
# enclosed()
#

name = "DGS"
def one():
    global name
    name = "DGS"


    def two():
        nonlocal name
        print(name)


        def three():
            name = "sharma"
            print(name)
one()


# x = "global"
# def outer():
#     x = "outer local"
#     def inner():
#         x = "inner local"
#         def func():
#             x = "func local"
#             print(x)
#         func()
#     inner()
#
# outer()  # "func local"




# x = 1
# def print_global():
#     print(x)
#
# print_global()  # 1
#
#
# x = 2
# def modify_global():
#
#     # global x
#     x = 10
#     x = x + 1
#     print(x)
#     y = 9
#     y -= 1
#
# modify_global()

# count1 = int(input())
# count2 = int(input())
# count3 = int(input())
# max = (True if count1 < count2 and count2 < count3 else False)
# print(max)



# place `import` statement at top of the program
from string import capwords


# don't modify this code or the variable may not be available
# input_string = capwords(input())
# print(input_string)


# price = int(input())# there should be some int value
# if price > 5000: # 5001 t0 n
#     print("That's too expensive!")
# elif price > 500: # 501 to 5000
#     print("I can afford that!")
# else: # less than 500
#     print("That's too cheap!")


# animal = 'unicorn'
# if animal in 'crow, dog, frog, pony,unicorn':
#     print('This animal exists')
# if animal in 'unicorn, pegasus, pony':
#     print('This animal is a horse')


# # nested elif example
# traffic_lights = "green, yellow, red"
# # a string with one color
# light = input()  # variable for color name
# if light in traffic_lights:
#     if light == "green":
#         print("You can go!")
#     elif light == "yellow":
#         print("Get ready!")
#     else:
#         # if the lights are red
#         print("Just wait.")
# else:
#     print("No such traffic light color, do whatever you want")




# A = int(input())
# B = int(input())
# H = int(input())
#
# if A < H and B > H:
#     print("Normal")
# if A < B and H > B:
#     print("Excess")
# if H < A and H < B:
#     print("Deficiency")



# min_sleep = int(input())
# max_sleep = int(input())
# curr_sleep = int(input())
#
# if curr_sleep < min_sleep:
#     print("Deficiency")
# elif curr_sleep > max_sleep:
#     print("Excess")
# else:
#     print("Normal")





# input_1 = input()
# input_2 = input()
# if input_1 == "1/2" and input_2 == "-1/3":
#     print("Strange", "Quark")
# elif input_1 == "1/2" and input_2 == "2/3":
#     print("Charm", "Quark")
# elif input_1 == "1/2" and input_2 == "-1":
#     print("Electron", "Lepton")
# elif input_1 == "1/2" and input_2 == "0":
#     print("Neutrino",  "Lepton")
# elif input_1 == "1" and input_2 == "0":
#     print("Photon ", "Boson")



# x = int(input())
# if x > 1000:
#     print("!")
# elif x > 500:
#     print("@")
# else:
#     if x > 250:
#         print("#")
#     else:
#         print("$")



# time_spent = int(input())
# if time_spent < 2:
#     print("That's rare nowadays!")
# elif 2 <= time_spent < 4:
#     print("This seems reasonable")
# else:
#     print("Don't forget to take breaks!")


# students_score = int(input())
# max_score = int(input())
# percentage = (students_score / max_score) * 100
# if 90 <= percentage <= 100:
#     print('A')
# elif percentage > 80:
#     print('B')
# elif percentage > 70:
#     print('C')
# elif percentage > 60:
#     print('D')
# elif percentage < 60:
#     print('F')



# import math
# a = int(input())
# b = int(input())
# c = int(input())
# P = (a + b + c) / 2
# S = math.sqrt(P * (P - a) * (P - b) * (P - c))
# print(S)


# from math import sqrt, pow
# a = int(input())
# octa = 2 * sqrt(3) * pow(a, 2)
# vol = 1 / 3 * sqrt(2) * pow(a, 3)
# print(round(octa, 2),end =" " )
# print(round(vol, 2))

# import math
# deg = float(input())
# abc = math.cos(deg)
# def_ = math.sin(deg)
# print(def_ - abc)

from math import e
input_ = int(input())
output_ = pow(e, input_) / (pow(e, input_) + 1)
print(output_)
