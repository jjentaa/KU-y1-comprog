x = int(input("Enter horizontal shift size: "))
y = int(input("Enter vertical shift size: "))

mat = []
print("Enter image:")

while True:
    txt = input()
    if(txt=="-1"): break
    mat.append(txt)

l, h = len(mat), len(mat[0])

print("After shift:")
for i in range(l):
    for j in range(h):
        if(i<y): print(0, end="")
        elif(j<x): print(0, end="")
        else: print(mat[i-y][j-x], end="")
    print()