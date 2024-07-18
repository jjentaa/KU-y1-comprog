scores = []
while True:
    num = input("Enter score (or ENTER to finish): ")
    if(num==''): break
    scores.append(int(num))

for i in range(len(scores)):
    print(f"Score #{i+1}: {scores[i]}")

print("Average score is", format(sum(scores)/len(scores), '.2f'))
print("Minimum score is", min(scores))
print("Maximum score is", max(scores))