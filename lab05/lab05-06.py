ls = list(map(int,input().split()))

while True:
    txt = input()
    if(txt=="E 0"): break
    menu, x = txt.split(" ")
    if(menu=="A"):
        ls.append(int(x))
    elif(menu=="S"):
        print(ls[int(x)])
    elif(menu=="R"):
        ls.pop(int(x))

for i in ls: print(i, end=" ")