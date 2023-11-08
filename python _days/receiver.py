# import pickle
# f = open("C:\\Users\\Gangadhar Sharma\\OneDrive\\Desktop\\python\\dgs.ser", "rb")
# print("Deserilization of objects")
# while True:
#     try:
#         obj = pickle.load(f)
#         print(type(obj))
#         obj.display()



#     except EOFError:
#         print("All objects completed")
#         break
# f.close()
# -------------------------------------------------------------------------------------------------------------------------------
# WAP TO PRINT n fibonacci numbers

# n = int(input("enter a number:"))
# a = 0
# b = 1
# count = 1
# while count <= n:
#     if count == 1:
#         print("The 1st fibonnaci number is {}".format(a))
#     elif count == 2:
#         print("The 2nd fibonacci number is {}".format(a))
#     elif count == 3:
#         print("The 3rd fibonnaci number is {}".format(a))
#     else:
#         print("The {}th fibonnaci number is {}".format(count, a))
#     c = a + b
#     a = b
#     b = c
#     count += 1



# n = int(input("enter a number:"))
# n1 = int(input("enter second number:"))
# d = {}
# count = 1
# a, b = 0, 1
# while count <= n1:
#     c = a + b
#     d[count] = a
#     a = b
#     b = c
#     count += 1
# while n <= n1:
#     print("The {}th fibonacci series is {}".format(n, d[n]))
#     n += 1

# n = int(input("enter a number:"))
# n1 = int(input("enter second number:"))
# a, b = 0, 1
# d = {}
# count = 1
# while count <= n1:
#     c = a + b
#     d[count] = a
#     a = b
#     b = c
#     count += 1
#
# for each in d:
#     if d[each] >= n and d[each] <= n1:
#         print(d[each])

# import time
# fact = 1
# c = 1
# while True:
#     fact *= c
#     print(f"The factorial of {c} is {fact}")
#     c += 1
#     time.sleep(2)
# l1 = [1, 2, 3]
# l2 = [8, 4, 5, 3]








