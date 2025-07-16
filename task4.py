import math

class Shape:
    def info(self):
        print("shape")

class Circle:
    def __init__(self,r):
        self.radius = r
    
    def area(self):
        self.yuza = math.pi * self.radius ** 2
        print(f"Doira yuzi: {self.yuza:.2f}")



class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def area(self):
        s = self.a * self.b
        print(f"Tug'ri burchakning yuzi {s:.2f}")

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.a = a

    def area(self):
        s = (self.a + self.b + self.c) / 2      
        print(f"Uchburchakning yuzi {s:.2f}")


doira = Circle(154)
tugri = Rectangle(12,15)
uchbur = Triangle(4,5,8)


doira.area()
tugri.area()
uchbur.area()