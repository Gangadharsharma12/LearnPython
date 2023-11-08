# for i in range(5):
#     a = 0
#     print(a)
#     for j in range (i+1):
#         print(j+1, end = " ")
#         a = j+1
#     print(a)


# v=["a","e","i","o","u"]
# n=input("enter any name:")
# l=[]
# for x in n:
#     if x in v:
#         l.append(x)
#     print(l)



# n=int(input("enter any value:"))      ***
# for i in range(n):                    ***
#      print("*"*n)                     ***



# n=int(input("enter any value:"))
# for i in range(1,n+1):                111
#     for j in range(1,n+1):            222
#         print(i,end=" ")              333
#     print()


# n=int(input("enter any value:"))      1 2 3 4
# for i in range(1,n+1):                1 2 3 4
#     for j in range(1,n+1):            1 2 3 4
#         print(j,end=" ")              1 2 3 4
#     print()




# n=int(input("enter any value:"))         A A A A
# for i in range(1,n+1):                   B B B B
#     for j in range(1,n+1):               C C C C
#         print(chr(64+i),end=" ")         D D D D
#     print()


# n=int(input("enter any value:"))         A B C D
# for i in range(1,n+1):                   A B C D
#     for j in range(1,n+1):               A B C D
#         print(chr(64+j),end=" ")         A B C D
#     print()


# n=int(input("enter any value:"))          5 5 5 5 5
# for i in range(1,n+1):                    4 4 4 4 4
#     for j in range(1,n+1):                3 3 3 3 3
#         print(n+1-i,end=" ")              2 2 2 2 2
#     print()                               1 1 1 1 1


# n = int(input("enter any value:"))          6 5 4 3 2 1
# for i in range(1,n+1):                      6 5 4 3 2 1
#     for j in range(1,n+1):                  6 5 4 3 2 1
#         print(n+1-j,end=" ")                6 5 4 3 2 1
#     print()                                 6 5 4 3 2 1




# n = int(input("enter any value:"))            J J J J J J J J J J
# for i in range (1,n):                         I I I I I I I I I I
#     for j in range(1,n):                      H H H H H H H H H H
#         print(chr(64-i+n),end=" ")            G G G G G G G G G G
#     print()                                   F F F F F F F F F F


# n = int(input("enter any value:"))              E D C B A
# for i in range (1,n):                           E D C B A
#     for j in range(1,n):                        E D C B A
#         print(chr(64+n-j),end=" ")              E D C B A
#     print()                                     E D C B A


# n = int(input("enter any value:"))                *
# for i in range(n):                                *  *
#     for j in range(i+1):                          *  *  *
#         print("*",end=" ")                        *  *  *  *
#     print()                                       *  *  *   *   *



# n = int(input("enter any value:"))                 1
# for i in range(n):                                 2  2
#     for j in range(i+1):                           3  3  3
#         print(i+1,end=" ")                         4  4  4 4
#     print()                                        5  5  5  5 5


# n = int(input("enter any value:"))                  1
# for i in range(n):                                  1  2
#     for j in range(i+1):                            1  2  3
#         print(j+1,end=" ")                          1  2  3  4
#     print()                                         1  2  3  4  5



# n = int(input("enter any value:"))                   A
# for i in range(1,n+1):                               B  B
#     for j in range(i):                               C  C  C
#         print(chr(64+i),end=" ")                     D  D  D  D
#     print()                                          E  E  E  E  E


# n = int(input("enter any value:"))                     A
# for i in range(1,n+1):                                 A  B
#     for j in range(i):                                 A  B  C
#         print(chr(65+j),end=" ")                       A  B  C  D
#     print()                                            A  B  C  D  E




# n = int(input("enter any value:"))                  * * * * *
# for i in range(1,n+1):                              * * * *
#     for j in range(1,n+2-i):                        * * *
#         print("*",end=" ")                          * *
#     print()                                         *



# n = int(input("enter any value:"))                 1 1 1 1 1
# for i in range(1,n+1):                             2 2 2 2
#     for j in range(1,n+2-i):                       3 3 3
#         print(i,end=" ")                           4 4
#     print()                                        5



# n = int(input("enter any value:"))                   1 2 3 4 5
# for i in range(1,n+1):                               1 2 3 4
#     for j in range(1,n+2-i):                         1 2 3
#         print(j,end=" ")                             1 2
#     print()                                          1



# n = int(input("enter any value:"))                 A A A A A
# for i in range(1,n+1):                             B B B B
#     for j in range(1, n + 2 - i):                  C C C
#         print(chr(64+i),end=" ")                   D D
#     print()                                        E


# n = int(input("enter any value:"))             A B C D E
# for i in range(1,n+1):                         A B C D
#     for j in range(1, n + 2 - i):              A B C
#         print(chr(64 + j), end=" ")            A B
#     print()                                    A



# n = int(input("enter any value:"))
# for i in range(1,n):
#     for j in range(1,n+1-i):
#         print((n-i),end=" ")
#     print()










# n = int(input())
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end = " ")
#     for k in range(i + 1):
#         print("*", end = " ")
#     print()



# x = int(input("Enter the base number:"))
# y = int(input("Enter the power number:"))
# power = 1
# sum = 0
# for i in range(1, y + 1):
#     if i % 2 != 0:
#         sum = sum + (x ** power)
#     elif i % 2 == 0:
#         sum = sum - (x ** power)
#     power = power + 2
# print(sum)



# #Return the factorial of the number N
# def factorial(N):
#     # Your code goes here
#     fact = 1
#     i = 1
#     while i <= N:
#         fact *= i
#         i += 1
#     return fact
# N = int(input())
# print(factorial(N))


