# WAP To REVERSE THE GIVEN INTEGER

# x = int(input())
# rev_n = 0
# while x > 0:
#     v = x % 10
#     rev_n = (rev_n * 10) + v
#     x = x // 10
# print(rev_n)


# WAP TO GENERATE FACTORIAL NUMBERS CONTINUOUSLY TILL THE GIVEN NUMBER

# import time
# n = int(input())
# fact = 1
# i = 1
# while True:
#     if n > 0:
#         fact = fact * n
#         print("The factorial of %d is %d" % (n, fact))
#         n = n + 1
#         i = i + 1
#         if n > 10:
#             break
#         else:
#             time.sleep(1)



# A = int(input())
# l = []
# for i in range(1, A + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         l.append("FizzBuzz")
#     elif i % 3 == 0:
#         l.append("Fizz")
#     elif i % 5 == 0:
#         l.append("Buzz")
#     else:
#         l.append(i)
# print(l)


# class Solution:
#     def __init__(self, leap):
#         self.leap = leap
#         self.solve()
#
#     def solve(self):
#         if self.leap % 4 == 0  and self.leap % 100 != 0:
#             print("1")
#         elif self.leap % 400 == 0:
#             print("1")
#         else:
#             print("0")
# n = int(input())
# s = Solution(n)


# class Solution:
#     def __init__(self,a):
#         self.A = a
#         self.m1()
#
#     def m1(self):
#         l = []
#         for i in range(1, self.A + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 l.append("FizzBuzz")
#             elif i % 3 == 0:
#                 l.append("Fizz")
#             elif i % 5 == 0:
#                 l.append("Buzz")
#             else:
#                 l.append(i)
#         print(l)
#
# s = Solution(20)



# for i in range(1,6):
#     for j in range(1, 6):
#         print(f"i {i} j {j}")
#     print()
# print(370%10)


#  DOUBT IN COUNT():
# str = "ab bc ca de ed ad da ab bc ca"
# oc = str.count('')
# print(oc)
# print(len(str))



# REAL TIME EXAMPLE FOR ENDSWITH()
# print("checking the user is a valid user or not")
# choice = input("please enter your mail id")
# if choice.endswith("@gmail.com"):
#     print("valid mail id")
# else:
#     print("invalid mail id")



# print("I designed this rhyme to explain in due time\nAll I know")
# print("Time is a \tvaluable thing")
# print("Watch it fly by\\as the pendulum swings")


# n = "!!!!!!abc@12345!a!b!cbcaabacac"
# print(n.strip("!abcd"))
# ---------------------------------------------------------------------------------------------------------------------

# 46

# def employee_check(work_hours):
#     max_work_hour = 0
#     employee_name = " "
#     for employee, hour in work_hours:
#         if hour > max_work_hour:
#             max_work_hour = hour
#             employee_name = employee
#     return max_work_hour, employee_name
#
#
# work_hours = [("ABC", 100), ("DEF", 800), ("GHI", 750), ("JKL", 900)]
# x, y = employee_check(work_hours)
# print(f"The best employee award goes to employee {y} who worked {x} hours in this week")

# ---------------------------------------------------------------------------------------------------------------------

# 47


# from random import shuffle
#
#
# def shuffle_list(my_list):
#     shuffle(my_list)
#     return my_list
#
#
#
# def player_guess():
#     guess = input("pick a number from 0,1 or 2:")
#     while guess not in ["0", "1", "2"]:
#         guess = input(f"pick a number from {int(0)},{int(1)} or {int(2)} only: ")
#     return int(guess)
#
#
# def check_guess(my_list, guess):
#     if my_list[guess] == "O":
#         print("Correct Guess!")
#     else:
#         print("OOPS!! Wrong guess")
#         print(my_list)
#
# my_list = [" ", "O", " "]
# mixed_list = shuffle_list(my_list)
# guess = player_guess()
# check_guess(mixed_list, guess)
# ---------------------------------------------------------------------------------------------------------------------

# def my_func(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
# print(my_func(2,4))
# print((my_func(7, 5)))




# def animal_crackers(text):
#     l = text.split()
#     if l[0][0] == l[1][0]:
#         return True
#     else:
#         return False
# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))



# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20 or n1+n2 == 20:
#         print("True")
#     else:
#         print("False")
#
# makes_twenty(20,10)
# makes_twenty(12,8)
# makes_twenty(2,3)


# def old_macdonald(name):
#     d = {}
#     for i in range(0, len(name)):
#         d[i+1] = name[i]
#
#     for each in d:
#         if each == 1 or each == 4:
#             print(d[each].upper(), end="")
#         else:
#             print(d[each], end="")
# old_macdonald('macdonald')




# def master_yoda(text):
#     l = text.split()
#     l1 = l[::-1]
#     l2 = " ".join(l1)
#     print(l2)
#
# master_yoda('I am home')
# master_yoda('We are ready')


# def almost_there(n):
#     print(abs(100 - n) <= 10 or (abs(200 - n) <= 10))
# almost_there(90)
# almost_there(104)
# almost_there(150)
# almost_there(209)



# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#             if nums[i] == 3 and  nums[i + 1] == 3:
#                 return True
#     return False
#
# print(has_33([1, 2, 3]))




# def paper_doll(text):
#     for each in text:
#         print(each * 3, end="")
#     print()
# paper_doll('Hello')
# paper_doll(' ')




# def blackjack(a,b,c):
#     if a + b + c <= 21:
#         return a + b + c
#     else:
#         if a == 11 or b == 11 or c == 11:
#             total = a + b + c
#             return total - 10
#         else:
#             if a+b+c > 21:
#                 return "BUST"
#
#
# print(blackjack(5, 6, 7))
# print(blackjack(9, 9, 9))
# print(blackjack(9, 9, 11))





# def summer_69(arr):
#     l = []
#     for number in arr:
#         if 6 <= number <= 9:
#             continue
#         elif arr == l:
#             return 0
#         else:
#             l.append(number)
#     print(sum(l))
# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])
# summer_69([])


# def count_primes(num):
#     l = []
#     for i in range(2, num):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
#     print(len(l))
# count_primes(100)



# def spy_game(nums):
#     for i in range(len(nums) - 2):
#         if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
#             return True
#     else:
#         return False
#
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1, 0, 2, 4, 0, 7, 0]))

# ----------------------------------------------------------------------------------------------------------------------

# import math
# def vol(rad):
#     return (4/3) * math.pi * (rad ** 3)
# print(vol(2))



# def ran_check(num,low,high):
#     flag = False
#     for i in range(low, high+1):
#         if num == i:
#             print(f"{num} is in the range between {low} and {high}")
#             print("True")
#             flag = True
#     else:
#         if flag == False:
#             print(f"{num} is not in the range between {low} and {high}")
#             print("False")
#
# ran_check(5,2,7)
# ran_check(101, 1, 10)




# def up_low(s):
#     l = []
#     l1 = []
#     for each in s:
#         if each.isupper():
#             l.append(each)
#         else:
#             if each.islower():
#                 l1.append(each)
#     print(f"The total number of upper characters in {s} are {len(l)} and the are", end=" ")
#     print(l)
#     print(f"The total number of lower characters in {s} are {len(l1)} and they are", end=" ")
#     print(l1)
#
# up_low("Hello Mr. Rogers, how are you this fine Tuesday?")




# def unique_list(lst):
#     return list(set(lst))
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# i = 1
# def multiply(numbers):
#     for each in numbers:
#         global i
#         i = each * i
#     return i
# print(multiply([1,2,3,-4]))



# def palindrome(s):
#     s = s.replace(" ", "")
#     if s.lower() == s[::-1].lower():
#         print('palindrome')
#     else:
#         print("not a palindrome")
#
#
# palindrome('NuR s e s r u n')




# def panagram(s):
#     alphabets = "abcdefghijklmnopqrstuvwxyz"
#     alpha_set = set(alphabets)
#     s = s.replace(" ", "")
#     s = s.lower()
#     s = set(s)
#     if s == alpha_set:
#         print("Panagram")
#     else:
#         print("not a panagram")
# panagram("The quick brown fox jumps over the lazy DOG")

# ---------------------------------------------------------------------------------------------------------------------
# calling parent class constructor by using class name in child class
# class Animal:
#     def __init__(self, name, gender):
#         print("Hello i am a Animal")
#         self.name = name
#         self.gender = gender
#     def eat(self):
#         print("Hello i am eating")
#     def sleep(self,name):
#         print("Hello i am sleeping")
#         print(f"{name} is sleeping")
#
# class Dog(Animal):
#     def __init__(self, name, gender):
#         Animal.__init__(self, name, gender)
#         print("Hello i am a dog")
#         print(f"hello my name is {self.name}")
#         print(f"i am {self.gender}")
#         super().eat()
#         super().sleep("dgs")
#
# my_dog = Dog("bunny", "male")

# ---------------------------------------------------------------------------------------------------------------------
# calling parent class constructor by using super() in child class

# class Animal:
#     def __init__(self, name, gender):
#         print("Hello i am a Animal")
#         self.name = name
#         self.gender = gender
#
#     def eat(self):
#         print("Hello i am eating")
#     def sleep(self):
#         print("Hello i am sleeping")
#
# class Dog(Animal):
#     def __init__(self, name, gender):
#         super().__init__(name, gender)
#         print("Hello i am a dog")
#         print(f"hello my name is {self.name}")
#         print(f"I am {self.gender}")

# my_dog = Dog("bunny", "Male")

# ---------------------------------------------------------------------------------------------------------------------

# when child class is not having constructor then automatically parent class constructor is executed
# class Animal:
#     def __init__(self):
#         print("Hello i am an Animal")
#
#     def eat(self, name, age):
#         print("Hello i am eating")
#         self.name = name
#         self.age = age
#
# class Dog(Animal):
#     def method(self, name, age):
#         Animal.__init__(self)
#         super().eat(name, age)
#         print(self.name)
#         print(self.age)
#
# d = Dog()
# d.method("DGS", 24)

# ----------------------------------------------------------------------------------------------------------------------

# class Line:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def Distance(self):
#         x1, y1 = self.a
#         x2, y2 = self.b
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
#     def Slope(self):
#         x1, y1 = self.a
#         x2, y2 = self.b
#         return (y2 - y1) / (x2 - x1)
#
# l = Line((3, 2), (8, 10))
# print(l.Distance())
# print(l.Slope())







# class Cylinder:
#     def __init__(self, height, radius):
#         self.radius = radius
#         self.height = height
#     def Vol(self):
#         return self.height * 3.14 * (self.radius) ** 2
#     def Surface_area(self):
#         top = 3.14 * (self.radius) ** 2
#         return (2 * top) + (2 * 3.14 * self.radius * self.height)
#
# c = Cylinder(2, 3)
# print(c.Vol())
# print(c.Surface_area())




# class Account:
#     balance = 100
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         print(f"Account owner:{self.owner}")
#         print(f"Account balance:${self.balance}")
#     def deposit(self,number):
#         self.balance += number
#         print("Deposit Accepted")
#     def withdraw(self,number):
#         if self.balance - number >= 100:
#             self.balance -= number
#             print("Withdrawl Accepted")
#         else:
#             print("Funds Unavailable!")
#
# acct1 = Account("jose", 100)
# print(acct1.owner)
# print(acct1.balance)
# acct1.deposit(5000)
# acct1.withdraw(75)
# acct1.withdraw(15000)
#----------------------------------------------------------------------------------------------------------------------

# __name__ == "__main__"
# def func():
#     print("FUNC() IN UDEMY.PY")
#
# print("TOP LEVEL IN UDEMY.PY")
# print(__name__)
# if __name__ == "__main__":
#     func()
#     print("UDEMY.PY IS  RUNNING DIRECTLY")
# else:
#     print("UDEMY.PY HAS BEEN IMPORTED!")
# ----------------------------------------------------------------------------------------------------------------------

# def mul(a, b):
#     return a * b
# print(__name__)
# if __name__ == "__main__":
#     print(mul(10, 20))
#     print(__name__)

# ---------------------------------------------------------------------------------------------------------------------
# def f1():
#     print("123")
# def f2():
#     print("456")
# def f3():
#     print("789")
# def f4():
#     print("101112")
# print(__name__)
# if __name__ == "__main__":
#     f1()
#     f2()
#     f3()
#     f4()
# ---------------------------------------------------------------------------------------------------------------------


# Generators

# def prime(n):
#     for i in range(2, n):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             yield i
# v = prime(10)
# print("the prime numbers between 1 and 10 are")
# for each in v:
#     print(each)


# try:
#     def simple_gen():
#         for x in range(3):
#             yield x
#     g = simple_gen()
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration:
#     print("Range finished...no value to print")


# def gensquares(N):
#     for x in range(N):
#         yield  x * x
# g = gensquares(10)
# for each in g:
#     print(each)



# import random
# def rand_num(low, high, n):
#     for x in range(n):
#         yield random.randint(low, high)
# g = rand_num(1, 10, 12)
# for each in g:
#     print(each)

# ---------------------------------------------------------------------------------------------------------------------

# 103 Introduction to advance pythonmodules
# notes written in pink binding book shri: side
# import os
# os.rename("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\New folder", "dgs")
# print("rename")

#  DEFINING OUR OWN EXCEPTION
# class DgsDivisionError(BaseException):
#     pass



# l = [1, 2, 3]
# l1 = [4, 5, 6]
# l2 = [7, 8, 9]
# l3 = zip(l, l1, l2)
#
# for each in l3:
#     print((each[0] * each[1]) % each[2])



# n = int(input("enter the max number to get factorial:"))
# for i in range(1, n+1):
#     fact = 1
#     for j in range(1, i+1):
#         fact = fact * j
#     print(f"the factorial of {i} is {fact}")


# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             print(f"{i} is not a prime number because it divides with {j}")
#             break
#     else:
#         print("------------------------------------------------------")
#         print(f"{i} is a prime number because it dont have any factors")
#         print("------------------------------------------------------")



# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
# print(fun(fun(2)) + 1)


# def any():
#     print(var + 1)
# var = 1
# any()
# print(var)


# def func_1(a):
#     return a ** a
# def func_2(a):
#     return func_1(a) * func_1(a)
# print(func_2(2))


# def func(a, b):
#     return a ** a
# print(func(2))


# def fun(x):
#     global y
#     y = x * x
#     return y
#
# fun(2)
# print(y)


# my_list = ["mary", "had", "a", "little", "lamb"]
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = "ram"
# print(my_list(my_list))


# d = {"one": "two", "three": "one", "two": "three"}
# v = d["one"]
# for k in range(len(d)):
#     v = d[v]
# print(v)


# d = {}
# l = ["a", "b", "c", "d"]
# for i in range(len(l) - 1):
#     d[l[i]] = (l[i],)
#
#
# for i in sorted(d.keys()):
#     k = d[i]
#     print(k[0])


# ----------------------------------------------------------------------------------------------------------------------

game_list = [0, 1, 2]
def display_game(game_list):
    print("Here is the game list:")
    print(game_list)
# display_game(game_list)


def position_choice():
    while True:
        l = [0, 1, 2]
        user_choice = input("pick a position to replace (0, 1, 2):")
        if user_choice.isdigit():
            flag = True
            for i in range(3):
                if user_choice == str(i):
                    return int(user_choice)

            if flag == True:
                    print("sorry, invalid choice! ")
        else:
            print("sorry, invalid choice! ")
# position_choice()



def replacement_choice(game_list, position):
    user_placement = input("type a string to replace the position:")
    game_list[position] = user_placement
    return game_list

# replacement_choice(game_list, 1)



def gameon_choice():
    while True:
        choice = input("keep playing [yes | no]: ")
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            if choice != ["yes" or "no"]:
                print("sorry i did not understand.please choose yes or no")
# gameon_choice()


game_on = True
while game_on:
    display_game(game_list)
    position = position_choice()
    updated_list = replacement_choice(game_list, position)
    display_game(updated_list)
    game_on = gameon_choice()
