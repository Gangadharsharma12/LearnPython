# class Student:
#     def __init__(self):
#         self.name = "Gangadhar"
#         self.roll no = 101
#         self.marks = 90
#     def speak(self):
#         print("hello my name is:",self.name)
#         print("hello my roll no is:",self.rollno)
#         print("hello my marks are:",self.marks)
# s=Student()
# print(f"my name is {s.name}")
# print(f"my roll no is {s.roll no}")
# print(f"my marks are {s.marks}")
# s.speak()


# class Test:
#     def __init__(self):
#         print("This is a constructor")
#     def a1(self,x):
#         print("This is a method")
# t=Test()
# t.a1(20)


# class Employee:
#     def __init__(melf,x,y,z):
#         melf.x = x
#         melf.y = y
#         melf.z = z
# e1 = Employee("abc",30,20000)
# print(e1.y)
# print(e1.z)
# print(e1.x)python
p



class Movie:
    ''' movie application created by dgs'''
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def info(self):
        print("Movie name:", self.title)
        print("Hero name:", self.hero)
        print("Heroine name:", self.heroine)

list_of_movies = []
while True:
    title = input("Enter the title of a movie:")
    hero = input("Enter hero name:")
    heroine = input("Enter heroine name:")
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print("movie added to list successfully")
    choice = input("Do you want to add one more movie [Yes|No]:")
    if choice.lower() == "no":
        break
print()
print("All movies updated")
print("#" * 45)
for i in list_of_movies:
    i.info()
    print()


