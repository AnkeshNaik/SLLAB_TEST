class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def Area(self):
        return self.length*self.breadth


r1=Rectangle(10,40)
print("Area of Rectangle is "+ str(r1.Area()))
