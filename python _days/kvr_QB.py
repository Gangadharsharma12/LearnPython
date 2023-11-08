# 1.Write a Python program to sum all the items in a list.

# l = [1, 2, 3, 4, 5]
# c = 0
# for each in l:
#     c = c + each
# print(c)
#-------------------------------------------------------------------------------------------------------------------------------
#2. Write a Python program to multiply all the items in a list.

# l = [1, 2, 3, 4, 5]
# c = 1
# for each in l:
#     c *= each
# print(c)
# -----------------------------------------------------------------------------------------------------------------------------

#3. Write a Python program to get the largest number from a list.
# l = [22, 55, 2, 99, 78, 45, 56]
# l.sort()
# print(f"The largest number in {l} is {l[-1]}")
# ------------------------------------------------------------------------------------------------------------------------------

#4. Write a Python program to get the smallest number from a list.

# l = [22, 55, 2, 99, 78, 45, 56]
# l.sort()
# print(f"The smallest number in {l} is {l[0]}")

# ------------------------------------------------------------------------------------------------------------------------------
#
# 5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2


# l = ['abc', 'xyz', 'aba', '1221', "xyx"]
# l1 = []
# for each in l:
#     if each[0] == each[-1]:
#         l1.append(each)
# print(len(l1))
# -------------------------------------------------------------------------------------------------------------------------------

#6.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# l = [(2, 5), (1, 2), (4, 4), (10, 0), (2, 3), (2, 1)]
# l1 = []
# l2 = []
# for each in l:
#     l1.append(each[1])
# l1.sort()
# for each in l1:
#     for x in l:
#         if x[1] == each:
#             l2.append(x)
# print(l2)
# ------------------------------------------------------------------------------------------------------------------------------

#7.Write a Python program to remove duplicates from a list.
# l = [1, 2, 3, 2, 3, 4, 2, 1, 6, 2, 3, 2, 7]
# l1 = []
# for each in l:
#     if each not in l1:
#         l1.append(each)
# print(l1)

# ------------------------------------------------------------------------------------------------------------------------------

#8.Write a Python program to check a list is empty or not
# l = [1, 2, 3]
# if len(l) > 0:
#     print("List is not empty")
# else:
#     print("list is empty")
# ------------------------------------------------------------------------------------------------------------------------------
# 9.Write a Python program to clone or copy a list

# l = [1, 2, 3]
# l1 = l.copy()
# print(l1)
# print(id(l1))   2129558258496
# print(id(l))    2129558258688

# -------------------------------------------------------------------------------------------------------------------------------

# 10.Write a Python program to find the list of words that are longer than n from a given list of words

# l = ["a", "bc", "def", "ghij", "klmno", "pqrstu"]
# n = int(input("enter any number:"))
# l1 = []
# for each in l:
#     if len(each) > n:
#         l1.append(each)
# print(l1)
# -----------------------------------------------------------------------------------------------------------------------------
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

# def func(l1, l2):
#     flag = True
#     for each in l1:
#         for i in l2:
#             if each == i:
#                 flag = False
#                 print("True")
#                 break
#     else:
#         if flag == True:
#             print("False")
#
# func([1, 2, 3], [8, 5, 6, 2])
# -----------------------------------------------------------------------------------------------------------------------------
# 12.

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 		Expected Output : ['Green', 'White', 'Black']

# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# l1 = []
# for each in l:
#     if l.index(each) == 0:
#         continue
#     elif l.index(each) == 4:
#         continue
#     elif l.index(each) == 5:
#         continue
#     else:
#         l1.append(each)
# print(l1)
# ------------------------------------------------------------------------------------------------------------------------------

# 13.
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# for each in l:
#     if each % 2 != 0:
#         l1.append(each)
# print(l1)

# -------------------------------------------------------------------------------------------------------------------------------

# 15. Write a Python program to shuffle and print a specified list.
# import random
# l = [1, 2, 3, 4, 5]
# random.shuffle(l)
# print(l)
#-----------------------------------------------------------------------------------------------------------------------------

#35 Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# 	Sample list : ['p', 'q']
# 	n =5
# 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# l = ["p", "q"]
# l1 = []
# n = int(input("enter any number:"))
# for i in range(1, n+1):
#     for each in l:
#         l1.append(each + str(i))
# print(l1)

# -----------------------------------------------------------------------------------------------------------------------------
# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# 	Sample list: [0,1,2,3,4,5]
# 	Expected Output: [1, 0, 3, 2, 5, 4]

# l = [0, 1, 2, 3, 4, 5]
# l1 = []
# for each in l:
#     if l.index(each) % 2 == 0:
#         l1.append(each + 1)
#     else:
#         l1.append(each - 1)
# print(l1)
# -----------------------------------------------------------------------------------------------------------------------------

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# 		Sample list: [11, 33, 50]
# 		Expected Output: 113350

# l = [11, 33, 50]
# l1 = ""
# for each in l:
#     for x in str(each):
#         l1 += x
# print(int(l1))

# ------------------------------------------------------------------------------------------------------------------------------

# Write a Python program to get the difference between the two lists

# l = [2, 4, 6]
# l1 = [3, 6, 9]
# l2 = list(zip(l, l1))
# l3 = []
# for each in l2:
#     l3.append(each[1] - each[0])
# print(l3)
# ------------------------------------------------------------------------------------------------------------------------------

#58 Write a Python program to replace the last element in a list with another list.
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# l =  [1, 3, 5, 7, 9, 10]
# l1 = [2, 4, 6, 8]
# l.pop(-1)
# print(l + l1)
# -----------------------------------------------------------------------------------------------------------------------------

# 63.Write a Python program to insert a given string at the beginning of all items in a list.
# 	Sample list : [1,2,3,4], string : emp
# 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

# l = [1, 2, 3, 4]
# s = "emp"
# l1 = []
# for each in l:
#     l1.append(s+str(each))
# print(l1)
# -----------------------------------------------------------------------------------------------------------------------------

 # 65. Write a Python program to move all zero digits to end of a given list of numbers.
	# Expected output:
	# Original list:
	# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
	# Move all zero digits to end of the said list of numbers:
	# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# l = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# l1 = []
# l2 = []
# for each in l:
#     if each == 0:
#         l1.append(each)
#     else:
#         l2.append(each)
# print(l2 + l1)
# ------------------------------------------------------------------------------------------------------------------------------

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]

# l = [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]
# l1 = []
# d = {}
# for each in l:
#     c = 0
#     for i in each:
#         c += i
#     d[c] = each
#     l1.append(c)
# print(d[max(l1)])
# ----------------------------------------------------------------------------------------------------------------------

# 67. Write a Python program to find all the values in a list are greater than a specified number.
# l = [0, 3, 55, 33, 21, 6, 8, 44, 90, 34, 78, 50, 84]
# n = int(input("enter any number:"))
# for each in l:
#     if each > n:
#         print(each, end=" ")
# ---------------------------------------------------------------------------------------------------------------------

# 68 Write a Python program to extend a list without append.
# 	Sample data: [10, 20, 30]
# 	[40, 50, 60]
# 	Expected output : [40, 50, 60, 10, 20, 30]

# l1 = [ 10, 20, 30]
# l2 = [40, 50, 60]
# print(l2+l1)
# ----------------------------------------------------------------------------------------------------------------------
# 69. Write a Python program to remove duplicates from a list of lists.
# 		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# 		New List : [[10, 20], [30, 56, 25], [33], [40]]

# l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# l1 = []
# for each in l:
#     if each not in l1:
#         l1.append(each)
# print(l1)
# ---------------------------------------------------------------------------------------------------------------------
# 70 Write a Python program to find the items starts with specific character from a given list.
# 		Expected Output:
# 		Original list:
# 		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# 		Items start with a from the said list:
# 		['abcd', 'abc', 'acjd']
# 		Items start with d from the said list:
# 		['dagfa']
# 		Items start with w from the said list:
# 		[]

# l = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# l1 = []
# s = input("enter the starting letter:")
# for each in l:
#     if each[0] == s:
#         l1.append(each)
# print("Items start with '{}' from the said list:".format(s))
# print(l1)
# ---------------------------------------------------------------------------------------------------------------------

# 71. Write a Python program to check whether all dictionaries in a list are empty or not.
# 	Sample list : [{},{},{}]
# 	Return value : True
# 	Sample list : [{1,2},{},{}]
# 	Return value : False

# l = [{}, {1, 2}, {}]
# flag = "True"
# for each in l:
#     if len(each) != 0:
#         flag = "False"
#         break
#     else:
#         flag = "True"
# if flag == "True":
#     print("True")
# else:
#     print("False")
#-----------------------------------------------------------------------------------------------------------------------
# 73. Write a Python program to remove consecutive duplicates of a given list.
# 		Original list:
# 		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 		After removing consecutive duplicates:
# 		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# ----------------------------------------------------------------------------------------------------------------------
# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# 	Original list:
# 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 	After packing consecutive duplicates of the said list elements into sublists:
# 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

# l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# l1 = []
# for each in l:
#     l1.append([each])
# l2 = []
# for each in l1:
# ---------------------------------------------------------------------------------------------------------------------

# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

# l = [1, 1, 2, 3, 4, 4, 5, 1]
# l1 = []
# c = 0
# for each in l:
#     if l[c] == l[c+1]:
#         l1.append([l[c], l[c+1]])
# print(l1)


# Write a Python program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

# l = [[2, 1], 2, 3, [2, 4], 5, 1]
# l1 = []
# for each in l:
#     l1.append([each])
# print(l1)
# l2 = []
# ---------------------------------------------------------------------------------------------------------------------

# 109
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# l2 = []
# l3 = []
# dir = input("please enter the direction:").lower()
# n = int(input("enter the number:"))
# if dir == "right":
#     c = 0
#     while c < n:
#         l1.append(l[-n+c])
#         c += 1
# for i in range(1, len(l)-n+1):
#     l1.append(i)
# print(l1)
#
# d = input("please enter the direction:").lower()
# if d == "left":
#     c = 0
#     c1 = 0
#     while c1 < n:
#         l2.append(l[c])
#         l.pop(c)
#         c1 += 1
#
# l3 = l + l2
# print(l3)
# ---------------------------------------------------------------------------------------------------------------------
# 111
# l = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# l1 = [0, 3, 5, 7, 10]
# l2 = []
# for each in l1:
#     l2.append(l[each])
# print(l2)
# ---------------------------------------------------------------------------------------------------------------------
# 114. Write a Python program to extract the nth element from a given list of tuples.
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element ( n = 0 ) from the said list of tuples:
# ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element ( n = 2 ) from the said list of tuples:
# [99, 96, 94, 98]


# l = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# n = 2
# l1 = []
# for each in l:
#     l1.append(each[n])
# print(l1)

# ---------------------------------------------------------------------------------------------------------------------

# 115. Write a Python program to check if the elements of a given list are unique or not.
# Original list:
# [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# Is the said list contains all unique elements!
# False
# Original list:
# [2, 4, 6, 8, 10, 12, 14]
# Is the said list contains all unique elements!
# True

# l = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# l = [2, 4, 6, 8, 10, 12, 14]
# l1 = []
# flag = True
# for each in l:
#     if each not in l1:
#         l1.append(each)
# if l == l1:
#     print("Is the said list contains all unique elements!", flag)
# else:
#     flag = False
#     print("Is the said list contains all unique elements!", flag)
# ----------------------------------------------------------------------------------------------------------------------
# 118. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# c = 0
# for i in range(1, len(l)):
#     c1 = l[i] - l[c]
#     l1.append(c1)
#     c += 1
# print(l1)
# ----------------------------------------------------------------------------------------------------------------------
# 122. Write a Python program to find common element(s) in a given nested lists.
# Original lists:
# [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
# Common element(s) in nested lists:
# [18, 12]
# l = [[12, 18, 23, 25, 45, 6], [7, 12, 18, 24, 28, 6], [1, 5, 8, 12, 15, 16, 18, 6]]
# l1 = set(l[0])
# l2 = set(l[1])
# l3 = set(l[2])
# print(list(l1 & l2 & l3))

# -----------------------------------------------------------------------------------------------------------------
#  123. Write a Python program to reverse strings in a given list of string values.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

# l = ['Red', 'Green', 'Blue', 'White', 'Black']
# l1 = [each[::-1]  for each in l]
# print(l1)
# ---------------------------------------------------------------------------------------------------------------------
# 124. Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list.
# The original list, tuple :
# [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list:
# (36, 8)


# l = [(2, 7), (2, 6), (1, 8), (4, 9)]
# l1 = []
# for each in l:
#     l1.append(each[0] * each[1])
# print((max(l1), min(l1)))



# l = [12, 18, 23, 25, 45,7, 12, 18, 24, 28,1, 5, 8, 12, 15, 16, 18, 45]
# # o/p = [12, 18]
# d = {}
# l1 = []
# for each in l:
#     d[each] = l.count(each)
# for x in d:
#     if d[x] > 1:
#         l1.append(x)
# print(l1)

