txt = input("Enter list of words: ")
counter = 0
for c in txt:
    if(97<=ord(c)<=122): counter+=1
print(counter)