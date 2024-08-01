x = int(input("Enter Rook's row position: "))
y = int(input("Enter Rook's column position: "))

print("-----------------")

for i in range(8):
    for j in range(8):
        print("|", end="")
        if(i==x and j==y): print("R", end="")
        elif(i==x or j==y): print("x", end="")
        else: print(" ", end="")
    print("|", end="")
    print()
    print("-----------------")