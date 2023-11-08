# p=1
# n=int(input("enter a value:"))
# for i in range(n):
#     for j in range(i+1):
#         print(p, end = " ")
#         p=p+1
#     print()



# s=[10,20,30,40]
# a=len(s)
# sum=0
# for x in s:
#     sum=sum+x
# print(sum)
# print(sum/a)



# n=eval(input("enter any list:"))
# l=[]
# for x in n:
#     if x not in l:
#         l.append(x)
# print(n)
# print(l)


# i=0
# d=dict()
# while i<26:
#     d[chr(97+i)]= 1+i
#     i=i+1
# while len(d) !=0:
#     print("deleting item is:",d.popitem())
# print(d)


#WAP TO TAKE DICT FROM KEYBOARD AND PRINT THE SUM OF VALUES

# n=eval(input("enter your dictionary:"))
# sum=0
# for x in n.values():
#     sum=sum+x
# print("the sum is:", sum)




# n=input("enter any string:")
# d=dict()
# v={"a","e","i","o","u"}
# for x in n:
#     if x in v:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#          print("{} occurs {} times" .format(k,v))



# n=input("enter any string:")
# d=dict()
# for x in n:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print("{} occures {} times" .format(k,v))



# n=input("enter any string:")
# d=dict()
# for x in n:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# for k,v in sorted(d.items()):
#     print("{} occures {} times" .format(k,v))




# n=int(input("enter the count of students:"))
# d=dict()
# for x in range(n):
#     name=input("please enter student name:")
#     marks=int(input("please enter student marks:"))
#     d[name]=marks
# print("All the students data inserted")
# while True:
#     result=input("enter a student name to display marks:")
#     if result in d:
#         print("The marks of {} is {}".format(result,d.get(result)))
#     else:
#         print("invalid name choosen")
#     option=input("do you want to find any other students marks {YES|NO}")
#     while option.lower() not in {"yes","no"}:
#         option=input("invalid option selected....please select a valid option from {YES|NO}:" )
#     if option.lower() in {"no"}:
#         break
# print("Thank you durga sir")



# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)



# print("""
# * * * *
# *     *
# *     *
# * * * *
#
#
# """)


# print('''
#
# O X X
# O X O
# X O X
#
# ''')

# print( 'This code is not good.')
# print("No. It's still not good!")
# print('Maybe  try  one  more  time? ')
# print('Almost there!')
# print('Okay, this one looks fine. :')
#
#
#
#
# print ('Always write beautiful code!')
#
# print ('Always write beautiful code!')





# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#               print(i,j,k)

# i=0
# while i<3:
#         print(5, " * ", i ,"=", 5*i)
#         i=i+1
#


# i=0
# while i<5:
#     print("geeks for geeks")
#     i=i+1



# m=int(input("enter a number:"))
# n=int(input("enter the limit:"))
# for i in range(1,n+1):
#      print(m*i)


# n=int(input("enter the number:"))
# l=[]
# for i in range(1,n+1):
#      if n%i==0:
#           l.append(i)
# print(l[1])

# n=int(input("enter the number:"))
# for x in range(2,n+1):
#      if n%x==0:
#           print(x)
#           break


# n=int(input("enter the number:"))
# i=2
# while i<=n:
#      if n%i==0:
#           print(i)
#           break
#      i=i+1


# i=1
# while i<=5:
#      if i==3:
#           break
#      print(i)
#      i=i+1
# print(i)





# n=int(input("enter a number:"))
# i=1
# while i<n:
#      if n-i==5:
#           continue
#      print(i)
#      i=i+1




# l=[10,16,17,18,19,15]
# a=[]
# for x in l:
#      if x%5 != 0:
#           a.append(x)
# print(a)


# i=0
# while i<=5:
#      if i ==3:
#           i=i+1
#           continue
#      print(i,i*i)
#      i=i+1




# for x in range(1,11):
#      for y in range(1,11):
#           print(x*y,end=" ")
#      print()



# for i in range(1,3):
#      j=1
#      while j<3:
#              print(i,j)
#              j=j+1
#      print("gfg")



# l1=[[10,20,30],[40,50,60],[70,80,90]]
# for x in l1:
#      for y in x:
#           print(y,end=" ")
#      print()


# n=int(input("enter any number:"))        *  *  *  *
# for i in range(n):                       *  *  *  *
#      for j in range(n):                  *  *  *  *
#           print("*",end=" ")             *  *  *  *
#      print()                             *  *  *  *



# n=int(input("enter any number:"))             *
# for i in range(n):                            *  *
#      for j in range(i+1):                     *  *  *
#           print("*",end=" ")                  *  *  *  *
#      print()                                  *  *  *  *  *


# n=int(input("enter any number:"))             * * * * *
# for i in range(1,n+1):                        * * * *
#      for j in range(1,n+2-i):                 * * *
#           print("*",end=" ")                  * *
#      print()                                  *



# n=int(input("enter any number:"))
# for i in range(n):
#      for j in range(n-i-1):
#           print(" ",end=" ")
#      for k in range(2*i+1):
#           print("*",end=" ")
#      print()


# n=int(input("enter any number:"))
# for i in range(n):
#      for j in range(n):
#           for k in range(n):
#                    print(i,j,k)



# n=int(input("enter any number:"))
# result=0
# while n>0:
#        n=n//10
#        result=result+1
# print("The count is",result)


# n=int(input("enter any number:"))
# x=1
# for i in range(2,n+1):
#      x=x*i
# print("The factorial is",x)


# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# small=min(a,b)
# for i in range(1,small+1):
#      if (a%i==0 and b%i==0):
#                gcd=i
# print("The gcd of two numbers is",gcd)


# import math
# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# c=math.gcd(a,b)
# print("The gcd is",c)


# import calendar
# a=int(input("enter any year:"))
# b=int(input("enter any month:"))
# print(calendar.month(a,b))


# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# c=max(a,b)
# while (c<=a*b):
#     if (c%a==0 and c%b==0):
#            break
#     c=c+1
# print("The lcm is",c)

# import math
# a=int(input("enter any number:"))
# b=int(input("enter any number:"))
# gcd=math.gcd(a,b)
# lcm=(a*b)/gcd
# print("The lcm is",int(lcm))


# a = int(input("enter any number:"))
# if a==0:
#     print(1)
# elif a==1:
#         print(1)
# else:
#     print("The fibnaoic series of a given number is",1,1,end=" ")
#     x=1
#     y=1
#     for i in range(2,a+1):
#         z=x+y
#         print(z,end=" ")
#         x=y
#         y=z


# a = int(input("enter any number:"))
# if a<=1:
#     print("no")
# else:
#     for i in range(2,a):
#         if(a%i==0):
#             print("no")
#             break
#     else:
#             print("yes")



# n=int(input("enter a number:"))
# l=[]
# for i in range(1,n):
#     if n%i==0:
#         l.append(i)
# print('All the possible divisors of', n, "are",l)


# n = int(input("enter a number:"))
# i=1
# while i<=n:
#     if n%i==0:
#         i=i+1
#         continue
#     print(i,end=" ")
#     i=i+1


# n = int(input("enter a number:"))
# i=1
# while i*i<n:
#     if n%i==0:
#         print(i)
#         print(int(n/i))
#     i=i+1
# if i*i==n:
#     print(i)



# n = int(input("enter a number:"))
# if n==1:
#     print("no")
# else:
#     x=2
#     while x*x<=n:
#         if n%x==0:
#             print("no")
#             break
#         x=x+1
#     else:
#         print("yes")


# import sys
# print(""" please select an operation:
# 1.addition
# 2.subtraction
# 3.multiplication
# 4.division
# 5.Modulus
# 6.floor division
# """)

# choice=int(input("please select any operation from above:"))
# if choice>=6:
#             print("invalid")
#             sys.exit()
# n=int(input("enter a number:"))
# m=int(input("enter a number:"))
# if choice==1:
#     print(n+m)
# elif choice==2:
#     print(n-m)
# elif choice==3:
#     print(n*m)
# elif choice==4:
#     print(n/m)
# elif choice==5:
#     print(n%m)
# else:
#     print(n//m)


# a=int(input("enter a number:"))
# b=int(input("enter a second number:"))
# c=max(a,b)
# while c<=a*b:
#     if(c%a==0 and c%b==0):
#         break
#     c=c+1
# print(c)

