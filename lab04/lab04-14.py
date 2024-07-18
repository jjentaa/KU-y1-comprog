import math
x = int(input())
y = int(input())
p = int(input())

counter = 1
seq = []
runner = x

while(runner<=y):
    if(runner%p):
        seq.append(runner)
        runner+=1
    else:
        runner+=11

if(len(seq)==0): print()
else:
    for i in range(math.ceil(len(seq)/10)):
        for j in seq[(i*10): (i*10)+10]:
            print(j, end=" ")
        print()