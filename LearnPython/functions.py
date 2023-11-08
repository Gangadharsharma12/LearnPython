# def calc(a,b):
#     print("The sum is",a+b)
#     print("The difference is",a-b)
#     print("The product is",a*b)
#     print("The dividend is",a/b)
# calc(20,10)
# calc(200,100)
# calc(2000,1000)
# print("TQ")

# def wish():
#     print("HELLO WORLD")
# wish()
# wish()
# wish()
# wish()


# def square(number):
#     print(f"The square root of given {number} is {number**2}")
# number=int(input("Enter any number:"))
# square(number)


# def wish(name):
#     print(f"Hello {name},good morning")
# name=input("enter any name:")
# wish(name)


# def table(number):
#     print("{x}*{z}={y}".format(x=number,z=i,y=number*i))
# number=int(input("enter any number:"))
# for i in range(1,11):
#     table(number)

# def product(a,b):
#     return a*b
# print("The product is",product(10,10))
# print("The product is",product(10,20))


# def fact(n):
#     x = 1
#     while n >= 1:
#         x = x*n
#         n = n-1
#     return x
# for i in range(1, 11):
#     print(f"The factorial of {i} is {fact(i)}")



# def fun(a):
#     x=10
#     print(x)
# a=15
# fun(a)
# print(a)


# def wish(msg,name="guest",):
#     print("Hello",name,msg)
# wish("good morning")
# wish("good morning",name="Gangadhar")
# wish(msg="Gangadhar",name="good morning")
# wish("ravi","good morning")
# wish("good morning","ravi")


# def sum(*n,a,b,c,d):
#     print(n)
#     print(a,b,c,d)
# sum(10,a=20,b=30,c=40,d=50)


# def fun(a=10,b=20):
#     print(a//9)
#     print(a*b)
# fun(a=9,b=2)

# def fun(*a,n):
#     print(n,a)
#     print(a)
# fun(10,20,30,n=40)



# def display(**kwargs):
#     for k,v in kwargs.items():
#         print("{}:{}".format(k,v))
# display(name="Gangadhar",age=24,gf="python",enemy1="tarika",enemy2="ravina",enemy3="pallavi")
#

# def f1(arg1, arg2, arg3=4, arg4=8):  # invalid
#     print(arg1, arg2, arg3, arg4)    # we need to declare values for arg1,arg2
# f1()

# def f1(arg1, arg2, arg3=4, arg4=8):
#     print(arg1, arg2, arg3, arg4)
# f1(10,20)                             # 10,20,4,8


# def f1(arg1, arg2, arg3=4, arg4=8):
#     print(arg1, arg2, arg3, arg4)
# f1(10,20,30,40)                          # 10,20,30,40


# def f1(arg1, arg2, arg3=4, arg4=8):
#      print(arg1, arg2, arg3, arg4)
# f1(25,50,arg4=100)                        # 25,50,4,100


# def f1(arg1, arg2, arg3=4, arg4=8):
#     print(arg1, arg2, arg3, arg4)
# f1(arg4=2,arg1=3,arg2=4)                     # 3 4 4 2


# def f1(*args,args1=20):
#          print(args,args1)
# f1(10,20,30)                                # (10, 20, 30) 20


# def f1(*args, args1=30):
#     print(args, args1)
# f1(10, 20, 30,args1=50)                       #  (10, 20, 30) 50


# def table(n):
#     for i in range(1,11):
#         print(f"{n}*{i}={n*i}")
# table(5)
# print()
# table(10)
# print()
# table(15)
# print()
# table(20)
# print()
# table(25)
# print()
# table(30)


# a=20
# def f1():
#     a=777
#     print("The local variable is:",a)
#     print("The global variable is:",globals()["a"])
#     print("The globals variable is:",globals().get("a"))
# f1()

# def fact(n):
#     if n == 1 or n == 0:
#         return(1)
#     elif (n < 0):
#         print("factorial is undefined")
#     else:
#         n=n*fact(n-1)
#         return n
# n=int(input("Enter any number:"))
# print("The factorial of",n,"is",fact(n))

# x=13
# def san():
#     x=12
# san()
# print(x)

#------------------------------------------------------------------------------------------------------------------------
# def table(n):
#     for x in range(1,11):
#         print(f"{n}*{x}={n*x}")
# print("The multiplication of given number is:")
# table(5)
# print()
# table(6)



# def greetings():
#     print("hello")
# greetings()
# greetings()
# greetings()



# def wish(name,msg):
#     print("hello",name,msg)
# wish("gangadhar","good evening")


# def f1(a,b):
#     return(a+b)
# c=f1(10,20)
# print("the sum is",c)
# print("The sum is",f1(100,200))



# def even_odd(n):
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# even_odd(2)
# even_odd(5)


# def fact(n):
#     x=1
#     while n>=1:
#         x=x*n
#         n=n-1
#     return x
# for i in range(1,11):
#     print(f"The factorial of {i} is {fact(i)}")



# def f1(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     fdiv=a//b
#     return sum,sub,mul,div,fdiv
# x=f1(20,10)
# print(x)

#PA

# def f1(a,b):
#     sum=a+b
#     return sum
# print(f1(20,10))


# def func(name):
#     message="hi"+ name
#     return message
# name=input("enter a name:")
# print("The output of this programm is",func(name))



# def simple(p,t,r):
#     return (p*t*r)/100
# a=float(input("enter a value:"))
# b=float(input("enter a value:"))
# c=float(input("enter a value:"))
# print("The simple intrest is",simple(a,b,c))


# def sum(p,q):
#     sum=a+b
#     return sum            TypeError: sum() missing 1 required positional argument: 'q'
# sum(10)


#KwA

# def f1(name,age):
#     print("Hello,my name is",name,"and my age is",age)
# f1(name="dgs",age=24)

# def f2(p,t,r):
#     return (p*t*r)/100
# x=f2(p=5000,t=3,r=5)
# print(x)

# def f3(name1,name2,name3):
#     print(name1,name2,name3)
# f3(name3="dgs",name2="tsk",name1="trs")


# def f4(name,age=45):
#     print("Hello my name is",name,"and my age is",age)
# f4("dgs")

# def f5(n,*args):
#     print(args)
#     print(n)
# f5(1,2,3,4,5)


# def f5(*args,n):
#     print(args)
#     print(n)
# f5(1,2,3,4,n=5)


# def f6(**kwargs):
#     print(kwargs)
# f6(name="DGS",address="medak",fname="prasad rao",mother_name="sri vani")

#-----------------------------------------------------------------------------------------------------------------------
#recursion:

# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)




# def lcm(a,b,c):
#     c=c+b
#     if c%a==0 and c%b==0:
#         return c
#     else:
#         return lcm(a,b,c)
# num=int(input("enter any number:"))
# num1=int(input("enter any number:"))
# c=0
# print("LCM IS",lcm(num,num1,c))



# def GCD(a,b):
#     if b!=0:
#         return GCD(b,a%b)
#     else:
#         return a
# num=int(input("enter any number:"))
# num1=int(input("enter any number:"))
# print("The GCD of",num,"and",num1,"is:",GCD(num,num1))

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# n=int(input("enter any number:"))
# if n<0:print("sorry,factorial can not be determined")
# elif n==0:print("the factorial of 0 is 1")
# else:print("The factorial of a given number is",fact(n))




# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)
# print(fib(4))
# for i in range(11):
#     print(fib(i),end=" ")


# def double(x):
#     return 2*x
# l=[1,2,3,4,5]
# l1=list(map(double, l))
# print(l1)

# l=[1,2,3,4,5]
# l1=tuple(map(lambda x:x**3,l))
# print(l1)


# x=[1,2,3]
# y=[4,5,6]
# y.append(x)
# print(y)



# a=20
# def f1():
#     a=888
#     print("The local variable",a)
#     print("The global variable",globals().get("a"))
#
# f1()
#

# def argumentFunction(a,b):
#     print(a+b)
# a=int(input(""))
# b=int(input())
# argumentFunction(a,b)


# def  returnValueFunction(n):
#     return 2*n
# n=int(input())
# print(returnValueFunction(n))


# def leap(n):
#     if n%4==0 and n%100 !=100:
#         print(n,"is a leap year")
#     elif n%400==0:
#         print(n,"is a leap year")
#     else:
#         print (n,"is not a leap year")
# n=int(input("enter a year:"))
# leap(n)


# s="hello hai good morning"
# s1=s.replace("good","very good")
# print(s1)


# s={100:1,200:2,300:3}
# print(s.setdefault(400,4))
# print(s)


# a = 10
# b = 20
# c = 30
# d = 40   # Here a,b,c,d are called Global Variable Names
# def   operation():
# 	a = 100
# 	b = 200
# 	c = 300
# 	d = 400   # Here a,b,c,d are called Local Variable Names
# 	res = a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
# 	print("sum of local var vals=",res)
# 	print("=============OR=============")
# 	res = a+b+c+d+globals().get('a')+globals().get('b')+globals().get('c')+globals().get('d')
# 	print("sum of local var vals=",res)
#
# #main program
# operation()
# print(globals())

