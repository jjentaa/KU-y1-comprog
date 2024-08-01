def isValid(x, y, m, n):
    if(x<0 or y<0 or x>=n or y>=m): return False
    return True

def bomb_splash(x, y):
    global mapp, m, n
    cols = [1, 0, -1]
    rows = [1, 0, -1]
    for i in rows:
        for j in cols:
            if(i==0 and j==0):
                pass
            else:
                if(isValid(x+i, y+j, m, n)):
                    mapp[x+i][y+j]+=1

m, n = input("Grid Size: ").split(" ")
m = int(m)
n = int(n)

mapp = []
for i in range(n):
    ls = []
    for j in range(m):
        ls.append(0)
    mapp.append(ls)

num = int(input("Number of mine(s): "))
bomb_ls = []
for o in range(num):
    txt = f"Mine#{o+1}: "
    x, y = input(txt).split(" ")
    bomb_ls.append([int(y), int(x)])
    bomb_splash(int(y), int(x))

for p in range(n):
    for q in range(m):
        if([p, q] in bomb_ls):
            print("X", end=" ")
        else:
            print(mapp[p][q], end=" ")
    print()