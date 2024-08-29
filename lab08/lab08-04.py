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
    
n = Line(1, 1, 4, 4)

print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
print(n.contains(0.0, 0.0))
print(n.contains(1.0, 1.0))
print(n.contains(1.0, 0.0))
print(n.contains(0.0, 1.0))
print(n.contains(2.0, 0.0))
print(n.contains(0.0, 3.0))
print(n.get_distance())
print(n.get_y(3))
print(n.get_y(0))