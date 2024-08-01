def isInChain(txt1, txt2):
    counter = 0
    for i in range(len(txt1)):
        if(txt1[i]!=txt2[i]): counter+=1

    if(counter>2): return False
    # print(txt1, txt2, counter)
    return True

text = input("Text: ")
words = text.split(" ")

chain = []
i = 0
j = 0
while(i<len(words)):
    j = i+1
    ls = []
    ls.append(words[i])
    while(j<len(words)):
        if(isInChain(ls[-1], words[j])):
            ls.append(words[j])
            j+=1
        else: 
            chain.append(ls)
            break
    i=j

chain.append(ls)

maxx = max([len(i) for i in chain])
print(f"{len(chain)} Chain(s). Maximum length is {maxx} word(s).")