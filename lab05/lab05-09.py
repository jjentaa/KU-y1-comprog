def commaCode(myList):
    if(len(myList)):
        if(len(myList)==1): print(myList[0])
        else:
            myList[-1] = "and "+myList[-1]
            print(", ".join(myList))

ls = input("Input: ").split()
commaCode(ls)
