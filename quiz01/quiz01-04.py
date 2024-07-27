seq1 = input("ผลการสำรวจ: ")
seq2 = seq1.split(" ")
seq = []
for i in seq2: seq.append(int(i))
h = max(seq)

print("แผนที่:")

for i in range(h):
    for j in range(len(seq)):
        if(seq[j]>=h-i):
            if(seq[j]-h+i>=8):
                print("x", end="")
            elif(seq[j]-h+i>=4):
                print("=", end="")
            else:
                print("o", end="")
        else:
            print(" ", end="")
    print()
   

print("อาจารย์โตโต้เดินทางไปปักธงที่จุดยอดสูงสุด:")
idx = seq.index(h)
l = len(seq)-idx


for i in range(6):
    for j in range(idx):
        print(" ", end="")
    if(i==0 or i==2):
        print("+-------+"[0:l], end="")
    elif(i==1):
        print("| CPE38 |"[0:l], end="")
    else: print("|", end="")
    print()

for i in range(h):
    for j in range(len(seq)):
        if(seq[j]>=h-i):
            if(seq[j]-h+i>=8):
                print("x", end="")
            elif(seq[j]-h+i>=4):
                print("=", end="")
            else:
                print("o", end="")
        else:
            print(" ", end="")
    print()

