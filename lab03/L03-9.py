import math

def area_of_circle(k):
    return math.pi*(k/2)*(k/2)



d = input("Diameter: ")
d_float = float(d)
area = area_of_circle(d_float)
print("area =", format(area, '.3f'))