# EX:1
# import re
# pattern = re.compile("ab")
# matcher = pattern.finditer("abaababa")
# count = 0
# for match in matcher:
#     count += 1
#     print(match.start(), "------", match.end(), "-----", match.group())
# print(f"The number of occurances are:{count}")

# ---------------------------------------------------------------------------------------------------------------------

# EX:2
# import re
# pattern = re.compile("[a-z]")
# matcher = pattern.finditer("abaababa")
# count = 0
# for match in matcher:
#     count += 1
#     print(match.start(), "------", match.end(), "-----", match.group())
# print(f"The number of occurances are:{count}")
# ---------------------------------------------------------------------------------------------------------------------
# EX:3
# import re
# pattern = re.compile("[0-9]")
# matcher = pattern.finditer("ab5aab2aba1")
# count = 0
# for match in matcher:
#     count += 1
#     print(match.start(), "------", match.end(), "-----", match.group())
# print(f"The number of occurances are:{count}")

# ----------------------------------------------------------------------------------------------------------------------

# 144  EX:1
# import re
# n1 = re.compile("a")             compiling string into n1 object
# n2 = n1.finditer("Gangadhar")    here n2 is an iterable object.
# for each in n2:
#     print(f"{each.start()}-----{each.end()}------{each.group()}")


# EX:2
# import re
# n1 = re.compile("[abc]")      If we want to search for either a or b or c
# n2 = n1.finditer("Gangadhar")
# for each in n2:
#     print(f"{each.start()}-----{each.end()}------{each.group()}")


# EX:3  defining directly without using compile
# import re
# matcher = re.finditer("[abc]", "a2b7k@q")    search either a or b or c
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")


# EX:4   except abc search for all
# import re
# matcher = re.finditer("[^abc]", "a2b7k@q")
# count = 0
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")
#     count += 1
# print(f"The total number of occurances are:{count}")


# EX:5   search all the lower case alphabets from a-z.we can also limit from any letter to any letter
# import re
# matcher = re.finditer("[a-z]", "a2b7k@q")
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")


# EX:6   search for only upper case alphabets

# import re
# matcher = re.finditer("[A-Z]", "A2b7K@Q")
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")


# EX:7   search for both lower case and upper case alphabets

# import re
# matcher = re.finditer("[a-zA-Z]", "A2b7K@Qa1b2c3")
# for each in matcher:
#     print(f"{each.start()} ---- {each.end()}-----{each.group()}")


# EX:8   search for only digits from 0-9
# import re
# matcher = re.finditer("[0-9]", "A2b7K@Qa1b2c3")
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")


# EX:9  ANY alpha numeric character
# import re
# matcher = re.finditer("[0-9 A-Z a-z]", "A2b7K@Qa1b2c3")
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")


# EX:10 To get special symbols

# import re
# matcher = re.finditer("[^0-9 A-Z a-z]", "A2b7K@Qa1b2c3")
# for each in matcher:
#     print(f"{each.start()} ---- {each.group()}")

# ---------------------------------------------------------------------------------------------------------------------

# 145 (Match())
# EX:1
# import re
# p = input("Enter the string in which target is to be searched for:")
# t = input("Enter the pattern to check:")
# m = re.match(t, p)
# if m != None:
#     print(f"Yes,the given pattern begin with {t}")
#     print(f"{m.start()} ---- {m.end()} ---- {m.group()}")
# else:
#     print(f"No,The given pattern will not begin with {t}")


# EX:2 ( Here None is returned)
# import re
# p = input("Enter the string in which target is to be searched for:")
# t = input("Enter the pattern to check:")
# m = re.match(t, p)
# print(m)


# EX:3 (FULLMATCH)
# import re
# num = input("Enter the mobile number to validate:")
# pattern = "[6-9][0-9]{9}"
# match = re.fullmatch(pattern, num)
#
#
# if match != None:
#     print(f"{num} is valid mobile number")
# else:
#     print(f"{num} is not a valid mobile number")



# EX:4(Returns None when the num does not match with pattern)

# import re
# num = input("Enter the mobile number to validate:")
# pattern = "[6-9][0-9]{9}"
# match = re.fullmatch(pattern, num)
# print(match)



# EX:5 [Search()]

# import re
# target = input("Enter the target:")
# str = input("Enter the string in which target to be searched for:")
# match = re.search(target, str)
# if match != None:
#     print(f"Target found at index:{match.start()} and end with {match.end()}")
# else:
#     print("No matching is found")


# EX:6  [FINDALL]
# import re
# l = re.findall("[0-9]", "a1b2c3d4e5")
# print(l)


#EX:7 [FINDITER]

# import re
# matcher = re.finditer("[0-9]", "a1b2c3d4")
# for match in matcher:
#     print(match.start(), "-------", match.end(), "-------", match.group())



# EX:8  [SUB]

# import  re
# s = re.sub("[0-9]", "***", "a1b2c3d4e5")
# print(s)


# EX:9 [SUBN]
# import re
# t = re.subn("[0-9]", "***", "a1b2c3d4")
# print(t)
# print("The result string is", t[0])
# print("The number of times replaced is", t[1])



# EX:10 [SPLIT]
# import re
# l = re.split(":", "07-30-22")
# print(l)


# import re [splitting is done whereever nither : nor , is present
# l = re.split("[:, ,]", "sunny,bunny:vinny,pinny:chinny")
# print(l)


# import re    if we take only . then it will split at every character because . means everything is matched
# l = re.split("[.]", "gangadhar.sharma.178.gmail.com")    [.] means consider only . symbol...we can also take "\."
# print(l)

# ---------------------------------------------------------------------------------------------------------------------

# 146  EX:1  [^ symbol]

# import re
# match = re.search("^Learn", "Learning python")
# if match != None:
#     print("Learning python begins with Learn")
# else:
#     print("not matched")


# EX:2   [$ symbol]
# import re
# match = re.search("easy$", "Learning python is easy")
# if match != None:
#     print("Matched")
# else:
#     print("not matched")



# EX:3  [IGNORECASE]
# import re
# match = re.search("^LEARNING", "Learning python is easy", re.IGNORECASE)
# if match != None:
#     print("Matched")
# else:
#     print("not matched")

# ---------------------------------------------------------------------------------------------------------------------
# Real time applications
# Programm to check the given male is valid or not:

# import re
# target = input()
# pattern = "[a-zA-Z0-9@.]*"
# match = re.fullmatch(pattern, target)
# if match != None:
#     print("Valid")
# else:
#     print("Invalid")

# To check valid mobile number
# import re
# target = input()
# pattern = "[6-9]\d{9}"
# match = re.fullmatch(pattern, target)
# if match != None:
#     print("valid phone number")
# else:
#     print("Invalid number")


# n = input()
# s = ""
# for i in n:
#     s = i + s
# print(s)


# l = ["amul", 1, 1, 1, 4, 5, 6, 5]
# n = 5
# l1 = []
# for i in range(len(l)):
#     if l[i] == n:
#         l1.append(i)
# print(l1)


# n = int(input())
# l = []
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l.append(i)
#
# for each in l:
#     a = str(each)
#     b = ""
#     c = -1
#     while c >= -len(a):
#         b += a[c]
#         c -= 1
#     if int(b) == each:
#         print(each,end = ",")

# import random
# def otpgen():
#     s = ""
#     for i in range(5):
#         s += str(random.randint(0, 9))
#     print("Your otp is", end=" ")
#     print(int(s))
# otpgen()
# import time
# for i in range(1, 1001):
#     print(f"{i} ----->  arunachala shiva")
#     time.sleep(1)


# def boolcheck(regfees, courseopted):
#     if (courseopted == "salesforce admin") or (courseopted == "salesforce developer") or (courseopted == "big data"):
#         return False
#     else:
#         if regfees < 5000:
#             return True
#         else:
#             return False
# print(boolcheck(4000, "Big data"))

# ch = input().lower()
# d = {1: "a", 2: "e", 3: "i", 4: "o", 5: "u"}
# for each in d:
#     if ch == d[each]:
#         print(f"{ch} is vowel")
#         break
# else:
#         print(f"{ch} is consonent")

# a = int(input())
# b = int(input())
# c = int(input())
# max = a if (a > b and a > c) else b if (b > c) else c
# if max == a:
#     print(f"{max} is greater than {b} and {c}")
# elif max == b:
#     print(f"{max} is greater than {a} and {c}")
# else:
#     print(f"{max} is greater than {a} and {b}")

# d = {1: "sunday", 2: "monday", 3: "tuesday", 4: "wednesday", 5: "thursday", 6: "friday", 7: "saturday"}
# n = int(input("Enter any number: \n"))
# print(d[n])

