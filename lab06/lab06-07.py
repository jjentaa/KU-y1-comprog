target = input("Direction to flip square (V/H): ")
n = int(input("Input size of square: "))

mat = []

for i in range(n):
    txt = input()
    ls = [int(i) for i in txt.split(" ")]
    mat.append(ls)

print("After flip:")

if(target=="V"):
    for i in range(n):
        for j in range(n):
            print(mat[n-i-1][j], end=" ")
        print()

else:
    for i in range(n):
        for j in range(n):
            print(mat[i][n-j-1], end=" ")
        print()