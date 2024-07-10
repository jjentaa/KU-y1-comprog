import math

def  MiniHeart(x):
    return (x*x)+math.pi*(x/2)*(x/2)

l = float(input('Please enter the value of L: '))
print('Area is', format(MiniHeart(l), '.4f'))
