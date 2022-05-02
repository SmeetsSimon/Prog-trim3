class rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y 
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
        
class Square(rectangle):
    def set_width(self, w, h):
        self.width = w
        self.height = h

    def set_height(self, h, w):
        self.width = w
        self.height = h
