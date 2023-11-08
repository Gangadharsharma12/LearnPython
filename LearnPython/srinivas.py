#WAP TO FIND A REVESE OF A GIVEN NUMBER:

# n=input("enter a number:")
# print("reverse of a given numbers is",n[::-1])

                    #(OR)
# n=int(input("enter a number:"))
# rev=0
# while n>0:
#     r=n%10
#     rev=(rev*10)+r
#     n=n//10
# print(f"reverse of a given numbers is {rev}")

#WAP TO CHECK A NUMBER IS PRIME OR NOT:
# n=int(input("enter a number:"))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count=count+1
#         print("Not a prime")
#         break
# else:
#     if (count==0):
#         print("Prime")


# n=int(input("enter a number:"))
# if (n<=1):
#     print("not a prime")
# else:
#     x=2
#     while x*x<=n:
#         if n%x==0:
#             print("not a prime")
#             break
#         x+=1
#     else:
#          print("yes")

#WAP TO PRINT FIBONACI SERIES IN A GIVEN RANGE:
# n=int(input("enter a range:"))
# fib1=0
# fib2=1
# fib=0
# while fib1<n:
#     fib=fib1+fib2
#     print(fib1,end=" ")
#     fib1=fib2
#     fib2=fib

# c = int(input())
# def fib_ser(n):
#     if n < 1:
#         return 1
#     if n < 3:
#         return 1
#     e1 = e2 = 1
#     s = 0
#     for i in range(3, n+1):
#         s = e1 + e2
#         e1, e2 = e2, s
#     return s
# for i in range(1, c+1):
#     print(i, "------->", fib_ser(i))


#WAP TO FIND THE MAXIMUM OF THREE NUMBERS USING TERNARY OPERATOR
# a=int(input())
# b=int(input())
# c=int(input())
# max= (a) if (a>b) and (a>c) else (b) if (b>c) else (c)
# print("maximum value",max)
#
# #WAP TO FIND THE MINIMUM OF THREE NUMBERS USING TERNARY OPERATOR
# a=int(input())
# b=int(input())
# c=int(input())
# min= (a) if (a<b) and (a<c) else (b) if (b<c) else (c)
# print("minimum value",min)


'''n=int(input("enter the range:"))
l=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)
'''

#WAP TO PRINT 1 TO N NATURAL NUMBERS:
# n=int(input("enter the range:"))
# for i in range(n+1):
#     print(i,end=" ")

#WAP TO FIND THE SUM OF FIRST N NUMBERS

# n=int(input("enter the range:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     avg=sum/n
# print(sum)
# print(avg)


#WAP TO SWAP TWO NUMBERS
# print("before swapping")
# a=int(input("enter the first value:"))
# b=int(input("enter the second value:"))
# temp=a
# a=b
# b=temp
# print("after swapping")
# print(a)
# print(b)


#WAP TO PRINT THE SUM OF DIGITS IN A GIVEN NUMBER

# n=int(input("enter a number:"))
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*r
#     n=n//10
# print(sum)

#WAP TO PRINT THE PRODUCT OF DIGITS IN A GIVEN NUMBER
# n=int(input("enter a number:"))
# sum=1
# while n>0:
#     r=n%10
#     sum=sum*r
#     n=n//10
# print(sum)


#WAP TO CHECK A NUMBER IS ARMSTRONG OR NOT
n = int(input("enter a number:"))
a = str(n)
m = n
s = 0
while n > 0:
          r = n % 10
          s = s+r**len(a)
          n = n//10
if (m == s):
    print("ARMSTRONG")
else:
    print("NA")

#WAP TO PRINT ARMSTRONG NUMBERS IN A GIVEN RANGE

# n=int(input("enter the range:"))
# for i in range(n):
#     m=i
#     s=0
#     a=str(i)
#     while i>0:
#         r=i%10
#         s=s+r**len(a)
#         i=i//10
#     if (m==s):
#         print(m)



# def abc(p,q):
#     while p !=q:
#         if p>q:
#             p=p-q
#         else:
#             q=q-p
#     return p

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# print("the gcd of given numbers is :",abc(a,b))


# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# a=a+b
# b=a-b
# a=b+b
# print(a)
# print(b)



# n=input("enter any alphabet:")
# l1=("a","e","i","o","u")
# l2=("A","E","I","O","U")
# if n in l1 or l2:
#     print("oval")
# else:
#     print("consonent")



# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# if (a==b):
#     print("the given numbers are equal ")
# elif(a<b):
#     print(f"{a} is less than {b}")
# else:
#     print(f"{a} is greater than {b}")


# n=int(input("enter first number:"))
# for i in range(1,101):
#     print(f"{n}*{i}={n*i}")



# n=int(input("enter first number:"))
# for i in range(n,0,-1):
#     print(i,end=" ")



# n=int(input("enter first number:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("The given number is a perfect number")
# else:
#     print("The given number is not a perfect number")



import sys
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
#     print(f"The addition of {a} and {b} is {sum}")
# if option==2:
#     difference=a-b
#     print(f"The difference of {a} and {b} is {difference}")
# if option==3:
#     product=a*b
#     print(f"The product of {a} and {b} is {product}")
# if option==4:
#     division=a/b
#     print(f"The division of {a} and {b} is {division}")
# print("TQ")


# celcius=float(input("enter the celsius temperature:"))
# fahrenheit=(celcius*9/5)+32
# print(fahrenheit)



# fahrenheit=float(input("enter the fahrenheit temperature:"))
# celcius=(fahrenheit-32)*5/9
# print(celcius)


