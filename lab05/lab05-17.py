txt1 = input("Input string: ")
txt2 = input("Input string: ")

txt = ''
for i in txt1:
    if(i not in txt2): txt+=i

for i in txt2:
    if(i not in txt1): txt+=i

print(txt)