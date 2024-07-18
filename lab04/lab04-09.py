def plus(total, value):
    return total+value

def minus(total, value):
    return total-value

n = int(input("How many food you have : "))

total = 0
for i in range(n):
    txt = input()
    num1, num2 = int(txt.split(" ")[0]), int(txt.split(" ")[1])
    total = plus(total, num2*num1)

print(total)