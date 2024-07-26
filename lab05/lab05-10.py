ls = list(map(int,input().split()))

counter = 0
while True:
    x, y = map(int,input().split())
    if((-len(ls)<=x<=len(ls)-1) and (-len(ls)<=y<=len(ls)-1)):
        if(y<0): y += len(ls)
        if(x<0): x += len(ls)
        if(x>y): break
        total = 0
        for i in range(x, y+1): total+=ls[i]
        print(total)
    else:
        if(-len(ls)<=x<=len(ls)-1):print("y Bad Input")
        elif(-len(ls)<=y<=len(ls)-1):print("x Bad Input")
        else: print("x and y Bad Input")