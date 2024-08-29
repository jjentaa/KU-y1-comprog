class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0: return True
        else: return False

    def is_on_y_axis(self):
        if self.__x == 0: return True
        else: return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
    
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)
        self.slope = (y2-y1)/(x2-x1)
        self.y_intersept = y2-(self.slope*x2)

    def contains(self, x, y) -> bool:

        if(self.start_point.get_x()<x<self.end_point.get_x() and self.start_point.get_y()<y<self.end_point.get_y()):
            m1 = (self.end_point.get_y()-y)/(self.end_point.get_x()-x)
            m2 = (y-self.start_point.get_y())/(x-self.start_point.get_x())
            return m1==m2
        if(x==self.start_point.get_x() and y==self.start_point.get_y()):
            return True
        if(x==self.end_point.get_x() and y==self.end_point.get_y()):
            return True
        
        return False
    
    def get_distance(self):
        return ((self.end_point.get_y()-self.start_point.get_y())**2+(self.end_point.get_x()-self.start_point.get_x())**2)**0.5
    
    def get_x1(self):
        return self.start_point.get_x()
    
    def get_y1(self):
        return self.start_point.get_y()
    
    def get_x2(self):
        return self.end_point.get_x()
    
    def get_y2(self):
        return self.end_point.get_y()
    
    def get_y(self, x):
        y = self.slope*x+self.y_intersept
        if(self.contains(x, y)):
            return y
        return -999.999
    
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))

l = Line(x1, y1, x2, y2)

print(f"value of x1 on this line is {l.get_x1():.3f}")
print(f"value of x2 on this line is {l.get_x2():.3f}")
print(f"value of y1 on this line is {l.get_y1():.3f}")
print(f"value of y2 on this line is {l.get_y2():.3f}")

print("==========")

print("Check x and y are on this line ?")
x = float(input("Enter x : "))
y = float(input("Enter y : "))

if(l.contains(x, y)):
    print(f"x = {x:.3f} and y = {y:.3f} are on this line")
else:
    print(f"x = {x:.3f} and y = {y:.3f} are not on this line")

print(f"Distance between startPoint and endPoint is {l.get_distance():.3f}")

print("==========")

print("Find value of y that gives( x , y ) on this line")
x = float(input("Enter x : "))
y = l.get_y(x)
print(f"value of y is {y:.3f}")

if(l.contains(x, y)):
    print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) on this line")
else:
    print(f"( x , y ) = ( {x:.3f} , {y:.3f} ) is not on this line")