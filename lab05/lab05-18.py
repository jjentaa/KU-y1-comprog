def txt2ls(text):
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('"', '')
    ls = text.split(", ")
    return ls

def canConcat(text):
    #letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(" ")
    letter2counter = [0]*26
    #for j in letters: letter2counter[j]=0
    for i in text:
        if(97<=ord(i)<=122):
            letter2counter[ord(i)-97]+=1
    
    if(letter2counter.count(0)): return False
    return True

def concat(l1, l2):
    unique_ls = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            new_txt = l1[i]+l2[j]
            if(canConcat(new_txt.lower()) and new_txt not in unique_ls): unique_ls.append(new_txt)

    return unique_ls

txt1 = input("String set1: ")
txt2 = input("String set2: ")

ls1 = eval(txt1)
ls2 = eval(txt2)

result = concat(ls1, ls2)

print("Output:", len(result))
if(len(result)):
    print("The total complete pairs that are forming are:")

    for ele in result:
        print(" "+ele)
