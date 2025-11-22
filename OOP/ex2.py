
class Rectangle:
    def __init__(self,width=1,height=1):
        self.width=width
        self.height=height
    def setWidth(self,width):
        self.width=width
    def setHeight(self,width):
        self.height=height
    def getWidth(self,width):
        return self.width
    def getHeight(self,height):
        return self.height
    def area(self):
        return   self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
    def __str__(self):
        return ("Width:"+ str(self.width) +"\nHeight:"+ str(self.height))
    
rect1=Rectangle(5,7)
print(rect1)
print(rect1.width)
print(rect1.height)
print(rect1.area())
print(rect1.perimeter())


