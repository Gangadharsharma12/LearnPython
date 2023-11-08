#print("Hello python!")



# import sys
# print("""
# 1.addition
# 2.subtraction
# 3.Multiplication
# 4.Division
# """)
# print("please select an option from above")
# option=int(input())
# while option>4:
#     print("out of range")
#     sys.exit()
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if option==1:
#     sum=a+b
#     print("The addition of {} and {} is {}".format(a,b,sum))
# if option==2:
#     difference=a-b
#     print("The difference of {} and {} is {}".format(a,b,difference))
# if option==3:
#     product=a*b
#     print("The product of {} and {} is {}".format(a,b,product))
# if option==4:
#     division=a/b
#     print("The division of {} and {} is {}".format(a,b,division))
# print("TQ")

#WAP TO FIND AREA OF TRIANGLE

# a=int(input("enter the base of triangle:"))
# b=int(input("enter the height of triangle:"))
# aot=1/2*a*b
# print("The area of triangle is",aot)


#WAP TO SOLVE QUADRATIC EQUATION

# import cmath
# print("The general form of quadractic equation is: ax2+bx+c")
# a=int(input("enter a(a != 0):"))
# b=int(input("enter b:"))
# c=int(input("enter c:"))
# d=(b**2)-(4*a*c)
# sol1=(-b-cmath.sqrt(d))/2*a
# sol2=(-b+cmath.sqrt(d))/2*a
# if d>0:
#     print("valuses are distinct")
# elif d==0:
#     print("values are equal")
# elif d<0:
#     print("values are complex")
# print(f"The solutions are {sol1} and {sol2}")


#WAP TO SWAP TWO NUMBERS WITHOUT USING THIRD VARIABLE
# print("The elements before swapping:")
# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# choice=a
# a=b
# b=choice
# print("The variables after swapping")
# print(f"The value of a is {a}")
# print(f"The value of b is {b}")


#WAP TO PRINT A RANDOM NUMBER
# import random
# l=[]
# for x in range(1,10):
#     n=random.randint(100,200)
#     l.append(n)
# print(l)

#WAP TO DISPLAY CALENDAR
# import calendar
# a=int(input("enter a year:"))
# b=int(input("enter any month:"))
# print(calendar.month(a,b))


#WAP TO CHECK WHETHER THE GIVEN NUMBER IS POSITIVE OR NEGATIVE OR ZERO

# n=int(input("enter a number:"))
# if n<0:
#     print("The given value {} is {}".format(n,"negative"))
# if n>0:
#     print("The given value {} is {}".format(n, "positive"))
# if n==0:
#     print("The given value {} is {}".format(n, "equal to zero"))


#WAP TO CHECK WHETHER THE NUMBER IS EVEN OR ODD

# n=int(input("enter a number:"))
# if n%2==0:
#     print("The number is {}".format("even"))
# else:
#     print("The number is {}".format("odd"))


#WAP TO CHECK LEAP YEAR
# l=int(input("enter a year:"))
# if (l%4==0 and l%100 !=0):
#     print("It is a leap year")
# elif(l%400==0):
#     print("it is a leap year")
# else:
#     print("not a leap year")


#WAP TO CHECK PRIME NUMBER:

# n=int(input("enter a number:"))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count=count+1
#         break
# if count==0:
#     print("The number is a prime number")
# else:
#     print("The number is not a prime number")

#WAP TO PRINT PRIME NUMBERS IN A RANGE

# a=int(input("enter lower value:"))
# b=int(input("enter upper value:"))
# print("The primes in given range are:")
# for x in range(a,b+1):
#     if x>1:
#         for i in range(2,x):
#             if x%i ==0:
#                 break
#         else:
#             print(x)


#WAP TO FIND THE FACTORIAL OF A NUMBER

# n=int(input("enter a number:"))
# i=1
# for x in range(1,n+1):
#     i=i*x
# print(i)


#WAP TO PRINT FIBNACOI SERIES

# a=int(input("enter a number:"))
# if a==0:
#     print(1)
# elif a==1:
#     print(1)
# else:
#     print(1,1,end=" ")
#     x=1
#     y=1
#     for i in range(2,a+1):
#         z=x+y
#         print(z,end=" ")
#         x=y
#         y=z


#WAP TO PRINT A TABLE OF A NUMBER:

# n=int(input("enter a number:"))
# for x in range(1,11):
#     print(n,"*",x,"=",n*x)

#WAP TP PRINT THE GIVEN NUMBER IS ARMSTRONG OR NOT

# n=int(input("enter a number:"))
# x=n
# m=str(n)
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r**len(m)
#     n=n//10
# if sum==x:
#     print(f"The given number {x} is an Armstrong number")
# else:
#     print("Not an Armstrong number")


# a = int(input("enter lower value:"))
# b = int(input("enter upper value:"))
# print("The primes in given range are:")
# for x in range(a, b+1):
#     if x >= 1:
#         for i in range(2, x):
#             if x % i == 0:
#                 break
#         else:
#             print(x)


print(2**3**4)