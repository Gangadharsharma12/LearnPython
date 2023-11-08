# s=input("enter any string:")
# print("The character present at odd places:")
# for x in s:
#     print(s[::2])
#     break
# print("The character present at even places:")
# print(s[1::2])



# s=input("enter a string:")
# for x in s:
#     print(s[-1:-6:-1])
#     break




# s=input("enter a string:")
# l1=s.split()
# n=len(l1)+1
# print(l1)
# for x in l1:
#       print(l1[-1:-n:-1])
#       break


# s=input("enter a string:")
# l1=s.split()
# n=len(s)+1
# print(l1)
# for x in l1:
#     print(x[-1:-n:-1],end=" ")




#5th
# s1=input("enter first string:")
# s2=input("enter second string:")
# a,b=0,0
# output=" "
# while a<len(s1) or b<len(s2):
#         if a<len(s1):
#               output=output+s1[a]
#               a=a+1
#         if b<len(s2):
#               output=output+s2[b]
#               b=b+1
# print(output)


#6th
# s=input("enter any alphanumeric sequence:")
# s1=""
# s2=""
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# target=""
# for x in sorted(s1):
#     target=target+x
# for x in sorted(s2):
#     target=target+x
# print(target)


#9th

# s=input("enter any string:")
# l=set()
# for x in s:
#     if x not in l:
#         l.add(x)
# target="".join(sorted(l))
# print(target)




#11th

# s=input("enter any string:")
# l=s.split()
# #print(l)
# l1=[]
# i=0
# while i<len(l):
#     if i%2==0:
#         l1.append(l[i])
#     else:
#         l1.append(l[i][::-1])
#     i=i+1
# target=" ".join(l1)
# print(target)
# #
# #










