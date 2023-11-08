# EX:1 Calling the inner function from outside of function
# def outer():
#     print("outer function execution")
#     def inner():
#         print("Inner function execution")
#     print("Outer function is returning inner function")
#     return inner
#
#
# new = outer()
# new()


# EX:2 passing single argument to the function
# def f1(func):
#     print(f"f1 function got {func} as an argument")
#     print(id(func))
#     func()
#
# def fx():
#     print("fx function")
#
# def fy():
#     print("fy function")
#
#
# f1(fx)
# print(id(fx))
# f1(fy)
# print(id(fy))


# EX:3 passing multiple arguments to the function
# def func(f1, f2):
#     f1()
#     print("dgs")
#     f2()
#
# def f1():
#     print("f1 function")
#
# def f2():
#     print("f2 function")
#
# func(f1, f2)


#EX:4

# def fun_1():
#     print("hello i am function 1")
#
# def fun_2(fun_1):
#     print("hello i am function 2 and now i am calling function 1")
#     return fun_1()
#
# x = fun_2(fun_1)
# ---------------------------------------------------------------------------------------------------------------------
# def decor(func):
#     def inner(x, y):
#         print("The multiplication of {} and {} is:".format(x, y), end="")
#         func(x, y)
#     return inner
#
# @decor
# def product(a, b):
#     print(a * b)
#
# product(5, 4)
# -----------------------------------------------------------------------------------------------------------------------
# Actual examples: 114
# EX:1
# def decor(func):
#     def inner():
#         print("Please follow some healthy tips")
#         print("so that you look beautifully")
#         print()
#     return inner
#
# @decor
# def display():
#     print("Showing the person as ususally")
#
# display()
# display()
# display()


# EX:2
# def decor(func):
#     def inner(x, y):
#         if y == 0:
#             print("sorry we can not divide the number by zero")
#         else:
#             return func(x, y)
#     return inner
#
# @decor
# def division(a, b):
#     a,b = b, a
#     print(a / b)
#
# division(20,10)
# division(10, 0)


# EX:3
# def decor_add(self):
#     def inner(x, y):
#         print("$" * 35)
#         print("The addition of {} and {} is:".format(x, y), end=" ")
#         self(x, y)
#         print("$" * 35, "\n")
#     return inner
#
# @decor_add
# def add(a, b):
#     print(a + b)
#
#
# add(10, 20)
# add(15, 30)


# EX:4
# def decor_greet(func):
#     def inner(name):
#         vip = ["DGS", "TSK", "TRS", "BJP", "TDP"]
#         if name in vip:
#             print("Hello {}.How are you?.Thanks for coming".format(name))
#         else:
#             func(name)
#     return inner
#
# @decor_greet
# def greet(name):
#     print("hello", name)
#
# greet("Durga")
# greet("efce")
# greet("fsfeef")
# greet("DGS")
# greet("TRS")

# ----------------------------------------------------------------------------------------------------------------------
# 115
# EX:1

# def decor(func):
#     def inner(x, y):
#         if y == 0:
#             print("sorry we can not divide the number by zero")
#         else:
#             return func(x, y)
#     return inner
#
# @decor
# def division(a, b):
#     a, b = b, a
#     print(a / b)
#
# @decor
# def moduloo(a, b):
#     a, b = b, a
#     print(a % b)
#
# division(20,10)
# division(10, 0)
# moduloo(20, 10)
# moduloo(20, 0)
# ---------------------------------------------------------------------------------------------------------------------

# EX:1 HOW TO CALL SAME FUNCTION WITH AND WITHOUT DECARATOR
# def decor(func):
#     def inner(name):
#         if name == "DGS":
#             print("Hello {}. very very good morning".format(name))
#         else:
#             func(name)
#     return inner
#
#
#
# def wish(name):
#     print("Good morning", name)
# d = decor(wish) [the retuned statement is comming here.so we assigned variable d to call decor function]
# wish("DGS")
# wish("TRS")
# d("TRS")
# d("DGS")



# EX:2
# def upper_d(func):
#     def inner():
#         return func() + " first " + " second1 " + func()
#     return inner
#
# def split_d(func):
#     def wrap():
#         return "second " +func() +" second2"
#     return  wrap
#
# @upper_d
# @split_d
# def ordinary():
#     return "Good morning"
#
# print(ordinary())


# def decor2(func):
#     def inner2():
#         x = func()
#         return x * x
#     return inner2
#
#
# def decor1(func):
#     def inner1():
#         x = func()
#         return 2 * x
#     return inner1
#
#
# @decor1
# @decor2
# def original():
#     return 10
# print(original())





# def upper_d(func):
#     def inner():
#         return "first " + " second1 " + func()
#     return inner
#
# def split_d(func):
#     def wrap():
#         return "second "+func() +"second2"
#     return  wrap
#
# @upper_d
# @split_d
# def ordinary():
#     return "Good morning"
#
# print(ordinary())
# ---------------------------------------------------------------------------------------------------------------------



# EX:1  Creating an another reference variable to the same function: (Function aliasing)
# for the existing function we can give another ref variable.Internally every function is an object
# we can access the function by using wish or greet
# if we delete one ref variable still we can access the function by using another ref variable


# def wish(name):
#     print("Hello", name)

# greet = wish                     (creating an another ref variable to the same function.Because wish is already pointing to that function)
# greet("Gangadhar")               (Hello Gangadhar)
# wish("Gangadhar")                (Hello Gangadhar)

# ------------------------------------------------------------------------------------------------------------------------------------------

# EX:2  NESTED FUNCTIONS(Function inside another function)
# we should call inner function with in the outer function and out side of inner function because inner function is local to outer function
# If we call inner function from outside of outer function we get name error
# Nested functions are local to outer functions. We can not call nested functions from outside directly

# def outer():
#     print("outer function execution")
#     def inner():    (creating inner function with in the outer function)
#         print("Inner function execution")
#     inner()         (calling the inner function)
#     print("Outer function is returning inner function")
#
# outer()          (calling outer function)
# ----------------------------------------------------------------------------------------------------------------------

# EX:3 Calling the inner function from outside of function
# Function can also return  another function

# def outer():        (creating outer function)
#     print("outer function execution")
#     def inner():    (creating inner function)
#         print("Inner function execution")
#     print("Outer function is returning inner function")
#     return inner    (outer function is returning inner.so now inner will go to the place from where outer is called)
#
#
# new = outer()      (here internally new = inner)
# new()              (so here we are calling inner() with the help of new())


# def f1():
#     print(100)
#     def f2():
#         print('f2 value')
#         return 200
#
#     return f2
# x = f1()
# print(x())

# ----------------------------------------------------------------------------------------------------------------------



# EX:2 passing single argument to the function
# def f1(func):       (here f1(func) = f1(fx))
#     print(f"f1 function got {func} as an argument")
#     print(id(func))
#     func()         (calling func() ie calling fx().so fx() will be executed automatically)
#
# def fx():
#     print("fx function")
#
# def fy():
#     print("fy function")
#
#
# f1(fx)     (calling f1 function by passing fx as argument...so it become fx = func
# print(id(fx))
# f1(fy)     (again calling f1 function by passing fy as an argument...so now fy = func()
# print(id(fy))


# def upper_d(ordinary):
#     def inner():
#         return ordinary() + " first " + " second1 " + ordinary()
#     return inner
#
# def split_d(inner):
#     def wrap():
#         return "second " +inner() +" second2"
#     return  wrap
# @upper_d
# @split_d
# def ordinary():
#     return "Good morning"

# print(ordinary())





# def decor(func):
#     def inner(x, y):
#         if y == 0:
#             print("sorry we can not divide the number by zero")
#         else:
#             return func(x, y)
#     return inner
#
# @decor
# def division(a, b):
#     a, b = b, a
#     print(a / b)
#
# @decor
# def moduloo(a, b):
#     print(a % b)
#
# division(20,10)
# division(10, 0)
# moduloo(20, 10)
# moduloo(20, 0)

# def decor_greet(func):
#     def inner(name):
#         vip = ["DGS", "TSK", "TRS", "BJP", "TDP"]
#         if name in vip:
#             print("Hello {}.How are you?.Thanks for coming".format(name))
#         else:
#             func(name)
#     return inner
#
# @decor_greet
# def greet(name):
#     print("hello", name)
#
# greet("Durga")
# greet("efce")
# greet("fsfeef")
# greet("DGS")
# greet("TRS")
# ---------------------------------------------------------------------------------------------------------------------
# def decor(func):
#     def inner(name):
#         if name == "MP" and "MLA":
#             print("Hello", name)
#         else:
#             func(name)
#     return inner
#
# @decor
# def greet(name):
#     print("Good morning", name)
# greet("MLA")
#------------------------------------------------------------------------------------------------------------------------
# def decor(func):
#     def inner(a, b):
#         if b == 0:
#             print("zero division error")
#         else:
#             func(a, b)          [func(a, b) = division(a, b)]
#     return inner
#
# @decor
# def division(a, b):
#     print(a / b)
# division(10, 0)
#
#
# @decor
# def moduloo(a, b):
#     print(b % a)
# moduloo(10, 0)
# ---------------------------------------------------------------------------------------------------------------------
# def lowercase_decorator(function):
#     def wrapper1():
#         func = function()
#         string_lowercase = func.lower()
#         return string_lowercase
#     return wrapper1
#
# def splitter_decorator(function):
#     def wrapper2():
#         func = function()
#         string_split = func.split()
#         return string_split
#     return wrapper2
# @splitter_decorator # this is executed next
# @lowercase_decorator # this is executed first
# def hello():
#     return 'HELLO WORLD'
# print(hello())

# ----------------------------------------------------------------------------------------------------------------------

# def names_decorator(function):
#     def wrapper(arg1, arg2):
#         arg1 = arg1.capitalize()
#         arg2 = arg2.capitalize()
#         string_hello = function(arg1, arg2)
#         return string_hello
#     return wrapper
#
# @names_decorator
# def say_hello(name1, name2):
#     return 'Hello ' + name1 + '! Hello ' + name2 + '!'
# print(say_hello('sara', 'ansh'))

# ---------------------------------------------------------------------------------------------------------------------
# def temp(func):
#     def wrap(x):
#         print("When we convert fahrenheit to celicius we get celcius temperature as:", end=" ")
#         return func(x)
#     return wrap
# @temp
# def fahrenheit_celsius(f):
#     return round((f - 32) * 5/9, 2)
# t = float(input("enter fahrenheit temperature to know celcius temperatue:"))
# print(fahrenheit_celsius(t), "C")

# ---------------------------------------------------------------------------------------------------------------------
# def temp(func):
#     def wrapper(v):
#         print("When we convert celcius to fahrenheit we get fahhrenheit temperature as:", end=" ")
#         return func(v)
#     return wrapper
# @temp
# def celsius_fahrenheit(c):
#      return round((c * 9/5) + 32, 2)
# t = float(input("enter celcius temperature to know fahrenheit temperatue:"))
# print(celsius_fahrenheit(t), "F")

# ---------------------------------------------------------------------------------------------------------------------

# def decor1(wrap1):
#     def inner():
#         return "hai "+wrap1()+" good evening "
#     return inner
#
# def decor2(wrap2):
#     def inner1():
#         return wrap2() + " good morning " + wrap2()+" good night "
#     return inner1
#
# def decor3(wrap3):
#     def inner2():
#         return "hello "+"good morning " + wrap3() + "good night"
#     return inner2
#
# @decor2
# @decor3
# @decor1
# def func():
#     return " Hello good morning "
# print(func())
# # ---------------------------------------------------------------------------------------------------------------------


# __name == "__main__:
# import udemy
# print("TOP LEVEL IN DECORATORS.PY")
# udemy.func()
# print(__name__)
# if __name__ == "__main__":
#      print("DECORATOR.PY IS RUNNING DIRECTLY")
# else:
#    print("DECORATOR.PY is being imported!")

# ---------------------------------------------------------------------------------------------------------------------
# import udemy
# print(udemy.mul(10, 5))
# print(__name__)
#---------------------------------------------------------------------------------------------------------------------

# import udemy
# print("I need only f1()")
# print(__name__)
# if __name__ == "__main__":
#     udemy.f1()
# ---------------------------------------------------------------------------------------------------------------------
# def decor(func):
#     def inner(a, b):
#         print(f"The addition of {a} and {b} is", end=" ")
#         print(func(a, b))
#     return inner
#
#
# @decor
# def func(a, b):
#     return a + b
# a = int(input())
# b = int(input())
# func(a,b)





# def decor(func):
#     def inner():
#         print("Please follow some healthy tips")
#         print("so that you look beautifully")
#         func()
#         print()
#     return inner
#
# @decor
# def display():
#     print("Showing the person as ususally")
#
# display()
# display()
# display()


# from udemy import DgsDivisionError
# def func(a, b):
#     try:
#         if b == 0:
#             raise DgsDivisionError
#     except DgsDivisionError:
#         print(a / a)
# func(10, 0)





