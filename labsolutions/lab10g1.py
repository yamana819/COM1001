class Shape:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return ("Shape:"+self.name)    
class Rectangle(Shape):
    def __init__(self,width,height,name=""):
        super().__init__(name)
        self.width=width
        self.height=height
    def areaRect(self):
        return self.width*self.height
    def perimeterRect(self):
        return 2*(self.width+self.height)
    def __str__(self):
        return ("The shape is:"+self.name.title()+" Area:"+str(self.areaRect())+" Perimeter:"+str(self.perimeterRect()))
class Circle(Shape):
    def __init__(self,radius,name=""):
        super().__init__(name)
        self.radius=radius
    def areaCircle(self):
        return 3*(self.radius*self.radius)
    def perimeterCircle(self):
        return 2*3*self.radius
    def __str__(self):
        return ("The shape is:"+self.name.title()+" Area:"+str(self.areaCircle())+" Perimeter:"+str(self.perimeterCircle()))
shape=input("Enter the name of the shape:")
if shape.lower()=="rectangle":
    width=float(input("Enter the width of rectangle:"))
    height=float(input("Enter the height of rectangle:"))
    rect1=Rectangle(height=height,width=width,name=shape)
    print(rect1)
elif shape.lower()=="circle":
    radius=float(input("Enter the radius of circle:"))
    circle=Circle(radius=radius,name=shape)
    print(circle)