from math import pi

class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
        
    def area(self):
        oppervlakte = self.w * self.h
        return oppervlakte 

    def perimeter(self):
        omtrek = self.w*2 + self.h*2
        return omtrek

    def set_width(self, w):
        self.w = w
    def set_height(self, h):
        self.h = h
        
class Square(Rectangle):
    def set_width(self, w, h):
        self.width = w
        self.height = h

    def set_height(self, h, w):
        self.width = w
        self.height = h
        
class circle():
    def __init__(self,r, x, y):
        Shape.__init__(self, x, y)
        self.r = r
        self.r = r

    def area(self):
        oppervlakte_circle = pi*self.r**2
        return oppervlakte_circle 

    def perimeter(self):
        omtrek_circle = 2*pi*self.r
        return omtrek_circle

