s = int(input("input: "))

half = s//2
for i in range(half):
    for j in range(half-i):
        print(" ", end="")
    for k in range((i*2)+1):
        print("#", end="")
    print()

print("#"*s)

for i in range(half):
    for j in range(i+1):
        print(" ", end="")
    for k in range((half-i)*2-1):
        print("#", end="")
    print()