class Triangle:
    def __init__(self):
        self.base=0
        self.height=0
        self.area=0
    def read(self,base,height):
        self.base=base
        self.height=height
    def display(self):
        self.area=0.5*self.base*self.height
        print("area of triangle: ",self.area)
t1=Triangle()
t1.read(2,6)
t1.display()
class Circle:
    def __init__(self):
        self.radius=0
        self.area=0
    def read(self,radius):
        self.radius=radius
    def display(self):
        self.area=3.16*self.radius*self.radius
        print("area of circle: ",self.area)
c1=Circle()
c1.read(4)
c1.display()
class Rectangle:
    def __init__(self):
        self.base=0
        self.length=0
        self.area=0
    def read(self,base,length):
        self.base=base
        self.length=length
    def display(self):
        self.area=self.base*self.length
        print("area of triangle: ",self.area)
r1=Rectangle()
r1.read(2,6)
r1.display()
        
