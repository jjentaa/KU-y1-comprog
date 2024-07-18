pos, neg = [], []
while True:
    num = float(input("Enter a number (or just 0 to exit): "))
    if(num==0): 
        pos.append(0)
        neg.append(0)
        break
    if(num>0): pos.append(num)
    if(num<0): neg.append(num)

print("The sum of all positive numbers is", format(sum(pos), '.2f'))
print("The sum of all negative numbers is", format(sum(neg), '.2f'))