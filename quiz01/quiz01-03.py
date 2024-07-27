def DrawRat():
  s='__QQ\n()">\n'
  print(s)
  
def DrawHunter():
  s=' O\n/|\ \n/ \ \n'
  print(s)
  
def DrawLion():
  s=' /\_/\ \n( o.o )\n > ^ <\n'
  print(s)
  
p1 = input("Player1 name: ")
p2 = input("Player2 name: ")
print()
s1, s2 = 0, 0

print("Round 1!")
print(f"{p1} {s1} / {p2} {s2}")
c1 = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
c2 = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
print()
print(p1)
if(c1==1): DrawRat()
elif(c1==2): DrawHunter()
elif(c1==3): DrawLion()
print("VS")

print()
print(p2)
if(c2==1): DrawRat()
elif(c2==2): DrawHunter()
elif(c2==3): DrawLion()

if(c1==1 and c2==2): s1+=1
elif(c1==1 and c2==3): s2+=1
elif(c1==3 and c2==2): s2+=1
elif(c1==3 and c2==1): s1+=1
elif(c1==2 and c2==3): s1+=1
elif(c1==2 and c2==1): s2+=1

print("Round 2!")
print(f"{p1} {s1} / {p2} {s2}")
c1 = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
c2 = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
print()
print(p1)
if(c1==1): DrawRat()
elif(c1==2): DrawHunter()
elif(c1==3): DrawLion()
print("VS")

print()
print(p2)
if(c2==1): DrawRat()
elif(c2==2): DrawHunter()
elif(c2==3): DrawLion()

if(c1==1 and c2==2): s1+=1
elif(c1==1 and c2==3): s2+=1
elif(c1==3 and c2==2): s2+=1
elif(c1==3 and c2==1): s1+=1
elif(c1==2 and c2==3): s1+=1
elif(c1==2 and c2==1): s2+=1

if(s1!=2 and s2!=2):
    print("Round 3!")
    print(f"{p1} {s1} / {p2} {s2}")
    c1 = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    c2 = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
    print()
    print(p1)
    if(c1==1): DrawRat()
    elif(c1==2): DrawHunter()
    elif(c1==3): DrawLion()
    print("VS")
    print()

    print(p2)
    if(c2==1): DrawRat()
    elif(c2==2): DrawHunter()
    elif(c2==3): DrawLion()


    if(c1==1 and c2==2): s1+=1
    elif(c1==1 and c2==3): s2+=1
    elif(c1==3 and c2==2): s2+=1
    elif(c1==3 and c2==1): s1+=1
    elif(c1==2 and c2==3): s1+=1
    elif(c1==2 and c2==1): s2+=1

print(f"{p1} {s1} / {p2} {s2}")
if(s1>s2): print(p1, "win!")
elif(s1<s2): print(p2, "win!")
else: print("Draw!")
