n = int(input("Enter the number of rows or columns : "))

for i in range(n):
    for j in range(n):
        target = i+j+1
        digits = len(str(target))
        for k in range(2-digits):
            print(" ", end="")
        print(target, end=" ")
    print()