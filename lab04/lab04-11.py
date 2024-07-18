d = int(input("Day: "))

n1, n2=1, 1

for i in range(d):
    print(n1, end=" ")
    n1, n2 = n2, n1+n2