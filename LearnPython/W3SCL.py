# class Parriot:
#     species = "bird"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f"{self.name} is a {Parriot.species}")
#
#     def show(self):
#         print(f"{self.name} is also a {Parriot.species}")
#
#
# p = Parriot("Blu", 10)
# p1 = Parriot("Woo", 15)
# print(f"{p.name} is a {Parriot.species}")
# print(f"{p1.name} is also a {Parriot.species}")
# print(f"{p.name} is {p.age} years old")
# print(f"{p1.name} is {p1.age} years old")

# class Parriot:
#
#     def __init__(self):
#         self.name = "Blu"
#         self.sing()
#
#     def sing(self):
#         print(f"{self.name} sings 'Happy'")
#         self.action()
#
#     def action(self):
#         print(f"{self.name} is now dancing")
#
#
# p = Parriot()


# class Parriot:
#     def __init__(self):
#         print("Bird is ready")
#
#     def run(self):
#         print("bird")
#
#     def swim(self):
#         print("Swim")
#
#
# class Bird(Parriot):
#     def __init__(self):
#         super().__init__()
#         print("Penguin is ready")
#
#     def m1(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
#     def swim(self):
#         print("swim faster")
#
#
# b = Bird()
# b.m1()
# b.swim()
# b.run()




# class Complex:
#     def __init__(self,r = 0, i = 0):
#         self.real = r
#         self.imag = i
#         self.disp()
#
#     def disp(self):
#         print(f"{self.real} + {self.imag}j")
#
# c = Complex(5, 10)
# c1 = Complex(20)
# c1.attr = 10
# print(f"({c1.real}, {c1.imag}, {c1.attr})")






