def isValid(x, y, n):
    if(x<0 or y<0 or x>=n or y>=n): return False
    return True

rows = [-2, -1, 0, 1, 2]
cols = [-2, -1, 0, 1, 2]

n = int(input())
state = []
area = []
for i in range(n):
    txt = input()

    for m in range(len(txt)):
        x = i
        y = m
        if(txt[m]=="G"):
        #record bomb coor
            for j in range(len(rows)):
                for k in range(len(cols)):
                    newX = x+rows[j]
                    newY = y+cols[k]
                    if(isValid(newX, newY, n)): area.append([newX, newY])

        # record enemy coor
        if(txt[m]=="E"): state.append([x, y])

counter = 0
for pos in state:
    if(pos in area): counter+=1

print(counter)