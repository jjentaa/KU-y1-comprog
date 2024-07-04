a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))
d = int(input('Input d: '))
e = int(input('Input e: '))

avg = (a+b+c+d+e)/5
print('mean:', format(avg, '.3f'))

sd = 0
for i in [a, b, c, d, e]:
    sd+=(i-avg)**2

sd /= 5
sd = sd**0.5
print('sd:', format(sd, '.3f'))