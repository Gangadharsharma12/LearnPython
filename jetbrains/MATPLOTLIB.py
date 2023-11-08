# n = int(input())
# if n < 0:
#     print("invalid input")
# elif n == 0:
#     print("0 is not a prime number")
# elif n == 1:
#     print("one is neither prime nor composite")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#         print(f"{n} is a prime number")


# n = int(input())
# l = []
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l.append(i)
# print(l)

# n = int(input())
# l = []
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         if len(l) <= n:
#             l.append(i)
# print(l)



# n = int(input())
# l = []
# while len(l) < n:
#     for i in range(2, n):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
# print(l)


# n = int(input("Enter a number : "))
# c = 2
# while n != 0:
#   for i in range(2, c):
#     if c % i == 0:
#       break
#   else:
#     print(c, end=" ")
#     n -= 1
#   c += 1

# a = int(input())
# b = int(input())
# d = {}
# c = 1
# for i in range(2, b):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         d[c] = i
#         c += 1
# print(f"prime numbers between {a} and {b} are:")
# for each in d:
#     if d[each] >= a and d[each] <= b:
#         print(d[each])


# s = input()
# print(f"The given word is {s}")
# s1 = ""
# d = {}
# c = 0
# for each in s:
#     if each not in s1:
#         s1 += each
#         d[each] = c
#     else:
#         if each in s1:
#             d[each] = d[each] + 1
# for i in d:
#     if d[i] == 1:
#         print(f"The duplicate elements are {i} and it repeated {d[i]} time extra")
#     else:
#         if d[i] > 1:
#             print(f"The duplicate elements are {i} and it repeated {d[i]} times extra")

# import keyword
# c = 1
# for each in keyword.kwlist:
#     print(c, "------>", each)
#     c += 1


import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()
