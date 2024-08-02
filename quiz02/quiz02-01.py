rat = '__QQ\n()">'.split("\n")
hunter = ' O \n/|\\\n/ \\'.split("\n")
lion = ' /\_/\ \n( o.o )\n > ^ < '.split("\n")

patterns = [rat, hunter, lion]

name1 = input("Player1 name: ")
name2 = input("Player2 name: ")

s1 = 0
s2 = 0

for i in range(5):
    if(s1==3 or s2==3): break
    print()
    print(f"Round {i+1}!")
    print(f"{name1} {s1} / {name2} {s2}")
    txt1 = f"{name1}'s choice (1/rat, 2/hunter and 3/lion): "
    txt2 = f"{name2}'s choice (1/rat, 2/hunter and 3/lion): "
    c1 = int(input(txt1))
    c2 = int(input(txt2))
    if(c1==3 and c2==1): s1+=1
    if(c1==3 and c2==2): s2+=1

    if(c1==2 and c2==1): s2+=1
    if(c1==2 and c2==3): s1+=1

    if(c1==1 and c2==2): s1+=1
    if(c1==1 and c2==3): s2+=1

    for j in range(3):
        if(c1==1 and c2==1 and j==2):
            pass
        else:
            if(c1==1 and j==2):
                print("    ", end="  ")
            else:
                print(patterns[c1-1][j], end="  ")

            if(j==1):
                print("VS", end="  ")
            else:
                print("  ", end="  ")

            if(c2==1 and j==2):
                print("    ", end="  ")
            else:
                print(patterns[c2-1][j], end="")
            print()

print()
print(f"{name1} {s1} / {name2} {s2}")

if(s1>s2): print(f"{name1} win!")
elif(s1<s2): print(f"{name2} win!")
else: print("Draw!")

print()

#10.17.124.152