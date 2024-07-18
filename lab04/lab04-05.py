scores = []
while True:
    num = input("Enter score (or ENTER to finish): ")
    if(num==''): break
    scores.append(int(num))

scores.sort()
scores.reverse()

for i in range(len(scores)):
    print(f'Rank #{i+1}: {scores[i]}')