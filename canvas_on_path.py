n, m, k = input().split()
n, m, k = int(n), int(m), int(k)

space_ls = []
txt = input().split()
canvas_pos = [int(i) for i in txt]
for j in range(1, m):
    space_ls.append(canvas_pos[j]-canvas_pos[j-1]-1)

space_ls.sort()

for o in range(k-1): 
    if(len(space_ls)): space_ls.pop()
    else: break
summ = 0
for l in space_ls: summ+=l
print(summ)