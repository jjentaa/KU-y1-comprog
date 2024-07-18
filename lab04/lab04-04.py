scores = []
while True:
    num = input("Enter score (or ENTER to finish): ")
    if(num==''): break
    scores.append(int(num))

avg = sum(scores)/len(scores)

sd = 0
for i in scores:
    sd+=(i-avg)**2/(len(scores)-1)

sd = sd**0.5

print("Average score is", format(sum(scores)/len(scores), '.2f'))
print("Standard deviation is", format(sd, '.2f'))

for j in range(len(scores)):
    pivot = scores[j]
    if(pivot>=(avg+1.5*sd)): grade="A"
    elif(pivot>=(avg+sd)): grade="B+"
    elif(pivot>=(avg+0.5*sd)): grade="B"
    elif(pivot>=avg): grade="C+"
    elif(pivot>=(avg-0.5*sd)): grade="C"
    elif(pivot>=(avg-sd)): grade="D+"
    elif(pivot>=(avg-1.5*sd)): grade="D"
    else: grade="F"
    print(f'Score #{j+1}: {pivot} grade: {grade}')