def add_mai(yr):
    if(yr%4): return False
    else:
        if(yr%100): return True
        else:
            if(yr%400): return True
            else: return False

d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

m2d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
counter = 0
for i in range(m-1):
    counter+=m2d[i]

counter+=d
if(add_mai(y)): counter+=1

print(counter)