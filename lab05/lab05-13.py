seq = list(map(int,input().split()))
counter = 0

seq.sort()
# seq.reverse()

while(len(seq)):
    #print(seq)
    x = seq[0]
    # print(x)
    # print(seq)
    if(x==1 and seq.count(3)):
        counter+=1
        seq.remove(1)
        seq.remove(3)
    elif(x==1 and seq.count(2) and seq.count(1)>1):
        counter+=1
        seq.remove(1)
        seq.remove(1)
        seq.remove(2)
    elif(x==1 and seq.count(1)>=4):
        counter+=1
        seq.remove(1)
        seq.remove(1)
        seq.remove(1)
        seq.remove(1)

    elif(x==2 and seq.count(2)>1):
        counter+=1
        seq.remove(2)
        seq.remove(2)
    elif(x==2 and seq.count(1)>=2):
        counter+=1
        seq.remove(1)
        seq.remove(1)
        seq.remove(2)

    elif(x==3 and seq.count(1)):
        counter+=1
        seq.remove(1)
        seq.remove(3)
    else:
        counter+=1
        seq.remove(x)

print(counter)