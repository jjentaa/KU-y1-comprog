seq = []
while True:
    num = int(input())
    seq.append(num)
    if(num==0): break

counter=1
max_count = 1
pivot = seq[0]

if(len(seq)>1):
    for i in range(1, len(seq)):
        if(seq[i]==seq[i-1]): 
            counter+=1
            #print("c=",counter)
        else:
            if(max_count<counter):
                max_count=counter
                pivot = seq[i-1]
                counter=0
    if(max_count<counter):
        max_count=counter
        pivot = seq[-1]
        counter=1

print(max_count)
print(pivot)