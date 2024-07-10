def distance(a, t):
    s = 0.5*a*t*t
    return s

acceleration = int(input("Acceleration : "))
time = int(input("Time : "))
print(distance(acceleration,time))