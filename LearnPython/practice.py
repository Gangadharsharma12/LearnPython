#1: WAP TO REVERSE A GIVE STRING
# s=input("enter a string:")
# print(s[::-1])
# print(s)

#2: WAP TO REVESE THE WORDS IN A GIVEN STRING:
#I/P:GANGADHAR SHARMA DAMMANNAGARI
#O/P: DAMMANNAGARI SHARMA GANGADHAR

# s=input("enter a string:")
# l=s.split()
# for x in l:
#     break
# target=" ".join(l[::-1])
# print(target)

#3.WAP TO REVERESE THE WORDS INDEX WISE
#I/P: GANGADHAR SHARMA DAMMANNAGARI
#O/P: RAHDAGANAG AMRAHS IRAGANNAMMAD

# s=input("enter a string:")
# l=s.split()
# i=0
# for x in l:
#     print(x[::-1],end=" ")

#4th. WAP TO PRINT THE CHARACTERS PRESENT AT EVEN AND ODD PLACES PRESENT IN A GIVEN STRING

# s=input("enter a string:")
# l=len(s)
# i=0
# while i<l:
#     if i%2==0:
#         print("The character present at odd string are",s[i])
#         i=i+1
#     else:
#      print("The character present at even string are",s[i])
#      i=i+1


#5th  wap to merge the characters into a single string by taking the albhabets alternatively

# s=input("enter any string:")
# t=input("enter second string:")
# n=len(s)
# a,b=0,0
# output=""
# while a<len(s) or b<len(t):
#         if a<len(s):
#             output=output+s[a]
#             a=a+1
#
#
#         if b<len(t):
#             output=output+t[b]
#             b=b+1
# print(output)

#6th WAP TO SORT CHARACTERS OF GIVEN STRING FIRST ALPHABETS FOLLOWED BY NUMBERS

# s=input("enter any string:")
# a1=" "
# b1=" "
# for x in s:
#     if x.isalpha():
#         a1=a1+x
#     else:
#         b1=b1+x
# target="".join(sorted(a1)+sorted(b1))
# print(target)


#8th   WAP TO PRFORM FOLLOWING TASK
#I/P:b6l9z8
#o/p:bhluz

# s="b6l9z8"
# target=" "
# for x in s:
#     if x.isalpha():
#         br=x
#         target=target+br
#     else:
#         newbr=chr(ord(br)+int(x))
#         target=target+newbr
# print(target)


#9th. WAP to remove duplicate characters in the string given

# s=input("enter any string:")
# l1=set()
# for x in s:
#     if x not in l1:
#         l1.add(x)
# output="".join(sorted(l1))
# print(output)


#10th   WAP TO FIND THE NUMBER OF OCCURANCES OF EACH CHARACTER IN THE GIVEN STRING
# s=input("enter any string:")
# d={}
# for x in s:
#     if x not in d:
#         d[x]=1
#     else:
#         d[x]=d[x]+1
# for y,z in d.items():
#     print("{} occured {} times". format(y,z))


#11th   WAP FOR THE FOLLOWING TASK
# I/P:ONE TWO THREE FOUR
# O/P:ONE OWT THREE RUOF


# s=input("enter any string:")
# l1=s.split()
# l2=[]
# i=0
# while i<len(l1):
#     if i%2==0:
#         l2.append(l1[i])
#     else:
#         l2.append(l1[i][::-1])
#     i=i+1
# target=" ".join(l2)
# print(target)


# p=input("enter any number:")
# q=input("enter any number:")
# p,q=q,p
# print("The value of p after swopping is",p)
# print("The value of q after swapping is",q)

#-----------------------------------------------------------------------------------------------------------------------

# s='The python \"classes\" by durga sir are \"good\"'
# m='my name is \"dammannagari gangadhar sharma\"'


# s=input("enter a name:")
# i=0
# for x in s:
#     print(f"The character present at positive index {i} and negative index{i-len(s)} is {x}")
#     i=i+1


# s=input()
# print("FORWARD DIRECTION:")
# for x in s[::1]:
#     print(x)
# print("BACKWARD DIRECTION:")
# for x in s[::-1]:
#     print(x)


# s=input()
# s1=input()
# if s1 in s:
#     print(s1,"is found in",s)
# else:
#     print(s1,"is not found in",s)

# s="afhfhvfhzbvjvjsdgvagfajgcjacashvkshvhsdvkhsvhahviashffakgduatfuavgzmbvmzbvmzbcmagcfjhavhavj"
# subs="a"
# print(f"The total number of occurances of {subs} in {s} are" ,s.count(subs))


# s="gshcgs bsjcbgsjc cbscbj"
# s=s.split(" ")
# print(s)

#n="durga"
# s=10000
# a=24
# print("my name is {},my salary is {} and my age is {}".format(n,s,a))
# print("my name is {0},my salary is {1} and my age is {2}".format(n,s,a))
# print("my name is {x},my salary is {y} and my age is {z}".format(z=a,y=s,x=n))
# print(f"my name is {n},my salary is {s} and my age is {a}")


#-----------------------------------------------------------------------------------------------------------------------
#LIST
#----------------------------------------------------------------------------------------------------------------------
# l=[0,1,2,3,4,5]
# i=0
# for x in l:
#     print(f"The element present at positive index {i} and negative index {i-len(l)} is {x}")
#     i=i+1


# import sys
# class Table:
#     def __init__(self):
#         self.no_of_legs = 4
#         self.glass_top = None
#         self.wooden_top = None
# dining_table = Table()
# back_table = Table()
# front_table = back_table
# back_table = dining_table
# dining_table = front_table
# front_table = back_table
# print(sys.getrefcount(front_table))



# a = 16
# b = 5
# while (a >= 2):
#     if (a > b):
#         a = a / 2
#     else:
#         print(a)
#         break




# g = ["A", "B", "B", "B+", "A","A","B-"]
# for grade in g:
#     if grade == "A":
#         print("Interviwe bit")
#     else:
#         print("NIB")


# class Parent:
#     def __init__(self, num):
#         self.__num = num
#     def get_num(self):
#         return self.__num
# class child(Parent):
#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val = val
#     def get_val(self):
#         return self.__val
# son = child(100, 200)
# print(son.get_num())
# print(son.get_val())



# class Demo:
#     num = 5
#     def __init__(self,status):
#         num = 10
#         print(status, num)
# d = Demo("A")


# class Customer:
#     def __init__(self, cust_id, age):
#         self.cust_id = cust_id
#         self.age = age
#
# c2 = Customer(100, 20)
# def change(c2):
#     c2 = Customer(100, 21)
# change(c2)
# print(c2.age)



# class Example:
#     def __init__(self):
#         self.__num = 5
#     def set__num(self,num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
# obj = Example()
# obj.set__num(6)
# print(obj.get_num())




# class Table:
#     def __init__(self):
#         self.no_of_legs = 4
#         self.__glass_top = None
#         self.__wooden_top = None
#
#     def assign_data(self, glass_top, wooden_top):
#         self.__glass_top = glass_top
#         self.__wooden_top = wooden_top
#
#     def identify_rate(self, glass_top, wooden_top):
#         self.assign_data(glass_top, wooden_top)
#         if(self.assign_data == True):
#             rate = 20000
#         elif(self.__wooden_top == True):
#             rate = 30000
#         else:
#             rate = 0
#         return rate
# dining_table = Table()
# dining_table.assign_data(10,20)
# rate = dining_table.identify_rate(True,False)
# print(rate)

# import time
# import itertools
# for i in itertools.count(1000, 500):
#     print(i, end = " ")
#     time.sleep(1)


# import itertools
# count = 0
# for i in itertools.cycle(" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "):
#     if count >= 389:
#         break
#     else:
#         print(count, i, end=" ")
#         count += 1






