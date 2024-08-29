import math

class Cylinder:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_radius(self) -> float:
        return self.radius
    
    def get_height(self) -> float:
        return self.height
    
    def set_radius(self, new_radius: float):
        self.radius = new_radius

    def set_height(self, new_height: float):
        self.height = new_height

    def get_base_area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def get_volume(self) -> float:
        return math.pi*self.radius*self.radius*self.height
    
    def __str__(self) -> str:
        return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"

