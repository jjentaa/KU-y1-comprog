b = int(input("Enter number of bushes: "))
s = int(input("Enter bush size: "))

for i in range(b):
    for j in range(s):
        for k in range(s-j-1):
            print(" ", end="")
        for m in range((j*2)+1):
            print("*", end="")
        print()