# name="gangadhar"
# salary=30000
# age=24
# print("hello {0} your salary is {1} and your age is {2}" .format(name,salary,age))

# print("The float values with sign {:+f}" .format(-123))

# l=[0,1,2,3,4,5,6,7,8,9]
# z=len(l)
# for x in l:
#     print("The element present at positive index {} and negative index {} is {}".format(x,(-z+1),x))
#
# l=[10,20,30,40]
# while len(l) !=0:
#     print(l.pop())
# print(l)


# s=input("enter any string:")
# i=0
# for x in s:
#     print("The character present at positive index {} and negative index {} is {}" .format(i,-len(s)+i,x))
#     i=i=1

# s=input("enter any string:")
# n=len(s)
# i=0
# print("forward direction")
# while i<len(s):
#     print(s[i])
#     i=i+1
# print("backward direction")
# i=-1
# while i>-len(s):
#     print(s[i])
#     i=i-1


# l=eval(input("enter any list:"))
# a=len(l)
# i=0
# while i<len(l):
#     print("The character prresent at positive index {} and negative index {} is {}".format(i,-a+i,l[i]))
#     i=i+1

# l=eval(input("enter main list:"))
# subl=eval(input("select a number from above:"))
# if subl in l:
#     i=l.index(subl)
#     print("{} is first occured at index {}".format(subl,i))
# else:
#     print("The specified number is out of range")


# l=[10,20,30]
# i=40
# l.append(i)
# print(l)


# l=[]
# for x in range(1001):
#     if x%3==0:
#         l.append(x)
# print(l)


# l=eval(input("enter any list:"))
# subl=int(input("select a number from l:"))
# if subl in l:
#           l.remove(subl)
#           print(l)
# else:
#            print("sorry")


# l=eval(input("enter any list:"))
# subl=int(input("select a number from l:"))
# while subl in l:
#     l.remove(subl)
# print(l)


# l=[10,20,30,40,50]
# m=l.pop(2)
# print(l)

# import calendar
# a=int(input("enter any year:"))
# b=int(input("enter any month:"))
# print(calendar.month(a,b))

# integer=10
# float=1.290
# string="gangadhar"
# print("hello,i am integer....my value is %d \nhai,i am float....my value is %f \nhai, my name is %s" %(integer,float,string))




# import random
# x=random.randint(0,100)
# print(x)


# x=int(input("enter the number for which you would like to know the table:"))
# print("please find below for  the table",x)
# for i in range(1,11):
#     print(x, '*', i, '=', x * i)






# bot_name = "dgs"
# birth_year = 1997
# print(f"Hello! my name is {bot_name}")
# print(f"I was created in {birth_year}")






# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')
#
# name = input()
#
# print('What a great name you have, ' + name + '!')
# print('Let me guess your age.')
# print('Enter remainders of dividing your age by 3, 5 and 7.')
# remainder3 = int(input("enter a number:"))
# remainder5 = int(input("enter a number:"))
# remainder7 = int(input("enter a number:"))
# age = age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
# print(f"Your age is {age}; that's a good time to start programming!")






# print('Hello! My name is Aid.')
# print('I was created in 2020.')
# print('Please, remind me your name.')
#
# name = input()
#
# print('What a great name you have, ' + name + '!')
# print('Let me guess your age.')
# print('Enter remainders of dividing your age by 3, 5 and 7.')
#
# rem3 = int(input())
# rem5 = int(input())
# rem7 = int(input())
#
# age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
#
# print("Your age is " + str(age) + "; that's a good time to start programming!")
# print('Now I will prove to you that I can count to any number you want.')
#
# # read a number and count to it here
# count = int(input())
# number = 0
# while number < count:
#     print(number,"!")
#     number += 1
#
# print('Completed, have a nice day!')





# def captain_adder(name):
#     print(name + " Jack Sparrow")
# name = "captain"
# captain_adder(name)



# print("Have you had enough hours of sleep today?")
# answer = input()
# print("Let's drink cocoa!" if answer == "yes" else "I'd recommend a coffee!")

# x = int(input())
# print(True) if x >= 0 else print(False)




# a = 5
# b = 9
# def sum_(x, y):
#    result = x + y
#    print(result)

# def change_city(new_user_city):
#     global user_city
#     user_city = new_user_city
#
# change_city("hyd")
# print(user_city)

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(f"{loan_principal}")
print(f"{first_month}")
print(f"{second_month}")
print(f"{third_month}")
print(f"{final_output}")
