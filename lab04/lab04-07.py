txt = input("What is your message? ")

for i in range(len(txt)):
    for j in range(i): print(" ", end="")
    print(txt[i])