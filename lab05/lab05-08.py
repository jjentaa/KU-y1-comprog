n = int(input("N: "))
m = int(input("M: "))

s = set()
for i in range(n):
    txt = f'Input number {i+1}: '
    num = int(input(txt))
    s.add(num%m)
    
print(len(s))