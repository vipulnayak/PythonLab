import math

class shape:
    def __init__(self):
        self.name=""
        self.area=0
    def showarea(self):
        print("the",self.name,"hass area of",self.area,"units")
    
class traingle(shape):
    def __init__(self,base,height):
        self.name="traingle"
        self.area=0
        self.base=base
        self.height=height
    def calcarea(self):
        self.area=0.5*self.base*self.height
        
class rectangle(shape):
    def __init__(self,length,breadth):
        self.name="rectangle"
        self.area=0
        self.length=length
        self.breadth=breadth
    def calcarea(self):
        self.area=self.length*self.breadth
        
class circle(shape):
    def __init__(self,radius):
        self.name="circle"
        self.area=0
        self.radius=radius
    def calcarea(self):
        self.area=math.pi*self.radius*self.radius

c1=circle(6)
c1.calcarea()
c1.showarea()
r=rectangle(6,5)
r.calcarea()
r.showarea()
t=traingle(6,5)
t.calcarea()
t.showarea()
