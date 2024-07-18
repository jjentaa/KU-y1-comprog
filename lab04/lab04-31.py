txt = input("Enter text: ")
s = int(input("Enter step: "))

for i in range(len(txt)):
    if(65<=ord(txt[i])<=90): 
        num = ((ord(txt[i])-65)+s)%26
        print(chr(65+num), end="")
    elif(97<=ord(txt[i])<=122):
        num = ((ord(txt[i])-97)+s)%26
        print(chr(num+97), end="")
    else: print(txt[i], end="")