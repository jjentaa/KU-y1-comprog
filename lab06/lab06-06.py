def northView():
    global mapp
    counter = 0
    for i in range(len(mapp[0])):
        pivot = mapp[0][i]
        counter+=1
        for j in range(len(mapp)):
            if(mapp[j][i]>pivot): 
                counter+=1
                pivot = mapp[j][i]
    
    return counter

def southView():
    global mapp
    counter = 0
    for i in range(len(mapp[0])-1, -1, -1):
        pivot = mapp[-1][i]
        counter+=1
        for j in range(len(mapp)-1, 0, -1):
            if(mapp[-j-1][i]>pivot): 
                counter+=1
                pivot = mapp[-j-1][i]
    
    return counter

def westView():
    global mapp
    counter = 0
    for i in range(len(mapp)):
        pivot = mapp[i][0]
        counter+=1
        for j in range(len(mapp[0])):
            #print(mapp[i][j], pivot)
            if(mapp[i][j]>pivot): 
                counter+=1
                pivot = mapp[i][j]
        #print(counter, i, "eiei")
    
    return counter

def eastView():
    global mapp
    counter = 0
    for i in range(len(mapp)):
        pivot = mapp[i][-1]
        counter+=1
        for j in range(len(mapp[0])-1, -1, -1):
            if(mapp[i][j]>pivot): 
                counter+=1
                pivot = mapp[i][j]
    
    return counter

def decision():
    global mapp
    idx2ans = {0:"N", 1:"S", 2:"E", 3:"W"}
    result = [northView(), southView(), eastView(), westView()]
    #print(result)
    maxx = max(result)
    
    for i in range(len(result)):
        if(result[i]==maxx):
            print(idx2ans[i], end=" ")

m, n = input("City Size: ").split(" ")
m, n = int(m), int(n)

mapp = []

for j in range(m):
    txt = input()
    ls = [int(i) for i in txt.split(" ")]
    mapp.append(ls)

decision()